# This is the main source code file for ADC Archiver 1.4.4.

# With great power comes great responsibility.

# ADC Archiver
# Version: 1.4.4
# byte-key: 8
# GitHub page: https://github.com/Mealman1551/ADC
# Webpage: https://mealman1551.github.io/adc.html
# Webpage 2: https://mealman1551.github.io/ADC.html

# This code is based on Aurora 2025.09.1 code and is licensed under the GNU General Public License v3.0.
# You can redistribute it and/or modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# ADC 1.4.4 is considered stable and production ready.

# ADC 1.4.4 is LTS (Long Term Support) and will receive updates for a long time.

"""
ADC Archiver 1.4.4 LTS - Main Entry Point
Command-line interface for creating and extracting archives.
"""

import os
import sys
import socket
import getpass
from colorama import init

from .constants import YELLOW, reset
from .ascii_art import print_banner, get_info_banner
from .archive import create_adc_archive, extract_adc_archive
from .ui import (
    select_files_for_archiving,
    select_directory_for_extraction,
    save_archive_file,
    open_archive_file
)
from .updater import check_and_show_update

init(autoreset=True)


def run():
    """Entry point for the application."""
    main()


# System information
dev = socket.gethostname()
name = getpass.getuser()
opr = os.sys.platform


def main():
    """
    Main function that handles command-line arguments and interactive mode.
    """
    # Print banner
    print_banner()
    
    # Check for updates
    check_and_show_update()
    
    # Auto-extract when the program is launched by double-clicking an .adc file
    if len(sys.argv) > 1:
        first_arg = sys.argv[1]
        if os.path.isfile(first_arg) and first_arg.lower().endswith(".adc"):
            output_dir = os.path.dirname(os.path.abspath(first_arg))
            print(f"{YELLOW}Auto-extracting {first_arg} to {output_dir}{reset}")
            extract_adc_archive(first_arg, output_dir)
            return

    # Handle command-line subcommands
    if len(sys.argv) > 1:
        subcommand = sys.argv[1]
        if subcommand == "c":
            if len(sys.argv) < 4:
                print("Use: adc.exe or adc c <files...> <output.adc>")
                return
            files = sys.argv[2:-1]
            output = sys.argv[-1]
            create_adc_archive(files, output)
            return
        elif subcommand == "e":
            if len(sys.argv) < 3:
                print("Use: adc.exe or adc e <archive.adc> [output_folder]")
                return
            archive = sys.argv[2]
            folder = sys.argv[3] if len(sys.argv) >= 4 else os.getcwd()
            extract_adc_archive(archive, folder)
            return
        else:
            print("Unknown command.")
            print(
                "Use:\n  adc.exe or adc c <files...> <output.adc>\n  adc.exe or adc e <archive.adc> [output_folder]"
            )
            return

    # Interactive mode
    while True:
        command = (
            input(
                f"Welcome to the ADC Archiver! Enter command ('c' to create, 'e' to extract, 'i' for info, 'q' to quit): "
            )
            .strip()
            .lower()
        )
        
        if command in ("c", "create"):
            files_to_archive = select_files_for_archiving()
            if files_to_archive:
                fmt = input("Choose format: [1] ADC (default), [2] ZIP: ").strip()
                fmt = "zip" if fmt == "2" else "adc"

                output_archive = save_archive_file(format=fmt)
                if output_archive:
                    create_adc_archive(files_to_archive, output_archive, format=fmt)
                else:
                    print("No output file specified. Aborting.")
            else:
                print("No files selected. Aborting.")

        elif command in ("e", "extract"):
            archive_to_extract = open_archive_file()
            if archive_to_extract:
                extraction_directory = select_directory_for_extraction()
                if extraction_directory:
                    extract_adc_archive(archive_to_extract, extraction_directory)
                else:
                    print("No output directory specified. Aborting.")
            else:
                print("No archive selected. Aborting.")

        elif command == "i":
            info = get_info_banner(dev, name, opr)
            print(info)

        elif command in ("q", "exit", "quit"):
            print(f"Thank you for using ADC Archiver!")
            break

        else:
            print(
                "Invalid command. Please type 'c' to create, 'e' to extract, 'i' for info or 'q' to quit."
            )


if __name__ == "__main__":
    run()
