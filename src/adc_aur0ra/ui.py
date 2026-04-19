# ADC Archiver Aurora UI Module
# (c) 2026 Mealman1551

import tkinter as tk
from tkinter import filedialog


def select_files_for_archiving():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    files = filedialog.askopenfilenames(title="Select files to archive")
    all_paths = list(files)

    while True:
        print("\n[INFO] You can now select folders to include (Cancel to finish).")
        folder = filedialog.askdirectory(
            title="Select additional directory to include (Cancel to finish)"
        )
        if not folder:
            break
        all_paths.append(folder)

    root.destroy()
    return all_paths


def select_directory_for_extraction():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    folder = filedialog.askdirectory(title="Select directory to extract files to")
    root.destroy()
    return folder


def save_archive_file(format="adc"):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    extensions = {
        "adc": (".adc", [("ADC archives", "*.adc")]),
        "zip": (".zip", [("ZIP archives", "*.zip")]),
        "tar": (".tar", [("TAR archives", "*.tar")]),
        "tar.gz": (".tar.gz", [("TAR.GZ archives", "*.tar.gz")]),
        "tar.xz": (".tar.xz", [("TAR.XZ archives", "*.tar.xz")]),
        "tar.bz2": (".tar.bz2", [("TAR.BZ2 archives", "*.tar.bz2")]),
        "7z": (".7z", [("7ZIP archives", "*.7z")]),
    }

    default_ext, filetypes = extensions.get(
        format, (".adc", [("ADC archives", "*.adc")])
    )
    file_path = filedialog.asksaveasfilename(
        defaultextension=default_ext,
        filetypes=filetypes,
        title="Save archive as",
    )
    root.destroy()
    return file_path


def open_archive_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    filetypes = [
        ("ADC archives", "*.adc"),
        ("ZIP archives", "*.zip"),
        ("7ZIP archives", "*.7z"),
        ("TAR archives", "*.tar"),
        ("TAR.GZ archives", "*.tar.gz"),
        ("TAR.XZ archives", "*.tar.xz"),
        ("TAR.BZ2 archives", "*.tar.bz2"),
        ("All files", "*.*"),
    ]

    file_path = filedialog.askopenfilename(
        filetypes=filetypes,
        title="Select archive to extract",
    )
    root.destroy()
    return file_path
