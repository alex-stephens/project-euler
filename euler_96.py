# Project Euler
# Problem 96

# Sudoku

from itertools import product
from time import time


def main():
    s = time()

    filename = "euler_96.txt"
    grids = parse(filename)

    ans = 0
    num_puzzles = len(grids)

    # read in the puzzle
    for i, grid in enumerate(grids):
        sudoku = Sudoku(grid)
        sudoku.solve()

        print(f"Solved puzzle {i+1}/{num_puzzles}")
        ans += int("".join([str(x) for x in sudoku.grid[0][:3]]))

    print(f"Time to solve: {time() - s:.2f} s")
    print(ans)


def parse(filename):
    """
    Parse the input file - returns a list of sudoku grids.
    """
    grids = []

    with open(filename, "r") as f:
        lines = f.readlines()
        num_puzzles = len(lines) // 10
        for puzzle in range(num_puzzles):
            grid = [[0 for x in range(9)] for y in range(9)]
            for i in range(9):
                for j in range(9):
                    grid[i][j] = int(lines[puzzle * 10 + i + 1][j])
            grids.append(grid)

    return grids


class Sudoku:
    def __init__(self, grid):
        self.grid = grid
        self.solved_squares = 0

        l = {x for x in range(1, 10)}
        self.options = [[set(l) for x in range(9)] for y in range(9)]
        for i, j in product([x for x in range(9)], repeat=2):
            if grid[i][j] != 0:
                self.options[i][j] = set()
                self.solved_squares += 1

    def eliminate(self, i, j):
        """
        Remove all invalid options at the given location using row, col and square
        """
        ans = set()
        for y in range(9):
            cur = self.grid[i][y]
            if cur != 0:
                ans.add(cur)
        for x in range(9):
            cur = self.grid[x][j]
            if cur != 0:
                ans.add(cur)
        R, C = i // 3, j // 3
        for r in range(3 * R, 3 * R + 3):
            for c in range(3 * C, 3 * C + 3):
                cur = self.grid[r][c]
                if cur != 0:
                    ans.add(cur)
        return ans

    def refresh(self):
        """
        Update the set of options
        """
        for (i, j) in product([x for x in range(9)], repeat=2):
            if self.grid[i][j] != 0:
                self.options[i][j] = set()
            else:
                elim = self.eliminate(i, j)
                for x in elim:
                    self.options[i][j].discard(x)

    def update(self):
        """
        Update the grid - return true if a change was made
        """
        success = False
        for (i, j) in product([x for x in range(9)], repeat=2):
            if self.grid[i][j] != 0:
                continue
            elif len(self.options[i][j]) == 1:
                self.grid[i][j] = self.options[i][j].pop()
                self.solved_squares += 1
                success = True
        return success

    def is_valid(self, testgrid, r, c, val):
        """
        Check if the given value is valid in the current test grid
        """
        # row
        for i in range(9):
            if testgrid[i][c] + self.grid[i][c] == val:
                return False
        # column
        for j in range(9):
            if testgrid[r][j] + self.grid[r][j] == val:
                return False
        # square
        R, C = r // 3, c // 3
        for i in range(3 * R, 3 * R + 3):
            for j in range(3 * C, 3 * C + 3):
                if testgrid[i][j] + self.grid[i][j] == val:
                    return False
        return True

    def dfs(self):
        """
        Perform depth-first search of the unfilled values
        """
        testgrid = [[0 for x in range(9)] for y in range(9)]
        unfilled = []
        l = {x for x in range(1, 10)}
        reducedOptions = [[set(l) for x in range(9)] for y in range(9)]
        for i, j in product([x for x in range(9)], repeat=2):
            reducedOptions[i][j] = set(self.options[i][j])
        # list of squares to check
        for i, j in product([x for x in range(9)], repeat=2):
            if self.grid[i][j] == 0:
                unfilled.append((i, j))

        n = 0  # index of unfilled square to check
        solved = False

        while not solved:
            i, j = unfilled[n]
            val = reducedOptions[i][j].pop()  # take a value from the options

            # if valid, move onto next square
            if self.is_valid(testgrid, i, j, val):
                testgrid[i][j] = val
                n += 1
                if n >= len(unfilled):
                    solved = True
                    break

            # otherwise, if there no other option on the current square,
            # move back
            elif len(reducedOptions[i][j]) == 0:
                while len(reducedOptions[i][j]) == 0:
                    # repopulate and move up until there are more options
                    reducedOptions[i][j] = set(self.options[i][j])
                    n -= 1
                    i, j = unfilled[n]
                    testgrid[i][j] = 0

                    if n < 0:
                        solved = True
                        print("-------- ERROR: BACKTRACKING EXCEEDED --------")
                        break

        for (i, j) in product([x for x in range(9)], repeat=2):
            self.grid[i][j] += testgrid[i][j]
            self.solved_squares = 81

    def solve(self):
        """
        Solve the puzzle
        """
        # Update as much as possible by direct deduction
        success = True
        while success:
            self.refresh()
            success = self.update()

        # complete via depth-first search
        if self.solved_squares < 81:
            self.dfs()


if __name__ == "__main__":
    main()
