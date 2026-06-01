#!/usr/bin/python3

import sys
sys.path.append("../src")

from text_template_engine.renderer import render_file

render_file(
    template_path="email.txt",
    output_path="output/email.txt",
    variables={
        "NAME": "John Doe",
        "EMAIL": "john@example.com",
        "COMPANY": "Acme Inc."
    }
)
