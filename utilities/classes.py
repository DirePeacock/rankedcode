import logging

"""
Given a list of non-overlapping intervals sorted by their start time, 
insert a given interval at the correct position and merge all necessary intervals 
to produce a list that has only mutually exclusive intervals.
"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]"

    def print_interval(self):
        print(self.__str__(), end="")

    def __repr__(self):
        return f"<Interval object: {self.__str__()}>"


class ListNode:
    # used for the min-heap
    def __lt__(self, other):
        return self.value < other.value

    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def as_list(self):
        retval = []
        node_i = self
        while node_i is not None:
            retval.append(node_i.value)
            node_i = node_i.next
        return retval

    def __repr__(self):
        values = ", ".join(str(num) for num in self.as_list())
        return f"<Interval object: [{values}]>"

    @classmethod
    def from_list(cls, list, double_linked=False):
        """make a new lnked list from a list of values, returns the head node"""
        if len(list) < 1:
            return None
        start = ListNode(value=list[0]) if not isinstance(list[0], ListNode) else list[0]
        curr = start

        for i in range(1, len(list)):
            curr.next = ListNode(value=list[i]) if not isinstance(list[i], ListNode) else list[i]
            if double_linked:
                curr.next.prev = curr
            curr = curr.next

        return start

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def __eq__(self, obj):
        if isinstance(obj, list):
            return self.as_list() == obj
        else:
            return super().__eq__(obj)


class for_node_in_list:
    def __init__(self, node, reverse=False):
        self.node = node
        self.reverse = reverse

    def __iter__(self):
        return self

    def __next__(self):
        if self.node.next is not None and not self.reverse:
            self.node = self.node.next
            yield self.node
        elif self.node.prev is not None and self.reverse:
            self.node = self.node.prev
            yield self.node
        else:
            logging.debug(f"ending at {self.node.prev} > {self.node} > {self.node.next}")
            raise StopIteration


def _is_tree_val(obj):
    """return true if this is something that we want as a list val"""
    return isinstance(obj, (int)) or obj is None


class TreeNode:
    """this assumes a child will be less than its parent or right sibling"""

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = None

        # self.left = (
        #     left if isinstance(left, TreeNode) or left is None else TreeNode(*left if not _is_tree_val(left) else left)
        # )
        if isinstance(left, TreeNode) or left is None:
            self.left = left
        else:
            if _is_tree_val(left):
                self.left = TreeNode(left)
            else:
                self.left = TreeNode(*left)
        self.right = None
        # self.right = (
        #     right
        #     if isinstance(right, TreeNode) or right is None
        #     else TreeNode(*right if not _is_tree_val(right) else right)
        # )
        if isinstance(right, TreeNode) or right is None:
            self.right = right
        else:
            if _is_tree_val(right):
                self.right = TreeNode(right)
            else:
                self.right = TreeNode(*right)

    @classmethod
    def from_list(cls, list):
        return cls.__init__()

    def __getitem__(self, key):
        if key == 0:
            return self.left
        elif key == 1:
            return self.right
        else:
            raise IndexError(f"index[{key}] out of range in bin tree")

    def __setitem__(self, key, value):
        if key == 0:
            self.left = value
        elif key == 1:
            self.right = value
        else:
            raise IndexError(f"index[{key}] out of range in bin tree")
