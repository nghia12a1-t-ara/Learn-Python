@py D:\Python\Examples\cmd.py %*
@pause

passwords = { 'email' : 'Nghia12a1', \
              'Facebook' : 'Nhungchos', \
              'Blog' : 'ABCXYA' }
import sys, pyperclip
if len(sys.argv) < 2 :
    print('Usage : Python pw.py[account] - copy account password')
    sys.exit()
account = sys.argv[1] # first command line arg is the account name
if account in passwords:
    pyperclip.copy(passwords[account])
    print('password for' + account + 'copied to clipboard')
else:
    print('None')
