NAME=ADC_Archiver_1.4.3
SRC=src/ADC_Archiver_1.4.3.py

linux:
	python3 -m nuitka --standalone --onefile --enable-plugin=tk-inter --output-dir=dist $(SRC)

windows:
	python -m nuitka --standalone --onefile --enable-plugin=tk-inter  --windows-icon-from-ico=ADCIcon.ico --output-dir=dist $(SRC)

deps-linux:
	pip install -r requirements.txt --break-system-packages
	pip install nuitka scons --break-system-packages

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
	python -m nuitka --standalone --onefile --enable-plugin=tk-inter  --windows-icon-from-ico=ADCIcon.ico --output-dir=dist src/ADC_Archiver_1.3.1.py

1.3.1-linux:
	python3 -m nuitka --standalone --onefile --enable-plugin=tk-inter --output-dir=dist src/ADC_Archiver_1.3.1.py

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
	@echo "Installing ADC Archiver to /opt/adc..."
	sudo mkdir -p /opt/adc
	sudo cp -r dist/* /opt/adc/
	sudo find /opt/adc -type f -executable -exec mv {} /opt/adc/adc \;
	sudo chmod +x /opt/adc/adc
	sudo ln -sf /opt/adc/adc /usr/local/bin/adc
	@echo "ADC Archiver installed successfully!"
	@echo "You can now run 'adc' from anywhere in the terminal"

remove:
	@echo "Removing ADC Archiver from /opt/adc..."
	sudo rm -rf /opt/adc
	sudo rm -f /usr/local/bin/adc
	@echo "ADC Archiver removed successfully!"