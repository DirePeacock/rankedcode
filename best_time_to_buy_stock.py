"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy 
one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution:
    @staticmethod
    def solution(prices):
        """for price in days return the largest diff
        the pair of numbers where r-l would be the largest
        approach 1
        trying to use two pointers
        isn't necessary
        approach 2
        one pass
        you can do this because the order of it being r-l=prof  means any new min can only affect the higher indeicies
        """

        min_val = float("inf")
        min_val_index = 0
        max_diff = 0
        for i in range(0, len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
                min_val_index = i
            elif prices[i] - min_val > max_diff:
                max_diff = prices[i] - min_val
                print(f"p[r({i})] - p[l({min_val_index})] = {max_diff}")

        return max_diff

    def bad_2p_solution(self, prices):
        """the iterator isn't right and also 2 pointers are not necessary"""
        l = 0
        r = 1
        max_diff = 0
        if len(prices) < 2:
            return 0

        while l < len(prices) - 1:
            diff = prices[r] - prices[l]
            if diff > max_diff:
                max_diff = diff
                print(f"p[r({r})] - p[l({l})] = {max_diff}")

            l += 1
            if l == r:
                r += 1
        return max_diff


cases = [((7, 1, 5, 3, 6, 4), 5), ((7, 6, 4, 3, 1), 0)]


def main():
    for case in cases:
        args, expected = case[0], case[1]
        print(f"{case}\n")

        retval = Solution.solution(args)
        print(f"expected = {expected}")
        print(f"{case}\n=\t{retval}\n")

        print("YES" if retval == expected else "NO")


if __name__ == "__main__":
    main()
