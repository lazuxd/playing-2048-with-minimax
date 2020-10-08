from copy import deepcopy
from typing import Tuple, List

class Grid:
    
    def __init__(self, matrix):
        self.setMatrix(matrix)
    
    def __eq__(self, other) -> bool:
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True
    
    def setMatrix(self, matrix):
        self.matrix = deepcopy(matrix)
    
    def getMatrix(self) -> List[List]:
        return deepcopy(self.matrix)
    
    def placeTile(self, row: int, col: int, tile: int):
        self.matrix[row-1][col-1] = tile
    
    def utility(self) -> int:
        count = 0
        sum = 0
        for i in range(4):
            for j in range(4):
                sum += self.matrix[i][j]
                if self.matrix[i][j] != 0:
                    count += 1
        return int(sum/count)
    
    def canMoveUp(self) -> bool:
        for j in range(4):
            k = -1
            for i in range(3, -1, -1):
                if self.matrix[i][j] > 0:
                    k = i
                    break
            if k > -1:
                for i in range(k, 0, -1):
                    if self.matrix[i-1][j] == 0 or self.matrix[i][j] == self.matrix[i-1][j]:
                        return True
        return False

    def canMoveDown(self) -> bool:
        for j in range(4):
            k = -1
            for i in range(4):
                if self.matrix[i][j] > 0:
                    k = i
                    break
            if k > -1:
                for i in range(k, 3):
                    if self.matrix[i+1][j] == 0 or self.matrix[i][j] == self.matrix[i+1][j]:
                        return True
        return False

    def canMoveLeft(self) -> bool:
        for i in range(4):
            k = -1
            for j in range(3, -1, -1):
                if self.matrix[i][j] > 0:
                    k = j
                    break
            if k > -1:
                for j in range(k, 0, -1):
                    if self.matrix[i][j-1] == 0 or self.matrix[i][j] == self.matrix[i][j-1]:
                        return True
        return False

    def canMoveRight(self) -> bool:
        for i in range(4):
            k = -1
            for j in range(4):
                if self.matrix[i][j] > 0:
                    k = j
                    break
            if k > -1:
                for j in range(k, 3):
                    if self.matrix[i][j+1] == 0 or self.matrix[i][j] == self.matrix[i][j+1]:
                        return True
        return False
    
    def getAvailableMovesForMax(self) -> List[int]:
        moves = []

        if self.canMoveUp():
            moves.append(0)
        if self.canMoveDown():
            moves.append(1)
        if self.canMoveLeft():
            moves.append(2)
        if self.canMoveRight():
            moves.append(3)
        
        return moves
    
    def getAvailableMovesForMin(self) -> List[Tuple[int]]:
        places = []
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    places.append((i+1, j+1, 2))
                    places.append((i+1, j+1, 4))
        return places
    
    def getChildren(self, who: str) -> List:
        if who == "max":
            return self.getAvailableMovesForMax()
        elif who == "min":
            return self.getAvailableMovesForMin()
    
    def isTerminal(self, who: str) -> bool:
        if who == "max":
            if self.canMoveUp():
                return False
            if self.canMoveDown():
                return False
            if self.canMoveLeft():
                return False
            if self.canMoveRight():
                return False
            return True
        elif who == "min":
            for i in range(4):
                for j in range(4):
                    if self.matrix[i][j] == 0:
                        return False
            return True
    
    def isGameOver(self) -> bool:
        return self.isTerminal(who="max")
    
    def up(self):
        for j in range(4):
            w = 0
            k = 0
            for i in range(4):
                if self.matrix[i][j] == 0:
                    continue
                if k == 0:
                    k = self.matrix[i][j]
                elif k == self.matrix[i][j]:
                    self.matrix[w][j] = 2*k
                    w += 1
                    k = 0
                else:
                    self.matrix[w][j] = k
                    w += 1
                    k = self.matrix[i][j]
            if k != 0:
                self.matrix[w][j] = k
                w += 1
            for i in range(w, 4):
                self.matrix[i][j] = 0
    
    def down(self):
        for j in range(4):
            w = 3
            k = 0
            for i in range(3, -1, -1):
                if self.matrix[i][j] == 0:
                    continue
                if k == 0:
                    k = self.matrix[i][j]
                elif k == self.matrix[i][j]:
                    self.matrix[w][j] = 2*k
                    w -= 1
                    k = 0
                else:
                    self.matrix[w][j] = k
                    w -= 1
                    k = self.matrix[i][j]
            if k != 0:
                self.matrix[w][j] = k
                w -= 1
            for i in range(w+1):
                self.matrix[i][j] = 0
    
    def left(self):
        for i in range(4):
            w = 0
            k = 0
            for j in range(4):
                if self.matrix[i][j] == 0:
                    continue
                if k == 0:
                    k = self.matrix[i][j]
                elif k == self.matrix[i][j]:
                    self.matrix[i][w] = 2*k
                    w += 1
                    k = 0
                else:
                    self.matrix[i][w] = k
                    w += 1
                    k = self.matrix[i][j]
            if k != 0:
                self.matrix[i][w] = k
                w += 1
            for j in range(w, 4):
                self.matrix[i][j] = 0
    
    def right(self):
        for i in range(4):
            w = 3
            k = 0
            for j in range(3, -1, -1):
                if self.matrix[i][j] == 0:
                    continue
                if k == 0:
                    k = self.matrix[i][j]
                elif k == self.matrix[i][j]:
                    self.matrix[i][w] = 2*k
                    w -= 1
                    k = 0
                else:
                    self.matrix[i][w] = k
                    w -= 1
                    k = self.matrix[i][j]
            if k != 0:
                self.matrix[i][w] = k
                w -= 1
            for j in range(w+1):
                self.matrix[i][j] = 0
    
    def move(self, mv: int) -> None:
        if mv == 0:
            self.up()
        elif mv == 1:
            self.down()
        elif mv == 2:
            self.left()
        else:
            self.right()
    
    def getMoveTo(self, child: 'Grid') -> int:
        if self.canMoveUp():
            g = Grid(matrix=self.getMatrix())
            g.up()
            if g == child:
                return 0
        if self.canMoveDown():
            g = Grid(matrix=self.getMatrix())
            g.down()
            if g == child:
                return 1
        if self.canMoveLeft():
            g = Grid(matrix=self.getMatrix())
            g.left()
            if g == child:
                return 2
        return 3