"""
something something
"""
class Solution():
    @staticmethod
    def solution(s,t):
        char_map={}
        for i in range(0, len(s)):
            if t[i] in char_map.values() and s[i] not in char_map.keys():
                return False
            if s[i] not in char_map.keys():
                char_map[s[i]] = t[i]
            if char_map[s[i]] != t[i]:
                return False
            
        print(char_map)
        return True

cases = [['badc', 'baba'], ['add', 'egg'], ['title', 'paper']]
def main():
    for case in cases:
        print(f'{case}\n')
        retval = Solution.solution(*case)
        print(f"{case}\n{retval}")
if __name__=="__main__":
    main()