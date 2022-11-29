from utilities.classes import TreeNode as TN

"""
Given a binary tree and a number ‘S’, 
find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.
"""


class Solution:
    @classmethod
    def solution(cls, root, val):
        return cls.recursive_pathsum(root, val)

    @classmethod
    def recursive_pathsum(cls, node, val):
        val_remaining = val - node.value

        if val_remaining == 0:
            return True

        if node is None:
            return False

        left_walk = False if not node.left else cls.recursive_pathsum(node.left, val_remaining)
        right_walk = False if not node.right else cls.recursive_pathsum(node.right, val_remaining)
        return left_walk or right_walk


cases = [
    ((TN(1, (2, 4, 5), (3, 6, 7)), 10), True),
    ((TN(12, (7, 9), (1, 10, 5)), 23), True),
    ((TN(12, (7, 9), (1, 10, 5)), 16), False),
]


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
