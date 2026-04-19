@echo off
title Leshie Compiler
echo === Leshie Compiler for ADC Canary ===

set "script_path=%~dp0..\adc.py"
set "icon_path=%~dp0..\ADCIcon.ico"

if not exist "%script_path%" (
    echo File not found: %script_path%
    pause
    exit /b 1
)

if not exist "%icon_path%" (
    echo Icon file not found: %icon_path%
    pause
    exit /b 1
)

python3 -m nuitka ^
  --onefile ^
  --enable-plugin=tk-inter ^
  --follow-imports ^
  --windows-icon-from-ico="%icon_path%" ^
  --output-dir=dist ^
  "%script_path%"

echo.
echo Builded with success in .\dist\adc.dist\
pause