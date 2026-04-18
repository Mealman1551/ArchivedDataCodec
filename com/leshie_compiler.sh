#!/bin/bash

echo "=== Leshie Compiler for ADC Canary ==="

script_path="$(dirname "$0")/../adc.py"

if [[ ! -f "$script_path" ]]; then
    echo "File not found: $script_path"
    exit 1
fi

nuitka \
  --standalone \
  --enable-plugin=tk-inter \
  --follow-imports \
  --output-dir=dist \
  "$script_path"

echo "Builded with success in ./dist/adc.dist/"
read -p "Press a key to close..." -n1 -s

