import random
import sys
import os


name = 'Bruce'

if (name =='Atoosa'):
    print("you are bad jense")
elif (name == 'Areya'):
    print('you are Chool talayee')
elif not(name=='Bruce'):
    print('What the Heck')
else:
    print('I do not know what you are')

space =' '
for x in range(0,11):
    print(x , end ="")
    print(', ', end="")

print (' ')

random_number = random.randrange(0, 20)

while (random_number != 15 ):
    if (random_number % 3 == 0):
       print(random_number, end=', ')
    random_number = random.randrange(0, 20)

print (' ')

i = 0
while (i != 15 ):
    print('i = ', i, end =' ')
    print(', ', end=' ')
    i +=1
