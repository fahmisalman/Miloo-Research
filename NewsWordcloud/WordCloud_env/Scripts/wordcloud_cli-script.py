#!d:\milo\wordcloud\miloo-research\newswordcloud\wordcloud_env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'wordcloud==1.5.0','console_scripts','wordcloud_cli'
__requires__ = 'wordcloud==1.5.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('wordcloud==1.5.0', 'console_scripts', 'wordcloud_cli')()
    )
