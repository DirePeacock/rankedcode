"""
n passengers board an airplane with exactly n seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of the passengers will:

    Take their own seat if it is still available, and
    Pick other seats randomly when they find their seat occupied

Return the probability that the nth person gets his own seat."""


class Solution:
    @staticmethod
    def solution(n):
        


cases = [((), None), ((), None)]


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
