"""
something something
"""
class Solution():
    @staticmethod
    def solution(num):
        ir_map = {'I':1,
                  'IV':4,
                  'V':5, 
                  'IX':9,
                  'X':10,
                  'XL':40, 
                  'L':50, 
                  'C':100,
                  'CD':400, 
                  'D':500,
                  'CM':900, 
                  'M':1000}
        desc_key_order = list(ir_map.keys())
        desc_key_order.reverse()
        print(desc_key_order)
        as_roman = ""
        while num > 0:
            for key in desc_key_order:
                if ir_map[key] <= num:
                    as_roman += key
                    num -= ir_map[key]
                    continue
            
        return as_roman

cases = [3, 58, 1994]
def main():
    for case in cases:
        print(f'{case}\n')
        retval = Solution.solution(case)
        print(f"{case}\n{retval}")
if __name__=="__main__":
    main()