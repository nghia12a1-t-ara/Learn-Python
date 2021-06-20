# copy string need be modified and run code

import pyperclip
texts = pyperclip.paste()
texts = texts.split('-\t')

for i in range(len(texts)):
    if texts[i] != '':
        texts[i] = '***\t' + texts[i]

texts = ''.join(texts)

pyperclip.copy(texts)

print('DONE!')
