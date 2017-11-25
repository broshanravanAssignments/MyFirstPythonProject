import random
import sys
import os

class Human:

    __name =''
    __age = 0
    __sex = ''
    __hight = 0

    def  __init__(self, name, age, sex, hight):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__hight = hight


    def set__sex(self,sex):
        self.__sex = sex

    def get__sex(self):
        return self.__sex

    def set__hight(self,hight):
        self.__hight = hight

    def get__hight(self):
        return self.__hight

    def set__age(self, age):
        set.__age = age

    def get__age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name