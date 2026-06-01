import os
import sys

import text_template_engine.about as about
from text_template_engine.modules.wabout import show_about


# ----------------------------------------------------------
# Main CLI
# ----------------------------------------------------------

def main():
    show_about()


if __name__ == "__main__":
    main()

