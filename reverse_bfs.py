from collections import deque
from utilities.classes import TreeNode as TN

"""
do a reverse bfs thing
R-L B-T
"""


class Solution:
    @staticmethod
    def solution(root):
        retval = []
        if root is None:
            return retval
        queue = deque()
        queue.append(root)

        while 0 < len(queue):
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                current_node = queue.popleft()
                if current_node.right:
                    queue.append(current_node.right)
                if current_node.left:
                    queue.append(current_node.left)
                current_level.append(current_node.val)

            retval.insert(0, current_level)
        return retval


cases = [((1), None), ((), None)]


def make_case():
    root = TN(1, TN(2, TN(4), TN(5)), TN(3, TN(6), TN(7)))
    root2 = TN(1, (2, 4, 5), (3, 6, 7))
    return root


def main():
    expected = []
    case = make_case()
    print(f"{case}\n")

    retval = Solution.solution(case)
    print(f"expected = {expected}")
    print(f"{case}\n=\t{retval}\n")

    print("YES" if retval == expected else "NO")


if __name__ == "__main__":
    main()
