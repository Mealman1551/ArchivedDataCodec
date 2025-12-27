# ADC Archive Format Specification

Name: ArchivedDataCodec (ADC)
Status: Stable (v1.4.x)
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

* Optional archive header (only present when encryption is enabled)
* One or more file entries

There is no global index or footer. The archive is read from start to end.

## 4. Archive header (optional)

The archive header is only present for encrypted archives.

Offset  Size   Description
0       8      Magic string: ADCARCH\0
8       16     Random salt used for key derivation

If the magic string is not present, the archive is treated as unencrypted.

## 5. File entry format

Each file entry is stored sequentially and consists of the following fields:

Field              Size    Description
Filename length    2       Unsigned big-endian integer
Filename           N       UTF-8 encoded filename
Data length        8       Unsigned big-endian integer
Data               M       Compressed file data

There is no padding or alignment between file entries.

Directories are not stored explicitly. Directory structure is implied by path separators in filenames.

## 6. Compression

Compression is applied per file using zlib.

ADC intentionally reuses an existing, widely supported compression algorithm. The purpose of the project is the container format, not the compression method itself.

## 7. Encryption (optional)

When encryption is enabled, the following scheme is used:

* Key derivation: PBKDF2-HMAC-SHA256
* Salt size: 16 bytes
* Key length: 32 bytes
* Encryption method: Fernet (symmetric encryption)

Compression is applied before encryption.

## 8. Limits and assumptions

* Maximum filename length: 65535 bytes
* Maximum file data size: 2^64 - 1 bytes (theoretical)
* No timestamps, permissions, or ownership metadata
* No global checksum beyond what zlib or Fernet provide

These limits are deliberate design trade-offs in favor of simplicity and clarity.

## 9. Forward compatibility

The format currently has no explicit version field. Future revisions may introduce optional versioned headers or additional metadata blocks.

Changes are expected to remain backward compatible where possible.

## 10. Reference implementation

The reference implementation of this format is the ADC Archiver project written in Python.

The specification in this document is considered authoritative, not just the behavior of the current implementation.

---

###### Made with 💚 by Mealman1551

---

###### © 2024 - 2025 Mealman1551 – The ADC Project and [contributors](contributors.txt)  
###### Licensed under the GNU GPL v3.0 or later.

