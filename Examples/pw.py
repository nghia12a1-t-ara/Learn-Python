#! python3

passwords = { 'mailhust' : 'nghia12a1', \
              'facebook' : 'Taarabt1012a', \
              'fpt' : 'Taarabt1012ab', \
              'tpbank' : 'Nghia12a1', \
              'blog' : 'ABCXYA', \
              'tpbank' : '04193958001\nTPBank\nNGUYEN VAN NGHIA', \
              'vietin' : '103002848083\nVietin Bank\nNGUYEN VAN NGHIA', \
              'elsa' : 'nghia12a1' }
import sys, pyperclip
if len(sys.argv) < 2 :
    print('Usage : Python pw.py[account] - copy account password')
    sys.exit()
account = sys.argv[1] # first command line arg is the account name
if account.lower() in passwords:
    pyperclip.copy(passwords[account.lower()])
    print('password for ' + account.upper() + ' copied to clipboard')
else:
    print('None')
