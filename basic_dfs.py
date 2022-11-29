from collections import deque
from utilities.classes import TreeNode
from utilities.classes import TreeNode as TN

"""
dfs
do the children of things
"""


class Solution:
    @classmethod
    def solution(cls, root=None):
        cls.recursive_solution(root)
        # cls.iterative_solution(root)

    @classmethod
    def recursive_solution(cls, node=None):
        if node.left is not None:
            cls.recursive_solution(node.left)
        if node.right is not None:
            cls.recursive_solution(node.right)
        print(node.value)

    @staticmethod
    def iterative_solution(root=None):
        visited = []
        stack = []
        if root is None:
            return result

        visited.append(root.value)
        stack.append(root)
        while len(stack) >= 1:
            node = stack.pop()
            # print(node.value, end=" ")

            for att in ["left", "right"]:
                child = node.__getattribute__(att)

                if child is not None and child.value not in visited:
                    visited.append(child.value)
                    stack.append(child)

        for val in visited:
            print(val, end=" ")


cases = [(([12]), None), ((), None)]


def make_case():
    root = root2 = TN(1, (2, 4, 5), (3, 6, 7))
    return root


def main():
    for case in cases:
        args, expected = case[0], case[1]
        if len(args) < 1:
            continue
        print(f"{case}\n")

        retval = Solution.solution(make_case())
        print(f"expected = {expected}")
        print(f"{case}\n=\t{retval}\n")

        print("YES" if retval == expected else "NO")


if __name__ == "__main__":
    main()
