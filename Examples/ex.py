import os

os.chdir('D:\\Python\\Examples')

for filename in os.listdir():
    if filename.endswith('.bat'):
        print(filename)
