from utilities.classes import Node, for_node_in_list

"""
something something
"""


class Solution:
    @staticmethod
    def solution(head: Node):
        prev = None
        curr = head
        next = None

        while curr.next is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


cases = [(2, 4, 6, 8, 10)]


def main():
    for case in cases:
        print(f"{case}\n")
        list_head = Node.from_list(case)
        print(f"{list_head}")
        retval = Solution.solution(list_head)
        print(f"{case}\n=\t{retval}\n")


if __name__ == "__main__":
    main()
