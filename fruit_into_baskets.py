"""
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

    Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
    You can start with any tree, but you can’t skip a tree once you have started.
    You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.
"""
class Solution():
    
    @staticmethod
    def solution(fruits):
        num_baskets = 2
        window_start, window_end = 0, 1
        fruits_table = {}
        max_fruit = 0
        while window_end < len(fruits):
            right_char = fruits[window_end]
            if right_char not in fruits_table.keys():
                fruits_table[right_char] = 0
            fruits_table[right_char] += 1 

            # while answer is good
            while len(fruits_table.keys()) > 2:
                # mv window_start left_char
                left_char = fruits[window_start]    
                fruits_table[left_char] -= 1
                if 0 == fruits_table[left_char]:
                    del fruits_table[left_char]
                window_start += 1
            
            max_fruit = max(max_fruit, sum(fruits_table.values()))

            window_end += 1

        return max_fruit

cases = ["abcac",
         "abcbbc"]

def main():
    for case in cases:
        print(f'{case}\n')
        retval = Solution.solution(case)
        print(f"{case}\n=\t{retval}\n")
if __name__=="__main__":
    main()