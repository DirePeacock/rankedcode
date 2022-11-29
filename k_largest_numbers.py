"""
something something
"""
import heapq


class Solution:
    @staticmethod
    def solution(nums, k):
        minHeap = []
        # put first 'K' numbers in the min heap
        for i in range(k):
            heapq.heappush(minHeap, nums[i])

        # go through the remaining numbers of the array, if the number from the array is bigger than the
        # top(smallest) number of the min-heap, remove the top number from heap and add the number from array
        for i in range(k, len(nums)):
            if nums[i] > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, nums[i])
        return minHeap


cases = [(([3, 1, 5, 12, 2, 11], 3), [5, 12, 11])]


def main():
    for case in cases:
        args, expected = case[0], case[1]
        print(f"{case}\n")

        retval = Solution.solution(*args)
        print(f"expected = {expected}")
        print(f"{case}\n=\t{retval}\n")

        print("YES" if retval == expected else "NO")


if __name__ == "__main__":
    main()
