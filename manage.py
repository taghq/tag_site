#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    try:
    	from environment import *
    except ImportError:
        ENVIRONMENT = "tag_site.settings.local"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", ENVIRONMENT)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
