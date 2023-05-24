# 3_Print colored text

'''
from termcolor import colored

print("\033[1;32m This text is Bright Green  \n")
txt = input("type text : ")
color = input("type color : ")

text_color = colored(txt,color,attrs=['reverse', 'blink'])
print(text_color)
'''

'''
import colorama
from colorama import Fore

print(Fore.RED + 'This text is red in color')
'''

from clrprint import *
#clrhelp()  # to see colors available

text_input = clrinput('Please type your Text : ', clr='green')  # just like input()

clrprint('Name of colors:\n','red or r\n','yellow or y\n', 'green or g\n','blue or b\n', 'purple or p\n','magenta or m\n','white is default\n', clr='green,r,y,g,b,p,m,default')
    
color_input = clrinput('Please type Color : ', clr='green')  # just like input()

clrprint('Your Colored Text : ', text_input, clr=f'g,{color_input}')  # just like print()
