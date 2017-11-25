
import random
import sys
import os

def add(num_1, num_2):
    ans = num_1 + num_2
    return ans

i = 3
j =9
sum = add(4, 8)
print('4 + 8 is: ', sum)

g = "Hello "
l =  'World'
combidedSr = add (g, l)
print("combined String is: ", combidedSr)

statement = "%s is %s and %s is %s "%('Areya','Chool Talaayee', 'Atoosa','bad Jens')
print(statement)

print(statement[:4])
print(statement[9:20])
print(statement[:-10])
last_five = statement[-9:]
print(last_five.capitalize())
print(statement[0:5] + '??? How about that!!!!!!')
print(statement.find('Atoosa'))
print(statement.replace('Atoosa','Atti Khare'))
words_list = statement.split(' ')
print (words_list)

'''
how about this
is this another moulty line 
comment, but in code
'''

print('''This is a 
printed Multy 
line
Coment
or is it''')



