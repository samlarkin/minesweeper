# minesweeper

Work in progress. This is a partial implementation of the game minesweeper in
Python (using only built in functionality of Python3).

At the moment, it just sets up the board (generating a random state using the
`random` module) and works out the score that each position has (i.e. how
many mines' is it adjacent to vertically, horizontally, or diagonally) and
which should be displayed when a player selects that position.

The dimensions of the board can be adjusted at will, as can the frequency of
mines.

## Example output

```
- - # - - - - - - -
- - - - - # - # - -
- # - - - - - - # #
- # - - - - - - - -
- - # - - # - - # -
- - # # - - - - - -
- # - - - - - - - -
- # - - - # - - - -
- - - - - - - # - -
- # - - # - - - - -

0 1 # 1 1 1 2 1 1 0
1 2 2 1 1 # 2 # 3 2
2 # 2 0 1 1 2 2 # #
2 # 3 1 1 1 1 2 3 3
1 3 # 3 2 # 1 1 # 1
1 3 # # 2 1 1 1 1 1
2 # 4 2 2 1 1 0 0 0
2 # 2 0 1 # 2 1 1 0
2 2 2 1 2 2 2 # 1 0
1 # 1 1 # 1 1 1 1 0
```

## To Do

* [ ] Implement a playable game of minesweeper
