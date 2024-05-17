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

import os
import random
import string
import time

os.system('cls||clear')

print('VITAL MESSAGE'
      '\n')

while True:
    D = int(input('HOW DIFFICULT? (4-10)'))
    if D>=4 and D<=10:
        break

M = ''

for i in range(D):
    M += random.choice(string.ascii_uppercase)

print('SEND THIS MESSAGE:'
      '\n'
      '\n',M)

time.sleep(0.3*D)

os.system('cls||clear')

N = input('')

if N == M:
    print('MESSAGE CORRECT!'
          '\n''THE WAR IS OVER')
else:
    print('YOU GOT IT WRONG''\n'
          'YOU SHOULD HAVE SENT:''\n',M)