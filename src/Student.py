import random
import sys
import os
from Human import Human

class Student(Human):

    __studentId =0
    __year = 0
    __course = ''

    def __init__(self, studentId, year, course):
        self.__studentId =studentId
        self.__year = year
        self.__course = course

    def set__studentId(self, studentId):
        self.__studentId = studentId

    def get__stusentID(self):
        return self.__studentId

    def set__year(self, year):
        self.__year = year

    def get__year(self):
        return self.__year

    def set__course(self, course):
        self.__course = course

    def get__course(self):
        return self.__course

    def showDetails(self):
        return "student of year {} her student Id is {} and her job is {}".format(self.__year,
                                                                                  self.__studentId,
                                                                                  self.__course)
atti = Student( 1234, 5, 'Rezalat')

print(atti.showDetails())
