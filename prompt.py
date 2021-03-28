#!/usr/bin/python3

from blankcryptLib import crypt

mode = input('Encrypt or Decrypt? (E/D): ')
fname = input('File to crypt: ')
pw1 = input('Password: ')

f = open(fname, 'r', encoding='utf-8')
text = f.read()
f.close()

result = crypt(mode, text, pw1)

f = open('%s.%s.txt' % (fname, mode), 'w', encoding='utf-8')
f.write(result)
f.close()

print('Done')

exit(0)
