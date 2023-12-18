import os
import shutil
import pyperclip
from colorama import Fore, Style

# First of all please download shutil and pyperclip libraries, then run the code :)

while True:
    
    a = int(input('''please select:
1- Viewing the content of existing files
2- Deleting files and folders
3- rename files
4- copy files
5- view List of available files and folders
6- Transfer files
7- Search inside files
8- Viewing the number of lines and characters of files
        '''))
    

    if a == 1:
        b = input('open which file: ')
        f = open(b,)
        r = f.read()
        print(r)


    elif a == 2:
        b = input('wich file or order do you want to remove? ')
        os.remove(b)
        print('Done')


    elif a == 3:
        b = input('Wich file do you want to rename? ')
        d =input('what do you want to rename? ')
        os.rename(b,d)
        print('file renamed to ',d)


    elif a == 4:
        b = input('wich file do you want to copy? ')
        with open(b,'r') as file:
            d = file.read()
            pyperclip.copy(d)
        print('Done')
        

    elif a == 5:
        b = input('Wich folder do you wnat to see the lists of files or folders? ')
        print(os.listdir(b))


    elif a == 6:
        b = input('wich file do you want to entegal? ')
        d = input('Wich file is your destination? ')
        shutil.copy(b,d)
        print('Done')


    elif a == 7:
        b = input('wich file do you want to search? ')
        f = open(b)

        s = str(f.read())
        lis = s.split()
        d = input('what do you want to search? ')

        if d in lis:
            print('yes it is in this file')

        else:
            print("it's not in this file")


    elif a == 8 :
        b = input('which file do you want to see the len? ')
        f = open(b)
        d = int(input('What do you want: 1)numbers of charachters  2)numbers of satrs   '))

        if d == 1:
            s = f.read()
            lis = str(s).split()
            lis2 = ''.join(lis)
            print('numbers of charachters are: ', len(lis2))
            
        else:
            words = f.readlines()
            print('numbers of satrs are: ', len(words))
        

    c = int(input('do you want to continue? 1)Yes 2)No   '))
    if c==1:
        continue
    elif c==2:
        break


print(Fore.RED+'Thanks for using this project')
print(Style.RESET_ALL)
