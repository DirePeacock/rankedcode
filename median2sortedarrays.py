"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106
"""
import math

class Solution():
    
    @staticmethod
    def o_log_n_method(l,r):
        return 0
        
    @staticmethod
    def brute_force(l, r):
        return Solution.get_median(Solution.combine(l,r))

    @staticmethod
    def get_median(arr):
        i= math.ceil(len(arr) * 0.5) -1
        if 0 == len(arr) % 2:
            j = 1 + i
            return (arr[i]+arr[j])/2
        else:
            return arr[i]
        
        

    @staticmethod
    def combine(l, r):
        # zip these later idk, just have this work now. 
        # i bet theres a trick to this outside fo th ebrute for solution
        retval = []
        for elem in l:
            retval.append(elem)
        for elem in r:
            retval.append(elem)
        retval.sort()
        return retval
    
    @staticmethod
    def solution(l, r):
        return Solution.brute_force(l, r)

cases = [[[1,3], [2]],
         [[1,2], [3,4]]]
def main():
    for case in cases:
        print(f'{case}\n')
        retval = Solution.solution(*case)
        print(f"{case}\n{retval}\n")
if __name__=="__main__":
    main()