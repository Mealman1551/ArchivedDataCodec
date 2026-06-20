# ADC Archive Format Specification

Name: ArchivedDataCodec (ADC)
Status: Matches reference implementation in this repository
License: GNU GPL v3.0 (see project)

## 1. Scope and intent

This document describes the exact on-disk layout produced and consumed by the
reference implementation in `src/libadc` of this repository. It is intended as a
precise, implementation-backed specification so third-party tools can interoperate
with ADC archives produced by this project.

## 2. Design goals

The implementation and format prioritize:

- Structural simplicity and sequential layout
- Easy streaming read/write (no global index)
- Per-file compression and optional encryption
- Minimal but sufficient metadata for integrity checks

## 3. High-level layout

An ADC file is a linear sequence of bytes containing (one of):

- A header identifying ADC V1 (current) or V0 (earlier), followed by file entries
- Or no header (legacy format) followed by file entries in the legacy layout

There is no global footer or index. Files are written and read sequentially.

## 4. Headers and format versions

The reference implementation recognizes three cases when reading an archive:

- ADC V1 (current): 8-byte header `ADCARCH\x01` (ASCII), followed by an
	encryption flag byte and then optional salt and file entries.
- ADC V0: 8-byte header `ADCARCH\x00` (ASCII), followed by a 16-byte salt and
	then file entries (files are encrypted in this mode).
- Legacy (pre-ADC header, e.g. 1.2.0): no 8-byte header present; the reader
	falls back to legacy parsing rules (4-byte data length and no CRC field).

Constants from the implementation:

- V1 header: `ADCARCH\x01` (bytes)
- V0 header: `ADCARCH\x00` (bytes)
- Salt size: 16 bytes
- PBKDF2 iterations: 390000

These constants are defined in `src/libadc/constants.py`.

## 5. ADC V1 (current) on-disk layout

When creating an ADC V1 archive the writer performs the following sequence:

1. Write the 8-byte header `ADCARCH\x01`.
2. Write a single encryption flag byte:
	 - `0x00` = not encrypted
	 - `0x01` = encrypted (password supplied)
3. If encrypted, write `SALT_SIZE` (16) random bytes (the salt used for PBKDF2).
4. Write one or more file entries (see section 7).

Notes:

- When encrypted, the implementation derives a 32-byte key via PBKDF2-HMAC-SHA256
	with `PBKDF2_ITERATIONS = 390000` and then encodes the derived key with
	URL-safe base64 for use with `cryptography.fernet.Fernet` (see
	`src/libadc/crypto.py`).
- Compression (zlib) is applied before encryption.

## 6. ADC V0 layout

ADC V0 archives begin with the 8-byte header `ADCARCH\x00` followed immediately
by a 16-byte salt. In V0 the implementation expects encrypted files and derives
the key the same way as V1. The rest of the file entries use the same per-file
layout as V1 except that the header implied encryption and there is no explicit
encryption flag byte.

## 7. Per-file entry layout (V1 and V0)

Each stored file in V1/V0 is written sequentially using the following fields:

Field                Size           Description
--------------------  -------------  -------------------------------------------------
Filename length      2 bytes        Unsigned big-endian integer (N)
Filename             N bytes        UTF-8 encoded path relative to input root
Data length          8 bytes        Unsigned big-endian integer (M) — length of the
																	 following data field (after compression and
																	 optional encryption)
CRC32                4 bytes        CRC32 (big-endian) of the original uncompressed
																	 file bytes (computed before compression)
Data                 M bytes        Compressed file data (zlib.compress) or the
																	 encrypted form of that compressed blob when
																	 the archive is encrypted.

Details:

- Filenames are encoded in UTF-8 and the implementation writes the 2-byte
	filename length in big-endian order. Maximum filename length is 65535
	bytes due to the 2-byte length field.
- The CRC32 is computed over the original (pre-compression) data using
	`zlib.crc32(...) & 0xFFFFFFFF` and stored as 4 big-endian bytes. The
	extractor verifies this CRC when present and warns on mismatches.
- Compression uses `zlib.compress()` (wrapped as `parma_compress` in
	`src/libadc/compression.py`). Compression is cached in-memory by the
	implementation to speed repeated operations.
- When encryption is enabled (V1 with flag `0x01` or V0), the compressed data
	is encrypted using `cryptography.fernet.Fernet` with the key derived from the
	password and the per-archive salt; the encrypted blob is what is written as
	the `Data` field and its length is stored in the 8-byte Data length field.

## 8. Legacy (pre-header) layout

For legacy archives (detected by the absence of the 8-byte headers), the
implementation falls back to a legacy parsing mode compatible with older
releases (not recommended for newly created archives). The main differences
are:

- There is no 8-byte ADC header.
- Data length is stored as a 4-byte big-endian integer instead of 8 bytes.
- No CRC32 field is present in the legacy layout; only zlib-compressed blobs
	are written/read.

## 9. Compression and integrity

- Compression: `zlib` (via `parma_compress` / `parma_decompress` wrappers).
- Integrity: CRC32 per file (4 bytes) for V1/V0 archives. Encrypted archives
	additionally rely on Fernet authentication to detect tampering of the
	compressed payload.

## 10. Limits and assumptions

- Filename length: limited to 65535 bytes (2-byte length field)
- File data length: effectively limited by the 8-byte unsigned field (2^64-1)
- No timestamps, permissions, or ownership metadata are stored by the
	reference implementation.

## 11. Reference implementation notes

- The precise behavior is implemented in `src/libadc/archive.py`.
- Key derivation and Fernet key encoding are in `src/libadc/crypto.py`.
- Compression and I/O helpers are in `src/libadc/compression.py`.
- Format constants live in `src/libadc/constants.py`.

---

###### Made with 💚 by Mealman1551

---

###### © 2024 - 2026 Mealman1551 – The ADC Project and [contributors](/community/contributors.txt)  
###### Licensed under the GNU GPL v3.0 or later.

