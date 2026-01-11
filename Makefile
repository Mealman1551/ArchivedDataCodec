NAME=ADC_Archiver_1.4.4
SRC=adc.py
INSTALL_DIR=/opt/adc
BINARY_NAME=adc
DESKTOP_FILE=adc-archiver.desktop
MIME_FILE=adc.xml
WRAPPER_SCRIPT=invterm.sh

linux:
	python3 -m nuitka --standalone --onefile --enable-plugin=tk-inter --output-dir=dist $(SRC)

windows:
	python -m nuitka --standalone --onefile --enable-plugin=tk-inter  --windows-icon-from-ico=ADCIcon.ico --output-dir=dist $(SRC)

deps-linux:
	pip install -r requirements.txt --break-system-packages
	pip install nuitka scons --break-system-packages
	sudo apt install python3-tk

deps-windows:
	python -m pip install -r requirements.txt
	python -m pip install nuitka scons

debug-linux:
	python3 -m nuitka --debug --onefile --standalone --enable-plugin=tk-inter --output-dir=dist $(SRC)

debug-windows:
	python -m nuitka --debug --onefile --standalone --enable-plugin=tk-inter  --windows-icon-from-ico=ADCIcon.ico --output-dir=dist $(SRC)

clean-windows:
	del /Q dist\*

clean-linux:
	rm -rf dist/*

1.3.1-windows:
	python -m nuitka --standalone --onefile --enable-plugin=tk-inter  --windows-icon-from-ico=ADCIcon.ico --output-dir=dist src/v1_3_1/ADC_Archiver_1.3.1.py

1.3.1-linux:
	python3 -m nuitka --standalone --onefile --enable-plugin=tk-inter --output-dir=dist src/v1_3_1/ADC_Archiver_1.3.1.py

1.2.0-windows:
	python -m nuitka --standalone --onefile --enable-plugin=tk-inter  --windows-icon-from-ico=ADCIcon.ico --output-dir=dist src/older/1.2.0/ADC_Archiver_1.2.0.py

1.2.0-linux:
	python3 -m nuitka --standalone --onefile --enable-plugin=tk-inter --output-dir=dist src/older/1.2.0/ADC_Archiver_1.2.0_Linux.py

1.1.0-windows:
	python -m nuitka --standalone --onefile --enable-plugin=tk-inter  --windows-icon-from-ico=ADCIcon.ico --output-dir=dist "src/older/1.1.0/ADC Archiver 1.1.0 Source-Code.py"

1.1.0-linux:
	python3 -m nuitka --standalone --onefile --enable-plugin=tk-inter --output-dir=dist "src/older/1.1.0/ADC Archiver 1.1.0 Source-Code.py"

1.0.0-windows:
	@echo This version is deprecated, please use at least 1.1.0
	python -m nuitka --standalone --onefile --enable-plugin=tk-inter  --windows-icon-from-ico=ADCIcon.ico --output-dir=dist src/older/1.0.0/src1.0.0.py

1.0.0-linux:
	@echo This version is deprecated, please use at least 1.1.0
	python3 -m nuitka --standalone --onefile --enable-plugin=tk-inter --output-dir=dist src/older/1.0.0/src1.0.0.py

install:
	@echo "Installing ADC Archiver to $(INSTALL_DIR)..."
	@if [ ! -f "dist/$(SRC:.py=.bin)" ]; then \
		echo "Error: Binary not found. Please run 'make linux' first to build the application."; \
		exit 1; \
	fi
	@set -e; \
	sudo mkdir -p "$(INSTALL_DIR)"; \
	sudo cp "dist/$(SRC:.py=.bin)" "$(INSTALL_DIR)/$(BINARY_NAME)"; \
	sudo chmod +x "$(INSTALL_DIR)/$(BINARY_NAME)"; \
	echo '#!/bin/bash' | sudo tee "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo 'TERMINAL=""' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo 'if command -v gnome-terminal >/dev/null 2>&1; then' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo '    TERMINAL="gnome-terminal --"' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo 'elif command -v xfce4-terminal >/dev/null 2>&1; then' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo '    TERMINAL="xfce4-terminal -x"' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo 'elif command -v mate-terminal >/dev/null 2>&1; then' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo '    TERMINAL="mate-terminal -x"' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo 'elif command -v konsole >/dev/null 2>&1; then' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo '    TERMINAL="konsole -e"' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo 'elif command -v xterm >/dev/null 2>&1; then' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo '    TERMINAL="xterm -e"' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo 'else' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo '    echo "No terminal emulator found. Please install gnome-terminal, xfce4-terminal, mate-terminal or xterm."' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo '    exit 1' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo 'fi' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	echo 'exec $$TERMINAL $(INSTALL_DIR)/$(BINARY_NAME) "$$@"' | sudo tee -a "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)" > /dev/null; \
	sudo chmod +x "$(INSTALL_DIR)/$(WRAPPER_SCRIPT)"; \
	sudo ln -sf "$(INSTALL_DIR)/$(BINARY_NAME)" "/usr/local/bin/$(BINARY_NAME)"; \
	echo "[Desktop Entry]" | sudo tee "/usr/share/applications/$(DESKTOP_FILE)" > /dev/null; \
	echo "Name=ADC Archiver" | sudo tee -a "/usr/share/applications/$(DESKTOP_FILE)" > /dev/null; \
	echo "Comment=Extract ADC archives" | sudo tee -a "/usr/share/applications/$(DESKTOP_FILE)" > /dev/null; \
	echo "Exec=$(INSTALL_DIR)/$(WRAPPER_SCRIPT) %f" | sudo tee -a "/usr/share/applications/$(DESKTOP_FILE)" > /dev/null; \
	echo "Terminal=false" | sudo tee -a "/usr/share/applications/$(DESKTOP_FILE)" > /dev/null; \
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
	sudo update-mime-database /usr/share/mime; \
	sudo update-desktop-database /usr/share/applications; \
	xdg-mime default "$(DESKTOP_FILE)" application/x-adc-archive; \
	if command -v caja >/dev/null 2>&1; then \
		caja -q; \
	elif command -v nautilus >/dev/null 2>&1; then \
		nautilus -q; \
	fi; \
	echo "Installation complete! You can now use 'adc' from anywhere or right-click .adc files."

build-and-install: linux install

remove:
	@echo "Removing ADC Archiver from $(INSTALL_DIR)..."
	sudo rm -rf $(INSTALL_DIR)
	sudo rm -f /usr/local/bin/$(BINARY_NAME)
	sudo rm -f /usr/share/applications/$(DESKTOP_FILE)
	sudo rm -f /usr/share/mime/packages/$(MIME_FILE)
	sudo update-mime-database /usr/share/mime
	sudo update-desktop-database /usr/share/applications
	@echo "ADC Archiver removed successfully!"
