"""
#416 Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

"""

class Solution(object):
    def hamming_distance(self, x, y):

        return bin(x^y).count("1")

"""
Knowledge points:
1. bin() convert integer to binanry number
2. x^y:if a bit is off in both numbers, 
it stays off in the result. Note that XOR-ing a 
number with itself will always result in 0. 
Ex: 1^4 = 0001 ^ 0100 = 0101 = 5
"""


