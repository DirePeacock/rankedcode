from utilities.classes import ListNode

"""

"""


class Solution:
    @staticmethod
    def solution(list1, list2):
        """iterative solution:
        space O(1)
        time O(n+m)
        """
        head1 = list1
        head2 = list2

        new_head = ListNode(-1)
        list_iter = new_head

        while True:
            if head1 is not None and head2 is not None:
                if head1.value < head2.value:
                    list_iter.next = head1
                    head1 = head1.next
                else:
                    list_iter.next = head2
                    head2 = head2.next
            elif head1 is not None and head2 is None:
                list_iter.next = head1
                head1 = head1.next
            elif head1 is None and head2 is not None:
                list_iter.next = head2
                head2 = head2.next
            else:
                break
            new_head = new_head if new_head is not None else list_iter
            list_iter = list_iter.next
            print(new_head.as_list())
        return new_head.next or []


cases = [(([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]), (([], []), []), (([], [0]), [0])]


def main():
    for case in cases:
        args, expected = case[0], case[1]
        if len(args) < 1:
            continue
        print(f"{case}\n")
        list1 = ListNode.from_list(args[0])
        list2 = ListNode.from_list(args[1])
        retval = Solution.solution(list1, list2)
        print(f"expected = {expected}")
        print(f"{case}\n=\t{retval}\n")

        print("YES" if retval == expected else "NO")


if __name__ == "__main__":
    main()
