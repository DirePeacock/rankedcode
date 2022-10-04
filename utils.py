import math
def is_palindrome(chars):
    """word is the same letters outwards from the middle char, like racecar"""
    cl = int(len(chars) / 2) # truncate
    return chars[:cl] == chars[:cl:-1]


def is_anagram(left,right):
    "strings contain the same occurences of characters in a different order"
    return sorted(left) == sorted(right)
    