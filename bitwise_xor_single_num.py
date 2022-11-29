"""
n a non-empty array of integers, every number appears twice except for one, find that single number.

"""


class Solution:
    @staticmethod
    def solution(arr):
        """N XOR N is false
        therefore if you XOR all numbers together all dupes will be inverted
        only the bin of the single num will remain"""
        num = 0
        for i in arr:
            on = num
            num ^= i
            print(f"num:{num}({bin(num)}) = {on}({bin(on)}) XOR {i}({bin(i)})")
        return num


cases = [[1, 4, 2, 1, 3, 2, 3]]


def main():
    for case in cases:
        print(f"{case}\n")
        retval = Solution.solution(case)
        print(f"{case}\n=\t{retval}\n")


if __name__ == "__main__":
    main()
