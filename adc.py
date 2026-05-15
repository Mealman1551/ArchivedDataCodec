#!/usr/bin/env python3
# ADC Archiver - Launcher
# This code is licensed under the GNU General Public License v3.0.

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

if __name__ == "__main__":
    from adc.__main__ import run

    run()
