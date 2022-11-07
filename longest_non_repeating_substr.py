"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.


"""
class Solution():
    @staticmethod
    def solution(string):
        if len(string) == 0:
            return 0
        i, j = 0, 1
        substr = string[0]
        
        while j < len(string):
            curr = string[i:j+1]

            if string[j] in string[i:j]:
                while string[j] in string[i:j]:
                    i += 1
            
            elif len(curr) > len(substr):
                substr = curr 
            
            j += 1

        return len(substr)


cases = ["abcabcbb", "bbbbb", "pwwkew", ' ', "", 'au']
def main():
    for case in cases:
        print(f'main case: {case}\n')
        retval = Solution.solution(case)
        print(f"q: {case}\na: {retval}\n")
if __name__=="__main__":
    main()