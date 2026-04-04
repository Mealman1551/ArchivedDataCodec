# ADC Archiver 1.4.5 LTS - Updater Module
# This code is licensed under the GNU General Public License v3.0.


import urllib.request
import json
import ssl
import tkinter as tk
import webbrowser

from .constants import UPDATE_JSON_URL, UPDATE_CHECK_TIMEOUT, VERSION

ssl._create_default_https_context = ssl._create_unverified_context


def show_update_banner(title, body, url, severity="info"):

    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    root.title(title)
    root.deiconify()
    root.geometry("360x160")
    root.resizable(False, False)

    frame = tk.Frame(root, padx=15, pady=15)
    frame.pack(expand=True, fill="both")

    label_title = tk.Label(frame, text=title, font=("Segoe UI", 12, "bold"))
    label_title.pack(anchor="w")

    label_body = tk.Label(frame, text=body, wraplength=320, justify="left")
    label_body.pack(anchor="w", pady=(8, 15))

    def open_link():
        webbrowser.open(url)
        root.destroy()

    tk.Button(frame, text="Download update", command=open_link).pack(side="left")
    tk.Button(frame, text="Close", command=root.destroy).pack(side="right")

    root.mainloop()


def _version_tuple(v):

    parts = [p for p in v.split(".")]
    nums = []
    for p in parts:
        try:
            nums.append(int(p))
        except:
            nums.append(0)
    while len(nums) < 3:
        nums.append(0)
    return tuple(nums)


def _is_newer(remote, local):

    try:
        return _version_tuple(remote) > _version_tuple(local)
    except:
        return False


def fetch_update_json(url, timeout=UPDATE_CHECK_TIMEOUT):

    req = urllib.request.Request(url, headers={"User-Agent": "ADC-Update-Checker/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read()
    return json.loads(raw.decode("utf-8"))


def check_and_show_update(url=UPDATE_JSON_URL, local_version=VERSION):

    try:
        data = fetch_update_json(url)
    except Exception as e:
        print(f"Failed to fetch update info: {e}")
        return

    remote = data.get("current_release") or data.get("version") or ""
    if not remote:
        return

    if not _is_newer(remote, local_version):
        return

    banner = data.get("banner", {})
    title = banner.get("title", f"Update available: {remote}")
    body = banner.get("body", "")
    severity = (banner.get("severity") or "info").lower()

    print(f"\n=== UPDATE {remote} ===\n{title}\n{body}\n====================\n")

    root = None
    try:
        show_update_banner(
            title,
            body,
            banner.get("url", "https://mealman1551.github.io/adc.html#downloads"),
            severity,
        )
    except Exception as gui_error:
        print(f"Failed to show update popup: {gui_error}")
    finally:
        if root:
            try:
                root.destroy()
            except:
                pass
