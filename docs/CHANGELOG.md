# Changelog

## ADC Archiver 1.5.0 (Borealis)

Changes since v1.4.5 "Grand Canyon" LTS.

---

### New Features

- Multi-format archive support (TAR, TAR.GZ, TAR.XZ, TAR.BZ2, 7Z)
- CRC32 integrity checking
- Headless/CLI mode with auto-detection
- Folder selection in UI
- OS-specific ASCII banners

---

### Improvements

- Package restructure: core moved to `src/libadc/`
- Fixed Nuitka build configuration
- Cleaned up Makefile (removed legacy targets)
- Fixed installer script on Linux (Bash) (install.sh)
- More quit command options
- Extraction creates subdirectory instead of throwing everything in the `.` directory
- File dialog shows all new supported archive formats (eg. tar.xz etc.)
- Caching for compress/decompress operations
- ADC archive version header (V1 new for CRC32 integrity checking)
- Updated dependencies
- Rewrote CONTRIBUTING.md
