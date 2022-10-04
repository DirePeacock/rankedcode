"""Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.


Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

 

Constraints:
    1 <= s.length <= 16
    s contains only lowercase English letters.
"""
from utils import is_palindrome

class Solution:
    @staticmethod
    def solution(chars: str) -> list[list[str]]:
        retval = []
        
        def recursive_dfs(i, current):
            if i == len(chars):
                retval.append(current[:])
            else:
                for j in range(i, len(chars)):
                    ij_permutation=chars[i:j+1]
                    print(f"\t{i},\t'{ij_permutation}',\t{j}")
                    if is_palindrome(ij_permutation):
                        current.append(ij_permutation)
                        recursive_dfs(j+1, current)
                        current.pop()

        recursive_dfs(0, [])
        return retval

cases = ["aaa", "aaba"]

def main():
    for case in cases:
        print(f'{case}\n')
        retval = Solution.solution(case)
        print(f"{case}\n{retval}")
        
if __name__=="__main__":
    main()