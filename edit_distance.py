"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

"""


class Solution:
    @staticmethod
    def solution(left: str, right: str) -> int:
        """2d dynamic programming
        insert, (i, j+1),
            compare the current index in word 1 to the next on in word 2
        delete, (i+1, j)
            compare the next char in left to char j in right[j]
        replace (i+1, j+1)
            compare

        DETERMINE WHICH SUBPROBLEMS DEPEND ON
        here the subproblems are dependent on smaller

        consider a 2d array of the words Right+1 by Left +1
              r h t _
            l
            f
            t       1
            _       0
        the 2d cache array will be the number of the changes that are needed to make a word

        """
        dp_cache = [[float("inf")] * (len(right) + 1) for _ in range(len(left) + 1)]

        for j in range(len(right) + 1):
            dp_cache[len(left)][j] = len(right) - j

        for i in range(len(left) + 1):
            dp_cache[i][len(right)] = len(left) - i

        for i in range(len(left) - 1, -1, -1):
            for j in range(len(right) - 1, -1, -1):
                if left[i] == right[j]:
                    dp_cache[i][j] = dp_cache[i + 1][j + 1]
                else:
                    dp_cache[i][j] = 1 + min(dp_cache[i + 1][j], dp_cache[i][j + 1], dp_cache[i + 1][j + 1])

        return dp_cache[0][0]


cases = [(("horse", "ros"), 3), (("intention", "execution"), 5)]


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
