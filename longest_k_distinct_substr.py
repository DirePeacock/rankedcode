"""
for w_end in range(len[arr]):
    new_elem = arr[w_end]
    
"""
class Solution():
    @staticmethod
    def solution(str1, k):
        window_start=0
        window_end=1
        longest_substr = ''
        char_frequency = {}

        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char not in char_frequency:
                char_frequency[right_char] = 0
            char_frequency[right_char] += 1

            # while 
            while len() == 1 + window_end - window_start:
                left_char = str1[window_start]
                char_frequency[left_char] -= 1
                if 0 == char_frequency[left_char]:
                    del char_frequency[left_char]
                window_start += 1 
            if len(longest_substr) <= window_end - window_start + 1:
                longest_substr = str1[window_start:window_end+1]
        
        return len(longest_substr)

    
    
   

cases = [("aabccbb",2),
         ("abbbb",1),
         ('abccde',3),
         ('cbbebi',10),
]
def main():
    for case in cases:
        print(f'{case}\n')
        retval = Solution.solution(*case)
        print(f"{case}\n=\t{retval}\n")
if __name__=="__main__":
    main()