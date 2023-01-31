"""minesweeper.py

Minesweeper game partial implementation using 2D lists

"""


from random import randrange


class Minefield:
    """Class which represents a minefield/game board for the game minesweeper.

    """
    def __init__(self, rows, cols, mine_freq):
        """Generates a minefield for the minesweeper game.

        Parameters:
            rows (int): number of rows in the minefield
            cols (int): number of columns in the minefield
            mine_freq (int): mines occur about once in every mine_freq
                             positions on the game board
        """
        self.rows = rows
        self.cols = cols
        self.mine_freq = mine_freq
        self.grid = [["-"] * self.cols for _ in range(self.rows)]
        self.num_mines = 0

        while self.num_mines < (self.rows * self.cols) / self.mine_freq:
            i = randrange(rows)
            j = randrange(cols)
            self.grid[i][j] = "#"
            self.num_mines += 1

    def display(self):
        """Display the minefield in an easy to read format."""
        for row in self.grid:
            print(" ".join(row))

    def sweep(self):
        """Sweep for mines.
    
        Returns:
            swept_grid (list): 2D list representing marked minesweeper board
        """
        swept_grid = [[0] * self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == "#":
                    swept_grid[i][j] = "#"
                    continue

                for row_index in range(i-1, i+2):
                    for col_index in range(j-1, j+2):
                        if row_index == -1 or col_index == -1:
                            # Do not count twice (-1 is a valid list index)
                            continue
                        try:
                            if self.grid[row_index][col_index] == "#":
                                swept_grid[i][j] += 1
                        except IndexError:
                            # ignore positions which are off the board
                            continue

        # Cast ints to strings for printing and print in user readable format
        for row in swept_grid:
            for j, col in enumerate(row):
                row[j] = str(col)
            print(" ".join(row))

        return swept_grid


def main():
    """Demonstration"""
    minefield = Minefield(10, 10, 5)
    minefield.display()
    print()
    minefield.sweep()


if __name__ == "__main__":
    main()
