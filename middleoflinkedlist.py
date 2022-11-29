"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node."""

from utilities.classes import ListNode


class Solution:
    @staticmethod
    def solution(head):
        """approach 1 fast slow pointer or whatever
        can't be circular i hope
        time o(n)
        middle o(1)
        """
        fast_node_iter = head
        middle = head
        switch_every_other = True
        list_len = 1

        while fast_node_iter.next is not None:
            fast_node_iter = fast_node_iter.next
            if switch_every_other:
                middle = middle.next
            switch_every_other = not switch_every_other
            list_len += 1

        return middle


cases = [(([1, 2, 3, 4]), 4), (([1, 2, 3, 4, 5]), 3)]


def main():
    for case in cases:
        args, expected = case[0], case[1]
        if len(args) < 1:
            continue
        print(f"{case}\n")
        head = ListNode.from_list(args[0], args[1])
        retval = Solution.solution(head=head)
        print(f"expected = {expected}")
        print(f"{case}\n=\t{retval}\n")

        print("YES" if retval.value == expected else "NO")


if __name__ == "__main__":
    main()
