"""
Given an array of positive integers and a number \"S,\" 
find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. 
Return 0 if no such subarray exists.
"""
import math

class smallest_subarray_sum():
    @staticmethod
    def solution(arr, s):
        small_subarr=[]
        window_sum = 0
        window_end = 0
        window_start = 0
        
        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            while window_sum >= s:

                if len(small_subarr) > (1 + window_end - window_start) or small_subarr == []:
                    small_subarr = arr[window_start:(window_end+1)]
                window_sum -= arr[window_start]
                window_start += 1

        print(small_subarr)
        return len(small_subarr)
        

cases = [([2,1,5,2,3,2],7), 
         ([2,1,5,2,8],7),
         ([3,4,1,1,6],8)]

def main():
    for case in cases:
        print(f'{case}\n')
        retval = smallest_subarray_sum.solution(*case)
        print(f"{case}\n\t={retval}\n\n")
if __name__=="__main__":
    main()