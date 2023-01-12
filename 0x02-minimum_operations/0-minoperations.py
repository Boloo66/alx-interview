#!/usr/bin/python3
''' this algo uses best OOP practices, be clean coder!'''


def minOperations(n):
    ''' calculates the fewest number of
        operations needed to result in exactly n '''

    if n <= 1 or not isinstance(n, int):
        return 0

    clip = ClipBoardOperations(1)
    clip.copy_all()

    while clip.output < n:
        clip.paste()

        if clip.output < n and n % clip.output == 0:
            clip.copy_all()

    return clip.number_of_operations


class ClipBoardOperations:
    ''' clipboard operations '''

    def __init__(self, data):
        self.__output = data
        self.__clipboard = 0
        self.__number_of_operations = 0

    @property
    def output(self):
        return self.__output

    @property
    def number_of_operations(self):
        return self.__number_of_operations

    def copy_all(self):
        self.__clipboard = self.__output
        self.__number_of_operations -= -1

    def paste(self):
        self.__output += self.__clipboard
        self.__number_of_operations -= -1
