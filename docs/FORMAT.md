# ADC Archive Format Specification

Name: ArchivedDataCodec (ADC)
Status: Stable (v1.5)
License: GPLv3 or later

## 1. Scope and intent

ADC is a simple archive container format. It defines how multiple files are stored sequentially in a single binary file. The project focuses on container structure, documentation, and ease of implementation.

ADC does not attempt to preserve file formats long term, guarantee future readability of archived content, or compete with existing archive standards such as tar or zip.

## 2. Design goals

The format is designed with the following goals in mind:

* Structural simplicity
* Linear, sequential layout
* Easy manual inspection if necessary
* Easy to reimplement without external tooling
* Minimal metadata

## 3. High-level layout

An ADC archive consists of the following elements in order:

* Archive header (current v1 format)
* One or more file entries

There is no global index, footer, or central directory. The archive is read from start to end.

## 4. ADC v1 header

The current format version uses an 8-byte magic header followed by an encryption flag.

Offset  Size   Description
0       8      Magic string: `ADCARCH\x01`
8       1      Encryption flag: `0x00` = no encryption, `0x01` = encrypted
9       16     Random salt used for key derivation (only when encrypted)

If the encryption flag is `0x01`, the following 16-byte salt is present and the subsequent file data is encrypted using Fernet.

## 5. Legacy format compatibility

The implementation also supports older archive layouts:

* V0 encrypted archives begin with `ADCARCH\x00` followed by a 16-byte salt and encrypted file payloads.
* V0 non-encrypted archives contain no magic header and begin directly with file entries.

New archives created by the current implementation always use the v1 header.

## 6. File entry format

Each file entry is stored sequentially and consists of the following fields:

Field              Size    Description
Filename length    2       Unsigned big-endian integer
Filename           N       UTF-8 encoded filename
Data length        8       Unsigned big-endian integer
CRC32              4       CRC32 of original file data
Data               M       Compressed or encrypted payload

The data payload contains the compressed file bytes. When encryption is enabled, this payload is the Fernet-encrypted compressed data.

There is no padding or alignment between file entries.

Directories are not stored explicitly. Directory structure is implied by path separators in filenames.

## 7. Compression

Compression is applied per file using zlib via the `parma_compress`/`parma_decompress` functions.

The payload written to the archive is:

* `zlib.compress(original_data)` when unencrypted
* `Fernet.encrypt(zlib.compress(original_data))` when encrypted

## 8. Encryption

When encryption is enabled, the v1 header sets the encryption flag to `0x01` and includes a random 16-byte salt.

* Key derivation: PBKDF2-HMAC-SHA256
* Iterations: 390000
* Salt size: 16 bytes
* Key length: 32 bytes
* Encryption method: Fernet

The encryption key is derived from the user password and salt, then used to encrypt the compressed file payload.

## 9. Integrity checking

For v1 archives, each file entry includes a 4-byte CRC32 of the original data.

During extraction, the implementation recomputes CRC32 on the decompressed file and reports a mismatch if it differs from the stored value.

## 10. Limits and assumptions

* Maximum filename length: 65535 bytes
* Maximum file data size: 2^64 - 1 bytes (theoretical)
* No timestamps, permissions, or ownership metadata
* No global checksum beyond what zlib or Fernet provide
* File order is preserved as written

These limits are deliberate design trade-offs in favor of simplicity and clarity.

## 11. Forward compatibility

The current format includes explicit header bytes for version detection. Future revisions may introduce additional metadata blocks or optional versioned headers while retaining sequential file entries.

## 12. Reference implementation

The reference implementation of this format is the ADC Archiver project written in Python.

The specification in this document is considered authoritative, not just the behavior of the current implementation.

---

###### Made with 💚 by Mealman1551

---

###### © 2024 - 2026 Mealman1551 – The ADC Project and [contributors](/community/contributors.txt)
###### Licensed under the GNU GPL v3.0 or later.
