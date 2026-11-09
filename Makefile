NAME=ADC_Archiver_1.4.5
SRC=adc.py
INSTALL_DIR=/opt/adc
BINARY_NAME=adc
DESKTOP_FILE=adc-archiver.desktop
MIME_FILE=adc.xml
WRAPPER_SCRIPT=invterm.sh

linux:
	PYTHONPATH=src python3 -m nuitka --standalone --onefile --enable-plugin=tk-inter --include-package=adc --output-dir=dist $(SRC)

windows:
	set PYTHONPATH=src && python -m nuitka --standalone --onefile --enable-plugin=tk-inter --include-package=adc --windows-icon-from-ico=assets/ADCIcon.ico --output-dir=dist $(SRC)

deps-linux:
	pip install -r requirements.txt --break-system-packages
	pip install nuitka scons --break-system-packages
	@set -eu; \
	if [ ! -r /etc/os-release ]; then \
		echo "Error: cannot identify this Linux distribution (/etc/os-release is missing)." >&2; \
		exit 1; \
	fi; \
	. /etc/os-release; \
	ID_LIKE=$${ID_LIKE:-}; \
	case " $$ID $$ID_LIKE " in \
		*" debian "*|*" ubuntu "*|*" linuxmint "*|*" pop "*|*" elementary "*|*" kali "*) \
			if ! command -v apt-get >/dev/null 2>&1; then \
				echo "Error: this Debian-based distribution requires apt-get to install python3-tk." >&2; \
				exit 1; \
			fi; \
			sudo apt-get install -y python3-tk ;; \
		*" fedora "*|*" rhel "*|*" centos "*|*" rocky "*|*" almalinux "*) \
			if command -v dnf >/dev/null 2>&1; then \
				sudo dnf install -y python3-tkinter; \
			elif command -v yum >/dev/null 2>&1; then \
				sudo yum install -y python3-tkinter; \
			else \
				echo "Error: this Fedora/RHEL-based distribution requires dnf or yum to install python3-tkinter." >&2; \
				exit 1; \
			fi ;; \
		*" arch "*|*" manjaro "*|*" endeavouros "*) \
			if ! command -v pacman >/dev/null 2>&1; then \
				echo "Error: this Arch-based distribution requires pacman to install tk." >&2; \
				exit 1; \
			fi; \
			sudo pacman -S --needed --noconfirm tk ;; \
		*" opensuse "*|*" suse "*) \
			if ! command -v zypper >/dev/null 2>&1; then \
				echo "Error: this SUSE-based distribution requires zypper to install python3-tk." >&2; \
				exit 1; \
			fi; \
			sudo zypper --non-interactive install python3-tk ;; \
		*" alpine "*) \
			if ! command -v apk >/dev/null 2>&1; then \
				echo "Error: Alpine Linux requires apk to install py3-tkinter." >&2; \
				exit 1; \
			fi; \
			sudo apk add py3-tkinter ;; \
		*) \
			echo "Error: unsupported Linux distribution '$$ID' (ID_LIKE='$$ID_LIKE'). Install its Tkinter package manually." >&2; \
			exit 1 ;; \
	esac

deps-windows:
	python -m pip install -r requirements.txt
	python -m pip install nuitka scons

debug-linux:
	PYTHONPATH=src python3 -m nuitka --debug --onefile --standalone --enable-plugin=tk-inter --include-package=adc --output-dir=dist $(SRC)

debug-windows:
	set PYTHONPATH=src && python -m nuitka --debug --onefile --standalone --enable-plugin=tk-inter --include-package=adc --windows-icon-from-ico=ADCIcon.ico --output-dir=dist $(SRC)

clean-windows:
	del /Q dist\*

clean-linux:
	rm -rf dist/*

install:
	@echo "Installing ADC Archiver to $(INSTALL_DIR)..."
	@if [ ! -f "dist/$(BINARY_NAME).bin" ]; then \
		echo "Error: Binary not found. Run 'make linux' first."; \
		exit 1; \
	fi
	@set -e; \
	sudo mkdir -p "$(INSTALL_DIR)"; \
	sudo cp "dist/$(BINARY_NAME).bin" "$(INSTALL_DIR)/$(BINARY_NAME)"; \
	sudo chmod +x "$(INSTALL_DIR)/$(BINARY_NAME)"; \
	echo '#!/bin/bash' | sudo tee "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo 'ADC="/opt/adc/adc"' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo 'exec "$$ADC" "$$@"' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	sudo chmod +x "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)"; \
	sudo ln -sf "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" "/usr/local/bin/$(BINARY_NAME)"; \
	echo "[Desktop Entry]" | sudo tee "/usr/share/applications/$(DESKTOP_FILE)" > /dev/null; \
	echo "Name=ADC Archiver" | sudo tee -a "/usr/share/applications/$(DESKTOP_FILE)" > /dev/null; \
	echo "Comment=Extract ADC archives" | sudo tee -a "/usr/share/applications/$(DESKTOP_FILE)" > /dev/null; \
	echo "Exec=$(INSTALL_DIR)/$(WRAPPER_SCRIPT) %f" | sudo tee -a "/usr/share/applications/$(DESKTOP_FILE)" > /dev/null; \
	echo "Terminal=true" | sudo tee -a "/usr/share/applications/$(DESKTOP_FILE)" > /dev/null; \
	echo "Type=Application" | sudo tee -a "/usr/share/applications/$(DESKTOP_FILE)" > /dev/null; \
	echo "MimeType=application/x-adc-archive;" | sudo tee -a "/usr/share/applications/$(DESKTOP_FILE)" > /dev/null; \
	echo "NoDisplay=true" | sudo tee -a "/usr/share/applications/$(DESKTOP_FILE)" > /dev/null; \
	echo "Categories=Utility;" | sudo tee -a "/usr/share/applications/$(DESKTOP_FILE)" > /dev/null; \
	echo '<?xml version="1.0" encoding="UTF-8"?>' | sudo tee "/usr/share/mime/packages/$(MIME_FILE)" > /dev/null; \
	echo '<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">' | sudo tee -a "/usr/share/mime/packages/$(MIME_FILE)" > /dev/null; \
	echo '    <mime-type type="application/x-adc-archive">' | sudo tee -a "/usr/share/mime/packages/$(MIME_FILE)" > /dev/null; \
	echo '        <comment>ADC Archive</comment>' | sudo tee -a "/usr/share/mime/packages/$(MIME_FILE)" > /dev/null; \
	echo '        <glob pattern="*.adc"/>' | sudo tee -a "/usr/share/mime/packages/$(MIME_FILE)" > /dev/null; \
	echo '    </mime-type>' | sudo tee -a "/usr/share/mime/packages/$(MIME_FILE)" > /dev/null; \
	echo '</mime-info>' | sudo tee -a "/usr/share/mime/packages/$(MIME_FILE)" > /dev/null; \
	command -v update-mime-database >/dev/null && sudo update-mime-database /usr/share/mime || true; \
	command -v update-desktop-database >/dev/null && sudo update-desktop-database /usr/share/applications || true; \
	xdg-mime default "$(DESKTOP_FILE)" application/x-adc-archive || true; \
	if command -v caja >/dev/null 2>&1; then caja -q; elif command -v nautilus >/dev/null 2>&1; then nautilus -q; fi; \
	echo "Installation complete! You can now use 'adc' from anywhere or right-click .adc files."

build-and-install: linux install

remove:
	@echo "Removing ADC Archiver..."
	sudo rm -rf $(INSTALL_DIR)
	sudo rm -f /usr/local/bin/$(BINARY_NAME)
	sudo rm -f /usr/share/applications/$(DESKTOP_FILE)
	sudo rm -f /usr/share/mime/packages/$(MIME_FILE)
	command -v update-mime-database >/dev/null && sudo update-mime-database /usr/share/mime || true
	command -v update-desktop-database >/dev/null && sudo update-desktop-database /usr/share/applications || true
	@echo "Removed successfully!"