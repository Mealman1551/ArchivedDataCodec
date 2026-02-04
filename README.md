<img src="https://raw.githubusercontent.com/The-ADC-Archiver-Project/Assets/refs/heads/main/banner/ADC%20banner.jpg" alt="ADC Banner" width=200>

---

[ADC contact e-mail address](mailto:nathandubuy4+adc@gmail.com)

[Mailinglist](https://groups.google.com/g/adc-archiver) (Main announcement channel)

IRC: OFTC - #adc-archiver (Only used for meetings and events)

# ADC (ArchivedDataCodec)

[![GitHub license](https://img.shields.io/github/license/Mealman1551/ADC)](#)
[![Platform: Windows/Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-blue.svg)](#)
[![Development](https://img.shields.io/badge/Development-Active-brightgreen)](#)
[![Latest version](https://img.shields.io/github/v/release/Mealman1551/ADC?label=Latest%20version&color=brightgreen)](https://github.com/mealman1551/adc/releases/latest)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)](#)
[![GitHub repo size](https://img.shields.io/github/repo-size/Mealman1551/ADC)](#)
[![GitHub issues](https://img.shields.io/github/issues/Mealman1551/ADC)](https://github.com/Mealman1551/ADC/issues)
[![GitHub stars](https://img.shields.io/github/stars/Mealman1551/ADC)](#)
[![StandWithUkraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg)](#)
[![GitLab Sync Status](https://github.com/Mealman1551/ADC/actions/workflows/gitlab-sync.yml/badge.svg?branch=main)](https://github.com/Mealman1551/ADC/actions/workflows/gitlab-sync.yml)
[![Build Status](https://github.com/Mealman1551/ADC/actions/workflows/build.yml/badge.svg)](https://github.com/Mealman1551/ADC/actions/workflows/build.yml)
![Total Downloads](https://img.shields.io/badge/dynamic/json.svg?url=https://raw.githubusercontent.com/Mealman1551/ArchivedDataCodec/main/.github/downloads.json&query=$.total_downloads&label=Total%20Downloads&color=97CA00)


Compatible with: <img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Windows_logo_-_2021.svg" alt="Windows 11" width="20"/> **&** <img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg" alt="Linux" width="20"/>

# Index / Quick Links

* [ADC Overview](#adc-archiveddatacodec)
* [Features](#features)
* [Getting Started](#getting-started)
* [Installation](#installation)

  * [Windows](#windows)
  * [Linux](#linux)
* [Usage](#usage)
* [License](#license)
* [Why ADC](#why-adc)
* [Issues](#issues)
* [Update Schedule](#update-schedule)
* [Contributing](#contributing)
* [Contact](#contact)
* [Supported Versions](#supported-versions)
* [Prepare Build environment on Windows .1](#preparing-build-environment-on-windows)
* [Prepare Build environment on Linux .1](#preparing-build-environment-on-linux)

  * [Start building on windows .2](#start-building-on-windows)
  * [Start building on Linux .2](#start-building-on-linux)

**ADC (ArchivedDataCodec)** is an open-source <img src="https://raw.githubusercontent.com/Mealman1551/ADC/362a969f45ab6f17883ec68cb6172dc4ad3ce58b/img/svg/open-source-icn.svg" alt="Open-Source" width="30"/> file extension and archiving/compression tool that uses Zlib for efficient compression and decompression of various file types. With a simple command-line interface, ADC supports both Windows and Linux, making it easy for users to archive and extract files.

ADC Archiver uses a byte-key of 8, meaning that it can create archives without limitations

For the unstable/rolling release see: [ADC Aurora](https://github.com/Mealman1551/ArchivedDataCodec/tree/ADC-Unstable)

Please note: ~~ADC can currently only pack files, folders aren't supported yet.~~ [ADC Aurora](https://github.com/Mealman1551/ArchivedDataCodec/tree/ADC-Unstable) supports this now!

Test files [here](https://github.com/The-ADC-Archiver-Project/adc-example-archive)

For container/format info go to [FORMAT.md](docs/FORMAT.md)

## Features

- **Great Compression Algorithm**: Utilizes zlib for efficient compression.
- **Cross-Platform**: Compatible with both Windows and Linux.
- **Command-Line Interface**: Simple and intuitive interface.
- **Support**: Supports a wide range of file types.

## Getting Started

### Prerequisites

***Users***
Windows

- Windows 8 or higher
  Linux
- A Modern Linux distro that has at least glibc 2.31

***Developers:***

- Python3
- zlib
- tkinter
- progress
- colorama
- cryptography
- bas64
- zipfile
- webbrowser
- urlib
- json
- ssl

## Installation

### Windows

1. Download the official installer here: [![Windows](https://custom-icon-badges.demolab.com/badge/Windows-0078D6?logo=windows11&logoColor=white)](https://github.com/Mealman1551/ArchivedDataCodec/releases/download/v1.4.4/adc1.4.4_amd64setup.exe)

### Linux

#### Tarball

Download the tarball and run `install.sh`, this will copy the files to `/opt` and make a symlink to `/usr/local/bin`.

To remove run `remove.sh` in the same tarball.

[Download tarball](https://github.com/Mealman1551/ArchivedDataCodec/releases/download/v1.4.4/adc.tar.xz)

#### Command

Dependencies:

1. Wget
2. xz-utils

Run:

```bash
mkdir -p ~/adc-temp && cd ~/adc-temp && wget -O adc.tar.xz "https://github.com/Mealman1551/ArchivedDataCodec/releases/download/v1.4.4/adc.tar.xz" && tar -xJf adc.tar.xz && sudo ./install.sh && cd ~ && rm -rf ~/adc-temp
```

to install ADC without leaving any garbage

To remove ADC you can run:

```bash
wget -O- "https://gitlab.com/adc-project/bash/-/raw/main/remove.sh" | bash
```

### ADC is installed but command `adc` doesn't work?

Run this:
```bash
sudo ln -sf /opt/adc/adc /usr/local/bin/adc && hash -r && adc
```

ADC has multiple mirrors

- [GitHub (Recommended)](https://github.com/Mealman1551/ArchivedDataCodec/releases/latest)
- [SourceForge](https://sourceforge.net/projects/adc-archiver)

### Unix (BSD, Solaris)

1. Install Python3
2. Install `requirements.txt`
3. Install python3-tk
4. Download the source code from /src
5. Run the source code in python3

## Usage

Download the program for Windows or Linux. Tarballs and setups available in the Releases tab.

## License

ADC Archiver is dual-licensed.

You may use, modify and distribute ADC Archiver under the terms of the
GNU General Public License v3 (GPLv3).

If you provide ADC Archiver as a network service, SaaS, or through a remote
or online virtual machine environment, the GNU Affero General Public License v3 (AGPLv3) applies.

See [LICENSE](LICENSE) and [LICENSE_AGPLv3](LICENSE_AGPLv3) for the full license texts.

## Why ADC

* **ADC is a purpose-built archiving format**
  No historical baggage, no legacy compromises. ADC is designed with a single, clear structure and a strict data layout.
* **Linear and predictable archive layout**
  Archives are written and read sequentially from start to end. No central directories, no backward seeks, no hidden tables.
* **Straightforward to implement in any language**
  The format is compact and explicit. A complete reader or writer can be implemented without complex or specialized libraries.
* **Full control over the archive contents**
  Each file is processed, compressed, and stored individually. There is no implicit metadata or opaque behavior.
* **Built-in modern encryption**
  Optional password protection is integrated into the format using proven cryptography, not external tooling.
* **Deterministic behavior**
  ADC behaves consistently and predictably. The same input produces the same structural output every time.
* **Tooling-first design**
  ADC is designed as a technical foundation. The CLI is an interface on top of the format, not the core of it.
* **Extensible without legacy constraints**
  The format can evolve without being locked into decades of backward-compatibility decisions.
* **Cross-platform by design**
  ADC archives behave identically across supported operating systems.
* **Fully transparent and open**
  The format is inspectable, understandable, and auditable. No black boxes, no closed specifications.
* **Built for engineers**
  ADC is focused, explicit, and controlled. It is designed for people who want to understand and own their tooling.

## Issues

Create an issue easily without the need for a GitHub account via [this form](https://docs.google.com/forms/u/0/d/e/1FAIpQLSckLmPxVy7rW30_va7YpE42GAY5UKZqD8tjQgrSGWdbfRJUvA/viewform?usp=form_confirm).

## Update Schedule

I select a date myself what is the best time, cuz i have work. Meanwhile, the rolling release Python source script [ADC Aurora](https://github.com/Mealman1551/ADC/tree/ADC-Unstable-(Aurora)) will be updated monthly, if not weekly.

#### Release flow

1. [ADC Canary](https://gitlab.com/Mealman1551/adc-canary), live updated repo, not meant to use.
2. after ADC Canary the working code will be ported to ADC Aurora asap.
3. Stable version will be based on Aurora's source code after testing the code, if there are bugs i will use a stable Aurora script.

<img src=https://raw.githubusercontent.com/Mealman1551-ADC-Project/Assets/d7a7c8b12a17b4c2ec9f6d6dbc5ce71ccda0c699/flowchart/ADC%20Release%20flow.svg width=500>

## Contributing

Contributions are welcome! See the CONTRIBUTING.md file.

## Contact

Have questions or want to learn more? Feel free to reach out via [this mail address](mailto:nathandubuy4+adc@gmail.com).

## GitLab

I have 2 ADC Repos on Gitlab, one is a continuously updated mirror of the Main branch (Stable only), and the other is the Canary repo, meant to be before Aurora.

Mirror/Main(Stable) GitLab repo of ADC: [ADC on GitLab](https://gitlab.com/Mealman1551/ADC\n)

Unstable (Aurora) is only on GitHub!

---

For Canary/continuous live development see: [ADC Canary on GitLab](https://gitlab.com/Mealman1551/adc-canary)

#### ***DO NOT USE THE CANARY REPO AS MAIN SOURCE, THIS IS LIVE DEVELOPMENT ONLY!***

---

ADC Core Utils are for OEM manufacturers or people who only want to open a `.adc` file:

[ADC-Core-Util](https://github.com/The-ADC-Archiver-Project/ADC-Core-Util)

---

### Syncing to GitLab

Syncing to GitLab is done via the [gitlab-sync.yml](https://github.com/Mealman1551/ADC/blob/main/.github/workflows/gitlab-sync.yml) file in `/.github/workflows/gitlab-sync.yml`

## Notes

If you want to support the project please consider a small donation: <a href="https://www.paypal.com/donate/?hosted_button_id=LEE83CJJ2BEJC">`
	`<img src="https://centerproject.org/wp-content/uploads/2021/11/paypal-donate-button-high-quality-png-1_orig.png" alt="Donate button" width="100"/>
  
  ---

### No macOS support

ADC Archiver does **NOT** support macOS, and it never will.
This is a deliberate decision to take a stand against the growing dominance of proprietary ecosystems and Apple’s developer restrictions.
This project supports **open platforms only**: Windows and Linux/Unix.

You can ofc run the source code but official binaries and/or setups are not compiled for macOS!

---

## Supported Versions

| Version | Release Type | Supported | EOL (End Of Life) |
| ------- | ------------ | --------- | ----------------- |
| 1.4.x   | LTS          | ✅        | 18-10-2029        |
| 1.3.x   | Regular      | ✅        | 15-05-2027        |
| 1.2.0   | Regular      | ✅        | 15-11-2026        |
| 1.1.0   | Regular      | ✅        | 15-05-2026        |
| 1.0.0   | Regular      | ❌        | 15-11-2025        |

## Build ADC

> [!Note]
> For compiling on Python 3.13 and up, a C compiler is required. On Linux, GCC is sufficient. On Windows, MSVC (cl.exe) is required via Visual Studio Build Tools 2022. Python 3.12 can compile without a C compiler using MinGW64.

Supported versions: 1.0.0, 1.1.0, 1.2.0, 1.3.1, 1.4.4. Use `make windows` or `make linux` for the latest version (1.4.4), or `x.x.x-windows` / `x.x.x-linux` for a specific version.

### Building on Windows

#### Preparing build environment on Windows

Please disable Windows Defender as it may block compilation.

##### Installing Make

Options to install GNU Make:

**Option 1 — WinGet (Recommended)**

```
winget install GnuWin32.Make
```

Add Make to PATH. [More info](https://leangaurav.medium.com/how-to-setup-install-gnu-make-on-windows-324480f1da69)

**Option 2 — Chocolatey**

```
choco install make
```

##### Downloading and extracting source code

1. Download and extract: [source_code.zip](https://github.com/Mealman1551/ArchivedDataCodec/archive/refs/tags/v1.4.4.zip)

##### Installing Python and VS Build Tools

1. Install Python 3.13.x (64-bit). Ensure pip is installed and Python is added to PATH.

```
python --version
```

2. Install Visual Studio Build Tools 2022:

```powershell
winget install Microsoft.VisualStudio.2022.BuildTools --override "--add Microsoft.VisualStudio.Workload.VCTools --includeRecommended"
```

3. Open VS Developer PowerShell:

```powershell
Import-Module "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\Common7\Tools\Microsoft.VisualStudio.DevShell.dll"
Enter-VsDevShell -VsInstallPath "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools" -DevCmdArguments "-arch=x64 -host_arch=x64"
```

Then:

```powershell
cd ArchivedDataCodec-1.4.4
```

Then:

```
make deps-windows
```

#### Start building on Windows

> [!Warning]
> Do ***NOT*** run the binary while compiling!

> [!Warning]
> Do ***NOT*** install MinGW64 if Nuitka asks for it.
> You ***CAN*** install depends.exe if Nuitka asks for it.

Compile the latest version:

```powershell
make windows
```

Or specific version:

```powershell
make 1.3.1-windows
```

Run the binary:

```powershell
cd dist
./adc.exe
```

or

```bash
./ADC_Archiver_1.3.1.exe
```

Clean build:

```powershell
make clean-windows
```

Debug build (Optional) Only use if you really need to, normally `make windows` is the best option:

```powershell
make debug-windows
```

---

### Building on Linux

#### Preparing build environment on Linux

Install dependencies:

```bash
sudo apt install build-essential pip python3-tk make patchelf ccache scons
```

Ensure Python 3.10+:

```bash
python3 --version
```

Download and extract source: [source_code.tar.gz](https://github.com/Mealman1551/ArchivedDataCodec/archive/refs/tags/v1.4.4.tar.gz)

Install additional dependencies:

```bash
make deps-linux
```

Restart or logoff to apply packages.

#### Start building on Linux

> [!Warning]
> Do ***NOT*** run the binary while compiling!

Compile latest version:

```bash
make linux
```

Or specific version:

```bash
make 1.3.1-linux
```

Run the binary:

```bash
cd dist
./adc.bin
```

or

```bash
./ADC_Archiver_1.3.1.bin
```

Clean build:

```bash
make clean-linux
```

Debug build (optional):

```bash
make debug-linux
```

#### Notes

Specific old versions can be compiled with commands like `make 1.1.0-windows` or `make 1.2.0-linux`. Version 1.0.0 is deprecated; compilation is possible but not recommended.

---

###### Made with 💚 by Mealman1551

---

###### © 2024 - 2026 Mealman1551 – The ADC Project and [contributors](contributors.txt)

###### Licensed under the GNU GPL v3.0 - ADC is Libre software.
