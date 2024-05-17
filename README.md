# Projects-in-Python

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


## 1)Vital Message

![image](https://github.com/bxlxji/Projects-in-Python/assets/79824566/0eed4fb7-f0bc-482d-bf6a-f83610c23796)

![image](https://github.com/bxlxji/Projects-in-Python/assets/79824566/389896c3-240f-41b1-9825-d10b03a70328)

![image](https://github.com/bxlxji/Projects-in-Python/assets/79824566/26043197-a7e8-4f50-b6dc-1d84243dc278)


``` python
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
```

#### Program outputs

![Screenshot 2024-05-17 153159](https://github.com/bxlxji/Projects-in-Python/assets/79824566/d8301c0a-c8dd-4f00-be30-e4d75b474e8a)

![Screenshot 2024-05-17 153229](https://github.com/bxlxji/Projects-in-Python/assets/79824566/c230cba8-9686-47b7-b44f-79104d12f788)


![Screenshot 2024-05-17 153419](https://github.com/bxlxji/Projects-in-Python/assets/79824566/be58524a-9a3b-44e9-ae85-b5a95e437255)

![Screenshot 2024-05-17 153441](https://github.com/bxlxji/Projects-in-Python/assets/79824566/bf03480f-2bb5-4f67-8a6c-32cfc1cf0366)



## 2)Shootout

![image](https://github.com/bxlxji/Projects-in-Python/assets/79824566/34960274-86e7-46ba-b6bc-617c227a38bf)

![image](https://github.com/bxlxji/Projects-in-Python/assets/79824566/36afce13-8a48-489b-852c-cd0577258a8b)

``` python
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

```

#### Program outputs

![Screenshot 2024-05-17 152856](https://github.com/bxlxji/Projects-in-Python/assets/79824566/c4e368a7-dd6b-43a9-a1ed-090ec4249371)

![Screenshot 2024-05-17 152916](https://github.com/bxlxji/Projects-in-Python/assets/79824566/56e7387c-7bb6-4a98-8589-8359f0767c82)
