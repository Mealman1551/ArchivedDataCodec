# Changelog

## ADC Archiver 1.5.0

Changes since v1.4.5 "Grand Canyon" LTS.

---

### New Features

- Multi-format archive support (TAR, TAR.GZ, TAR.XZ, TAR.BZ2, 7Z)
- ADC archive encryption with PBKDF2 + Fernet
- CRC32 integrity checking
- Headless/CLI mode with auto-detection
- Folder selection in UI
- OS-specific ASCII banners

---

### Improvements

- Package restructure: core moved to `src/libadc/`
- Fixed Nuitka build configuration
- Cleaned up Makefile (removed legacy targets)
- Fixed installer script
- More quit command options
- Extraction creates subdirectory
- File dialog shows all archive formats
- Caching for compress/decompress operations
- ADC archive version header (V1)
- Updated dependencies
- Rewrote CONTRIBUTING.md
