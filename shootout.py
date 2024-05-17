"""

Hey! I'm Balaji! and this is a Simple Game Program
 written in "Python" that tries to recreate
 a programming game from the 80s on the
 "BBC Micro" System.
 
 This is a small flashback into the lives 
 of the kids in the 80s and how programming 
 was made fun for them in the coding language 
 "BASIC". This was a game that came in a magazine
 published by "Usborne Computer Coding Book".
 The BBC Micro was a staple in British Schools 
 in the 80s and this inspired a lot of kids to
 get interested in Programming!  
 
 These Books consisted of many "Coding Games".
 They seem very simple now but for the 80s, 
 this was a blast! Hope you had some fun with it too!
 
 THIS IS A PROGRAM WRITTEN ONLY FOR EDUCATIONAL PURPOSES,
 NO COPYRIGHT INFRINGEMENT INTENDED.

"""
from time import sleep
from random import randint
import msvcrt
import os

os.system('cls||clear')

print('COWBOY SHOOTOUT'
      '\n''YOU ARE BACK TO BACK'
      '\n''TAKE 10 PACES...')

W = 1
while W <= 10:
    sleep(0.2)
    print(W,'...')
    W += 1

S = randint(1,5)
sleep(S*0.2)
print('HE DRAWS...')

x = 0
while x < S:
    if msvcrt.kbhit() == True:
        print('BUT YOU SHOOT FIRST'
              '\n''YOU KILLED HIM')
        exit()
    else:
        sleep(0.2)
        x = x+1

print('AND SHOOTS'
      '\n''YOU ARE DEAD')