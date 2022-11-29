"""
leetcode 1 two sum
find 2 numbers in a list that add up to another specified sum

"""


class Solution:
    @staticmethod
    def solution(nums: list[int], target: int) -> list[int]:
        """
        edgecase
        this pattern"""

        if len(nums) == 0:
            return [-1, -1]
        cache = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in cache.keys():
                return [cache[complement], i]

            cache[nums[i]] = i
            print(f"i[{i}]={nums[i]}, comp={complement}, cache={cache}")

        return [-1, -1]

    @staticmethod
    def old_solution(nums: list[int], target: int) -> list[int]:
        compliments = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in complements.keys():
                return [i, complements[comp]]
            complements[nums[i]] = i


cases = [(([2, 11, 15, 7], 9), [0, 3]), (([3, 2, 4], 6), [1, 2]), (([3, 3], 6), [0, 1])]


def main():
    for case in cases:
        args, expected = case[0], case[1]
        print(f"{case}\n")

        retval = Solution.solution(*args)
        print(f"expected = {expected}")
        print(f"{case}\n=\t{retval}\n")

        print("YES" if retval == expected else "NO")


if __name__ == "__main__":
    main()
