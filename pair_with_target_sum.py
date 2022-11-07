"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
"""
class Solution():
    @staticmethod
    def solution(arr, t):
          left_i = 0
          right_i = len(arr)-1
  
          while left_i != right_i:
              if arr[left_i] + arr[right_i] == t:
                  print(f"{arr[left_i]}+{arr[right_i]} == {t}"), 
                  return left_i, right_i
              if arr[left_i] + arr[right_i] < t:
                  left_i+=1
              else:  # arr[left_i] + arr[right_i] > t:
                  right_i -= 1 
          return -1

    @staticmethod
    def solution2(arr, target_sum):
        nums = {}  # to store numbers and their indices
        for i, num in enumerate(arr):
            if target_sum - num in nums:
                return [nums[target_sum - num], i]
            else:
                nums[arr[i]] = i
        return [-1, -1]
                

cases = [([1,2,3,4,6], 6),
         ([2,5,9,11], 11)]
def main():
    for case in cases:
        print(f'{case}\n')
        retval = Solution.solution(*case)
        print(f"{case}\n=\t{retval}\n")
if __name__=="__main__":
    main()