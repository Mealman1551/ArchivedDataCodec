# Changelog

## ADC Archiver 1.5.0

Changes since v1.4.5 "Grand Canyon" LTS.

---

### New Features

- **Multi-format archive support** - Added support for creating and extracting TAR, TAR.GZ, TAR.XZ, TAR.BZ2, and 7Z archives alongside the existing ADC and ZIP formats.
- **ADC archive encryption** - Archives in ADC format can now optionally be protected with a password. Key derivation uses PBKDF2 with a random salt; encryption uses Fernet.
- **CRC32 integrity checking** - ADC archives now embed a CRC32 checksum per file, verified on extraction.
- **Headless/CLI mode** - New `src/adc/headless.py` module enabling full create/extract workflows without a display (e.g. over SSH or in CI). Activated automatically when no display is detected or `--headless` is passed.
- **Display auto-detection** - The application detects whether a display server (X11/Wayland) is available and falls back to headless mode automatically.
- **Folder selection in UI** - The file picker now allows selecting additional directories to include in an archive, not just individual files.
- **GitLab mirror workflow** - New `gitlab-mirror.yml` GitHub Actions workflow that keeps a full mirror of all branches and tags in sync to GitLab, replacing the old `gitlab-sync.yml`.
- **`pyproject.toml`** - Added `pyproject.toml` for standard Python packaging (`setuptools`).
- **Application ID** - Added `docs/appid` containing a unique application GUID.
- **Mailing list rules** - Added `docs/mailinglist_rules.md` documenting subject prefixes, posting guidelines, and community rules for the ADC mailing list.
- **OS-specific ASCII banners** - The startup banner now shows a different color scheme depending on the OS: teal for Linux, blue for Windows, light green for other platforms.

---

### Improvements

- **Package restructure** - Core library code moved from `src/adc/` into a new `src/libadc/` package. The `src/adc/` package now acts as the application layer on top of `libadc`. The top-level `adc.py` entrypoint was replaced by `src/adc.py`.
- **Nuitka build fix** - The Nuitka compilation command in `build.yml` and `Makefile` was updated to use `PYTHONPATH=src`, `--include-package=libadc`, and `--include-package=adc` to correctly resolve the `src/` layout.
- **Makefile cleanup** - Removed all legacy per-version build targets (1.0.0 through 1.3.1). Build targets now use a generic `ADC_Archiver` name and the corrected `src/adc.py` entrypoint. Install and remove targets were simplified and made more robust (commands now use `|| true` to avoid hard failures on missing tools).
- **Installer fix** - The install wrapper script (`invterm.sh`) logic was corrected. The previous version incorrectly wrote both a terminal-emulator detection block and a direct binary invocation; it now correctly detects the available terminal emulator (gnome-terminal, xfce4-terminal, mate-terminal, konsole, xterm) and invokes the binary through it. `Terminal=false` in the `.desktop` file was corrected to `Terminal=true`.
- **Expanded quit commands** - The interactive prompt now accepts a wider set of quit keywords (`quit`, `exit`, `stop`, `bye`, `goodbye`, `end`, `close`, `terminate`, `shutdown`, `leave`, `byebye`) in addition to `q`.
- **Improved extraction output** - Extraction now creates a subdirectory named after the archive rather than dumping files directly into the target directory.
- **File dialog improvements** - `open_archive_file()` now shows all supported archive types (ADC, ZIP, 7Z, TAR, TAR.GZ, TAR.XZ, TAR.BZ2) rather than only ADC. `save_archive_file()` sets the correct extension and file type filter for every supported format.
- **Caching in compression and archive modules** - `parma_compress`, `parma_decompress`, and `read_binary_file` use `lru_cache` keyed on file mtime so repeated reads of unchanged files are fast, while changes are picked up correctly.
- **ADC archive version header** - New `ADC_HEADER_V1` (`ADCARCH\x01`) distinguishes v1 archives (with CRC32 and explicit encryption flag) from v0 archives (`ADCARCH\x00`). Extraction remains backward compatible with both.
- **Version string** - Version is now reported as `"development version"` in this Aurora snapshot rather than `"1.4.5"`.
- **CONTRIBUTING.md rewrite** - The contribution guide was fully rewritten with detailed sections covering repository structure, branch model, PR workflow, and project philosophy.
- **Updated dependencies** - `cryptography` bumped from 46.0.6 to 46.0.7; `py7zr` 1.1.0 added.
- **Security policy updated** - Versions 1.1 and 1.2 are now marked as end-of-life (no longer supported).
- **Download counters updated** - `.github/downloads.json` updated to reflect current download totals.

---

### Removals

- **Legacy source files removed** - All files under `src/legacy/` (versions 1.0.0 through 1.4.3) have been deleted from the repository.
- **`src/adc/archive.py` and `src/adc/compression.py` removed** - Functionality consolidated into `src/libadc/archive.py` and `src/libadc/compression.py`.
- **`runtime.txt` removed.**
- **GitHub issue templates removed** - `bug_report.md` and `feature_request.md` deleted from `.github/ISSUE_TEMPLATE/`.
- **`gitlab-sync.yml` removed** - Replaced by the new `gitlab-mirror.yml`.
- **Top-level `adc.py` removed** - Replaced by `src/adc.py`.

---

### Tests

- Import paths in all test files updated from `adc.*` to `libadc.*`.
- New tests added for `read_binary_file` cache invalidation on file write, and for `_list_files_in_path` cache updates when directory contents change.
- `test_constants.py` updated to expect `VERSION == "development version"`.
