#!/usr/bin/python3
from hashlib import *
from requests import get
from sys import platform
if platform in ['linux','linux2']:
    w = '\033[0m'
    F = '\033[32;1m'
    n = '\033[31;1m'
else:
    w = F = n = ''
flag = False
def out(x,y,z):   # x = flag & y = line & z = want2
    if x == True:
        print(F+'[+]found --> '+y+' = '+z)
    else:
        print(n+'[-]not found --> S0rry your Hash not found :'+z)
def decrypter(want2,file):
    if len(want2) == 32: # md5
        pali = input('your hash is md5 i can crack the hash without using password list do U want use Your passward list[Y/N] :')
        if pali == 'N' or pali == 'n':
            md = str(get('http://www.nitrxgen.net/md5db/' + want2).text)
            if len(md) != 0:
                print(F+'[+]found --> '+want2+' = '+md)
            else:
                print(n+'[-]not found --> S0rry your Hash not found :'+want2)
        elif pali == 'Y' or pali == 'y':
            try:
                with open(file,mode='r') as f:
                    for line in f:
                        line = line.strip()
                        if md5(line.encode()).hexdigest() == want2:
                            flag = True;break
                        else:
                            flag = False
                    out(flag,line,want2)
            except:
                print(n+'No file with this name, please check your inputs')           
        else:
            print('U have error in your inputs')
    elif len(want2) == 40: # sha1
        try:
            with open(file,mode='r') as f:
                for line in f:
                    line = line.strip()
                    if sha1(line.encode()).hexdigest() == want2:
                        flag = True;break
                    else:
                        flag = False
                out(flag,line,want2)
        except:
            print(n+'No file with this name, please check your inputs')
    elif len(want2) == 56: # sha224
        try:
            with open(file,mode='r') as f:
                for line in f:
                    line = line.strip()
                    if sha224(line.encode()).hexdigest() == want2:
                        flag = True;break
                    else:
                        flag = False
                out(flag,line,want2)
        except:
            print(n+'No file with this name, please check your inputs')
    elif len(want2) == 64: #sha256
        try:
            with open(file,mode='r') as f:
                for line in f:
                    line = line.strip()
                    if sha256(line.encode()).hexdigest() == want2:
                        flag = True;break
                    else:
                        flag = False
                out(flag,line,want2)
        except:
            print(n+'No file with this name, please check your inputs')
    elif len(want2) == 96: # sha384
        try:
            with open(file,mode='r') as f:
                for line in f:
                    line = line.strip()
                    if sha384(line.encode()).hexdigest() == want2:
                        flag = True;break
                    else:
                        flag = False
                out(flag,line,want2)
        except:
            print(n+'No file with this name, please check your inputs')
    elif len(want2) == 128:
        try:
            with open(file,mode='r') as f:
                for line in f:
                    line = line.strip()
                    if sha512(line.encode()).hexdigest() == want2:
                        flag = True;break
                    else:
                        flag = False
                out(flag,line,want2)
        except:
            print(n+'No file with this name, please check your inputs')
    else:
    	print("Sorry I can not specify the type of hash")
print(n+'''
    $$$$$$$$\                 $$\   $$\                  $$$$$$\  
    $$  _____|                $$ | $$  |                $$  __$$\ 
    $$ |                      $$ |$$  /                 $$ /  \__|
    $$$$$\                    $$$$$  /                  \$$$$$$\  
    $$  __|                   $$  $$<                    \____$$\ 
    $$ |                      $$ |\$$\                  $$\   $$ |
    $$ |            $$\       $$ | \$$\       $$\       \$$$$$$  |
    \__|            \__|      \__|  \__|      \__|       \______/
'''+"\n I love Jordan & I'm fine")
print(F+'''
######################################################
[ #Developed_by_Mo0Ssaa ]
[ Twitter:https://twitter.com/AhmedMosaa18 ]
[ E-mail:am01003264893@gmail.com ]
[ Facebook:https://www.facebook.com/Ahmed.R.Mosaa404 ]
[ Github:https://github.com/mosaa404 ]
#######################################################
''')
while True:
    ch = input(w+"If U want Encrypter  press 1 or U want Decrypter  press 2 :")
    if ch == '1' :
        print("What kind of encodeing "
        "\n1.md5"
        "\n2.sha1"
        "\n3.sha224"
        "\n4.sha256"
        "\n5.sha384"
        "\n6.sha512"
        "\nChoose type{1 - 2 - 3 - 4 - 5 - 6}")
        ch2 = input("Enter the number of tybe :")
        want = input ("Enter the thing to be encrypted :")
        if ch2 == '1':
            en = md5(want.encode()).hexdigest()
            print(want,' = ',en)
        elif ch2 == '2':
            en = sha1(want.encode()).hexdigest()
            print(want,' = ',en)
        elif ch2 == '3':
            en = sha224(want.encode()).hexdigest()
            print(want,' = ',en)
        elif ch2 == '4':
            en = sha256(want.encode()).hexdigest()
            print(want,' = ',en)
        elif ch2 == '5':
            en = sha384(want.encode()).hexdigest()
            print(want,' = ',en)
        elif ch2 == '6':
            en = sha512(want.encode()).hexdigest()
            print(want,' = ',en)
        else:
            print("U have error in your inputs")
    elif ch == '2':
        want2 = input ("Enter the Hash :")
        file = input("Enter name of password list :")
        decrypter(want2,file)
    else:
        print("U have error in your inputs")
