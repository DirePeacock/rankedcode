import logging

"""
something something
"""


class Solution:
    @staticmethod
    def solution(*args, **kwargs) -> int:
        """each node is going to have a number of sides equal to 4 minus the number of connections it has"""
        grid = args
        print(f"{grid}")
        height = len(grid) - 1
        width = len(grid[0]) - 1
        table = {}

        def in_bounds(a, low, high):
            return a >= low and a <= high

        for y in range(0, height):
            for x in range(0, width):
                if grid[y][x] == 1:
                    cell = (y, x)
                    table[cell] = 0

                    for neighbor in [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)]:
                        if in_bounds(neighbor[0], 0, width) and in_bounds(neighbor[1], 0, height):
                            if grid[neighbor[0]][neighbor[1]] == 1:
                                # record that the thing has found a valid neighbor into th table
                                print(f"{neighbor}:{grid[neighbor[0]][neighbor[1]]} == {cell}:{grid[x][y]}")
                                table[cell] += 1
                    print(f"{cell} has {table[cell]} neighbors")

        perimeter = 0
        for coord, neighbors in table.items():
            print(f"{coord} has {neighbors} neighbors")
            perimeter += 4 - neighbors
        return perimeter


cases = [
    (([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]), 16),
    (([[1, 1, 0, 0], [0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0]]), 16),
    # (
    #     (
    #         [
    #             [1],
    #         ]
    #     ),
    #     4,
    # ),
    # (([[1, 0]]), 4)
]


def main():

    for case in cases:
        args, expected = case[0], case[1]
        if len(args) < 1:
            continue
        print(f"{case}\n")

        retval = Solution.solution(*args)
        print(f"expected = {expected}")
        print(f"{case}\n=\t{retval}\n")

        print("YES" if retval == expected else "NO")


if __name__ == "__main__":
    main()
