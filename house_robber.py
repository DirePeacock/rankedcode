"""
https://leetcode.com/problems/house-robber/ 
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them 
is that adjacent houses have security systems connected and it will automatically 
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution:
    @staticmethod
    def solution(nums: list[int]) -> int:
        # Special handling for empty case.
        if not nums:
            return 0
        # define a sub problem table
        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        N = len(nums)

        # Base case initialization.
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]

        # DP table calculations.
        for i in range(N - 2, -1, -1):

            # Same as recursive solution.

            print(f"maxRobbedAmount[i + 1]={maxRobbedAmount[i + 1]}")
            print(f"maxRobbedAmount[i + 2] + nums[i]={maxRobbedAmount[i + 2] + nums[i]}")
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])

            print(f"maxRobbedAmount[{maxRobbedAmount}]")
        return maxRobbedAmount[0]


cases = [(([1, 2, 3, 1]), 4), (([2, 7, 9, 3, 1]), 12)]


def main():
    for case in cases:
        args, expected = case[0], case[1]
        if len(args) < 1:
            continue
        print(f"{case}\n")

        retval = Solution.solution(args)
        print(f"expected = {expected}")
        print(f"{case}\n=\t{retval}\n")

        print("YES" if retval == expected else "NO")


if __name__ == "__main__":
    main()
