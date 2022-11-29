"""
something something
"""


class Solution:
    @staticmethod
    def solution(arr, key):
        start = 0
        end = len(arr) - 1
        is_ascending = arr[start] <= arr[end]

        while start <= end:
            # assume that start and end may or may not be 0
            # this doesn't actually matter in python but it is neat
            mid = int(start + (end - start) / 2)

            if arr[mid] == key:
                return mid
            elif is_ascending:
                if key < arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if key > arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

        return -1


cases = [
    ([4, 6, 10], 10),
    ([1, 2, 3, 4, 5, 6, 7], 5),
    ([10, 6, 4], 10),
    ([10, 6, 4], 4),
]


def main():
    for case in cases:
        print(f"{case}\n")
        retval = Solution.solution(*case)
        print(f"{case}\n=\t{retval}\n")


if __name__ == "__main__":
    main()
