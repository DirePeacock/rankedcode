"""
something something
"""


class Solution:
    @staticmethod
    def solution(nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  # swap
            else:
                i += 1
        return nums


cases = [
    (([3, 1, 5, 4, 2]), [1, 2, 3, 4, 5]),
    (([2, 6, 4, 3, 1, 5]), [1, 2, 3, 4, 5, 6]),
]


def main():
    for case in cases:
        args, expected = case[0], case[1]
        print(f"args= {args}\n")

        retval = Solution.solution(args)
        print(f"expected = {expected}")
        print(f"{case}\n=\t{retval}\n")

        print("YES" if retval == expected else "NO")


if __name__ == "__main__":
    main()
