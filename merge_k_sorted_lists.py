"""
something something
"""
from heapq import merge
from utilities.classes import ListNode


class Solution:
    @classmethod
    def solution(cls, lists=()):
        """
        so this problem relies on the underlying ability of a min heap to merge 2 lists in N time
        then what it does is merges 2 lists at a time
        a & b then c & d then ab & cd to get abcd which happens in log(k) time

        merged lists is just a pointer
        """
        # indicies = [0 for i in range(len(lists))]
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            print(lists)
            i = 0
            while i < len(lists):
                l2 = lists.pop(i + 1) if (i + 1) < len(lists) else None
                l1 = lists.pop(i)
                lists.insert(0, cls.mergeList(l1, l2))
                i += 1

        return lists[0]

    @classmethod
    def mergeList(cls, l1, l2=None):
        return l1 if l2 is None else list(merge(l1, l2))


cases = [[[1, 6, 8], [3, 6, 7], [1, 3, 4]]]


def main():

    for case in cases:
        print(f"{case}\n")
        retval = Solution.solution(case)
        print(f"{case}\n=\t{retval}\n")


something_counter = 0


def something(default_arg=""):
    global something_counter

    default_arg = default_arg + f" {something_counter} "
    print(default_arg)
    something_counter += 1


if __name__ == "__main__":
    main()
