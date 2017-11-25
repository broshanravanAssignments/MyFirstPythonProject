import random
import sys
import os


test_file = open("test_file.txt", "wb")
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("This is going to be written to file \n", 'UTF-8'))

test_file.write(bytes("This is the next line that is going to be written to file \n", 'UTF-8'))
#test_file.a



text_file = open("test_file.txt", "wb")
test_file.write(bytes("added text for more writing",'UTF-8'))

text_in_file = text_file.read()
print("TEXT IN FILE IS",text_in_file)

test_file.close()
