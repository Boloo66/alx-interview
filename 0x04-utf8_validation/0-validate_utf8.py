#!/usr/bin/python3
"""
This module validates a UTF-8 entry
"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Validates a utf-8 data and return True
    , else False"""
    def count_bit(num: int) -> int:
        """ Counts the number of starting 1's in a byte and 
        return the count """

        count: int = 0
        for i in range(7, -1, -1):
            if(num & (1 << i)):
                count += 1
            else:
                return count

        return count

    counter: int = 0
    for d in data:
        if not counter:
            counter = count_bit(d)

            if counter == 0:
                continue
            elif counter == 1 or counter > 4:
                return False
            else:
                counter -= 1
        else:
            if(count_bit(d) != 1):
                return False
            counter -= 1

    return counter == 0
