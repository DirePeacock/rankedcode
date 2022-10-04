"""
something something
"""
class Solution():
    @staticmethod
    def solution(*args, **kwargs):
        return None

cases = []
def main():
    for case in cases:
        print(f'{case}\n')
        retval = Solution.solution(case)
        print(f"{case}\n{retval}")
if __name__=="__main__":
    main()