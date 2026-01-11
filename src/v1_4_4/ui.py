# ADC Archiver 1.4.4 LTS - UI Module
# This code is licensed under the GNU General Public License v3.0.

"""
User interface functions using tkinter for file dialogs.
"""

import tkinter as tk
from tkinter import filedialog


def select_files_for_archiving():
    """
    Opens file selection dialog for archiving.
    
    Returns:
        List of file paths selected by the user
    """
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    files = filedialog.askopenfilenames(title="Select files to archive")
    root.destroy()
    return list(files)


def select_directory_for_extraction():
    """
    Opens a directory selection dialog for extraction destination.
    
    Returns:
        Directory path selected by the user
    """
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    folder = filedialog.askdirectory(title="Select directory to extract files to")
    root.destroy()
    return folder


def save_archive_file(format="adc"):
    """
    Opens a save file dialog for creating an archive.
    
    Args:
        format: Archive format (adc or zip)
        
    Returns:
        File path where the archive should be saved
    """
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    default_ext = ".zip" if format == "zip" else ".adc"
    file_path = filedialog.asksaveasfilename(
        defaultextension=default_ext,
        filetypes=(
            [("ADC archives", "*.adc")]
            if format == "adc"
            else [("ZIP archives", "*.zip")]
        ),
        title="Save archive as",
    )
    root.destroy()
    return file_path


def open_archive_file():
    """
    Opens a file selection dialog for selecting an ADC archive to extract.
    
    Returns:
        File path of the selected archive
    """
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    file_path = filedialog.askopenfilename(
        filetypes=[("ADC archives", "*.adc")], title="Select ADC archive to extract"
    )
    root.destroy()
    return file_path
