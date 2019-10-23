#! python3.7
# argumentOrClipboard - Getting arguments from command line or clipboard

import sys, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
