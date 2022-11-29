"""
Given the weights and profits of N items, we are asked to put these items in a knapsack with a capacity C.
The goal is to get the maximum profit out of the knapsack items. 
Each item can only be selected once, as we don't have multiple quantities of any item.
"""


class Solution:
    @staticmethod
    def solution(profits, weights, capacity):
        cache
        return None


cases = [(([1, 6, 10, 16], [1, 2, 3, 5], 5), None), 
         (([1, 6, 10, 16], [1, 2, 3, 5], 6), None),
         (([1, 6, 10, 16], [1, 2, 3, 5], 7), None)]
  
def main():
    for case in cases:
        args, expected = case[0], case[1]
        if len(args) < 1:
            continue
        print(f"{case}\n")

        retval = Solution.solution(*args)
        print(f"expected = {expected}")
        print(f"{case}\n=\t{retval}\n")

        print("YES" if retval == expected else "NO")


if __name__ == "__main__":
    main()
