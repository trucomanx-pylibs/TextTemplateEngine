#!/usr/bin/python3

import sys
sys.path.append("../src")

import text_template_engine.about as about

print(about.__package__)
print(about.__version__)
