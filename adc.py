#!/usr/bin/env python3

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from adc.__main__ import run

if __name__ == "__main__":
    run()