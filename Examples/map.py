import webbrowser, sys, pyperclip

sys.argv # ['map.py', '870', 'Valencia', 'St.']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # ['map.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# http://www.google.com/maps/place/<ADDRESS>
webbrowser.open('http://www.google.com/maps/place/' + address)
