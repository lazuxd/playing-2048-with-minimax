from Grid import Grid
from GameDriver import GameDriver
from minimax import getBestMove

gameDriver = GameDriver()
moves_str = ['UP', 'DOWN', 'LEFT', 'RIGHT']
moves_count = 1

while True:
    grid = gameDriver.getGrid()
    if grid.isGameOver():
        print("Unfortunately, I lost the game.")
        break
    moveCode = getBestMove(grid, 5)
    print(f'Move #{moves_count}: {moves_str[moveCode]}')
    gameDriver.move(moveCode)
    moves_count += 1