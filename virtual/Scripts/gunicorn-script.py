#!c:\users\vk\mlpython\udemy\webapp\virtual\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'gunicorn==20.0.4','console_scripts','gunicorn'
__requires__ = 'gunicorn==20.0.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('gunicorn==20.0.4', 'console_scripts', 'gunicorn')()
    )
