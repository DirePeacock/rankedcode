"""
Given an array of numbers sorted in an ascending order, 
find the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be 
the smallest element in the given array greater than or equal to the ‘key’.

Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.
"""


class Solution:
    @staticmethod
    def solution(arr, key):
        start = 0
        end = len(arr) - 1
        if arr[end] < key:
            return -1

        while start <= end:
            # assume that start and end may or may not be 0
            # this doesn't actually matter in python but it is neat
            mid = start + (end - start) // 2

            # key <=
            if arr[mid] == key:
                return mid
            if key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        # THIS IS WHERE THE TRICK IS
        # the start will be a lower number
        return start


cases = [
    ([4, 6, 10], 10),
    ([1, 2, 3, 4, 5, 6, 7], 5),
    ([10, 6, 4], 10),
    ([10, 6, 4], 4),
]


def main():
    for case in cases:
        print(f"{case}\n")
        retval = Solution.solution(*case)
        print(f"{case}\n=\t{retval}\n")


if __name__ == "__main__":
    main()
