import os
import sys
import ctypes
import shutil
import traceback


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


def elevate():
    params = " ".join(['"%s"' % a for a in sys.argv])
    try:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, params, None, 1
        )
        return True
    except Exception:
        return False


def copy_dist_to_dst(src, dst):
    if not os.path.exists(src):
        raise FileNotFoundError("dist folder not found. Build first.")
    os.makedirs(dst, exist_ok=True)
    for entry in os.listdir(src):
        s = os.path.join(src, entry)
        d = os.path.join(dst, entry)
        if os.path.isdir(s):
            try:
                shutil.copytree(s, d, dirs_exist_ok=True)
            except TypeError:
                # older python versions: copy tree manually
                if not os.path.exists(d):
                    os.makedirs(d)
                for root, dirs, files in os.walk(s):
                    rel = os.path.relpath(root, s)
                    dest_root = os.path.join(d, rel) if rel != "." else d
                    os.makedirs(dest_root, exist_ok=True)
                    for f in files:
                        shutil.copy2(os.path.join(root, f), os.path.join(dest_root, f))
        else:
            shutil.copy2(s, d)


def find_first_exe(dst):
    for root, dirs, files in os.walk(dst):
        for f in files:
            if f.lower().endswith(".exe"):
                return os.path.join(root, f)
    return None


def create_shortcut_lnk(target, link_path, icon=None, workdir=None):
    try:
        import win32com.client

        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortcut(link_path)
        shortcut.TargetPath = target
        if workdir:
            shortcut.WorkingDirectory = workdir
        if icon and os.path.exists(icon):
            shortcut.IconLocation = icon
        shortcut.Save()
        return True
    except Exception:
        return False


def create_shortcut_url(target, link_path, icon=None):
    # .url file (works without pywin32)
    try:
        with open(link_path, "w", encoding="utf-8") as f:
            f.write("[InternetShortcut]\n")
            f.write("URL=file:///%s\n" % target.replace("\\", "/"))
            if icon and os.path.exists(icon):
                f.write("IconFile=%s\n" % icon)
                f.write("IconIndex=0\n")
        return True
    except Exception:
        return False


def main():
    try:
        if not is_admin():
            ok = elevate()
            if not ok:
                print("Elevation failed or cancelled.")
                sys.exit(1)
            # elevated process started, exit current
            sys.exit(0)

        cwd = os.path.abspath(os.getcwd())
        src = os.path.join(cwd, "dist")
        dst = os.path.join(
            os.environ.get("ProgramFiles", "C:\\Program Files"), "ADC Archiver"
        )

        copy_dist_to_dst(src, dst)

        exe = find_first_exe(dst)
        if exe:
            target_exe = os.path.join(dst, "ADC Archiver.exe")
            shutil.copy2(exe, target_exe)

        desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
        programs = os.path.join(
            os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs"
        )
        start_folder = os.path.join(programs, "ADC Archiver")
        os.makedirs(start_folder, exist_ok=True)

        icon = os.path.join(dst, "ADCIcon.ico")
        target_exe_path = os.path.join(dst, "ADC Archiver.exe") if exe else None

        if target_exe_path:
            lnk_desktop = os.path.join(desktop, "ADC Archiver.lnk")
            if not create_shortcut_lnk(
                target_exe_path, lnk_desktop, icon=icon, workdir=dst
            ):
                # fallback to .url
                create_shortcut_url(
                    target_exe_path,
                    os.path.join(desktop, "ADC Archiver.url"),
                    icon="/ADCIcon.ico",
                )

            lnk_start = os.path.join(start_folder, "ADC Archiver.lnk")
            if not create_shortcut_lnk(
                target_exe_path, lnk_start, icon=icon, workdir=dst
            ):
                create_shortcut_url(
                    target_exe_path,
                    os.path.join(start_folder, "ADC Archiver.url"),
                    icon=icon,
                )

        print("Installation complete.")
    except Exception:
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
