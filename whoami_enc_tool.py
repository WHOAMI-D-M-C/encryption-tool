#CODED BY - WHOAMI-XD-KING :)
#FOR ENCRYPT YOUR TOOL
#CONATCT ME ON FACEBOOK (RAJ KHAN)
#LEGENDS NEVER DIE :)
import base64
import zlib
import marshal
import os
os.system('clear')
password = 'KING'
print('\033[0;91m   ███████████████  \n██████████████ \n████████████████████████  \n█████   ██ ██   ██████   ██ \n██   ██ ██   ██ ██████  ██ ██   ██\n \033[0;94m────────────────────────────────────────────────────────\n\033[0;92mAuthor     \033[0;91mWHOAMI-XD THE SCRIPT F**KER\n\033[0;92mYOUTUBE    \033[0;96m(😈😈)\n\033[0;92mFACEBOOK   \033[0;94mRaj Khan\n\033[0;94m────────────────────────────────────────────────────────')
p = input('\x1b[91m Enter Password > ')
os.system('xdg-open https://youtube.com/channel/UChKjimPjldJkkq-w ')

x1 = ' '
print(x1[::-1])
print('\033[0;91m██   ██  █████  ██████  ██ ██████  \n██  ██  ██   ██ ██   ██ ██ ██   ██ \n█████   ███████ ██████  ██ ██████  \n██  ██  ██   ██ ██   ███ ██   ██ \n██   ██ ██   ██ ██████  ██ ██   ██\n \033[0;94m────────────────────────────────────────────────────────\n\033[0;92mAuthor     \033[0;91mWHOAMI-XD THE SCRIPT F**KER\n\033[0;92mYOUTUBE    \033[0;96m(😈😈)\n\033[0;92mFACEBOOK   \033[0;94mRaj Khan\n\033[0;94m────────────────────────────────────────────────────────')
os.system('xdg-open https://www.facebook.com/Raj Khan ')
file = input('\x1b[91m  Enter The File > ')
if file == '':
    os.system('clear')
    print('Error: Could not open the file\n\n')
out = file.replace('.py', '') + '-enc.py'
file = open(file).read()
cc = compile(file, '<X>', 'exec')
dn = marshal.dumps(cc)
z = zlib.compress(dn)
b = base64.b64encode(z)
m = marshal.dumps(b)
b2 = base64.b64encode(m)
m2 = marshal.dumps(b2)
b3 = base64.b64encode(m2)
m3 = marshal.dumps(b3)
b4 = base64.b64encode(m3)
m4 = marshal.dumps(b4)
b5 = base64.b64encode(m4)
m5 = marshal.dumps(b5)
b6 = base64.b64encode(m5)
m6 = marshal.dumps(b6)
b7 = base64.b64encode(m6)
m7 = marshal.dumps(b7)
b8 = base64.b85encode(m7)
a1 = repr(b8)
s = open(out, 'w')
s.write('# Encrypt By WHOAMI-XD\n# My FACEBOOK Account (Raj khan)\n# My YOUTUBE  Channel (😈👿)\n# https://github.com/WHOAMI-XD-KING\n_ = lambda __ : __import__("marshal").loads(__import__("zlib").decompress(__import__("base64").b64decode(__import__("marshal").loads(__import__("base64").b64decode(__import__("marshal").loads(__import__("base64").b64decode(__import__("marshal").loads(__import__("base64").b64decode(__import__("marshal").loads(__import__("base64").b64decode(__import__("marshal").loads(__import__("base64").b64decode(__import__("marshal").loads(__import__("base64").b64decode(__import__("marshal").loads(__import__("base64").b85decode(__[::-1])))))))))))))))));exec((_)(' + str(a1)[::-1] + '))')
s.close()
print('\x1b[1;94m[\x1b[1;92m\x1b[1;94m] \x1b[1;97  File saved as \x1b[1;96m{ \x1b[1;92m%s \x1b[1;96m}' % out)
