#!/usr/bin/python3

#pip install text_template_engine
#OR
#import sys
#sys.path.append("../src")

from text_template_engine.renderer import render_file

###################

render_file(
    template_path="email.txt",
    output_path="output/email.txt",
    variables={
        "NAME": "John Doe",
        "EMAIL": "john@example.com",
        "COMPANY": "Acme Inc."
    }
)

###################

in_str="""
Hello {{NAME}}, Welcome to {{COMPANY}}!!!! Your institutional email address is: {{EMAIL}}
Best regards,
Support Team
"""

out_str=render_string(  in_str, 
                        variables={ "NAME": "John Doe",
                                    "EMAIL": "john@example.com",
                                    "COMPANY": "Acme Inc."} 
                     )
print(out_str)

###################
# render_directory(template_dir, output_dir, variables, filter=[".html", ".txt", ".md"])
