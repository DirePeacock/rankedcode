from .utilities.functions import is_palindrome

"""
leetcode 5


"""


class Solution:
    @staticmethod
    def solution(word: str) -> str:
        """ok so subproblems is
        is left or right a palindrome

        it's on 1d because there is really one list of potential substr centers
        EDGECASE EVEN PALINDROMES

        1d cache len(word) by len(word)

        BOTTOM UP DynPro, problems will depend on if the subproblem of the inner palindrome


        letter in cache, treat each as being the center
        in this case i is the
        """
        retval

        dp_cache = [1 for i in range(len(word))]
        for i in range(len(word)):
            # two pointers
            # incase we want an even length palindrome

            l, r = i, i

            while l >= 0 and r < len(word) and s[l] == s[r]:
                if r - l + 1 > len(retval):
                    retval = word[l : r + 1]
                l -= 1
                r += 1
            "start iterating with 2 things"
            l, r = i, i + 1
            while l >= 0 and r < len(word) and s[l] == s[r]:
                if r - l + 1 > len(retval):
                    retval = word[l : r + 1]


cases = [(("babad"), "bab"), (("cbbd"), 2)]


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
