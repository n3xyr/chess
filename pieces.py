class pawn:
    def __init__(self, coordY, coordX, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.name  = 'pawn'

    def getCoordX(self):
        """
        returns piece's x coordinate
        """
        return self.__coordinateX
    
    def getCoordY(self):
        """
        returns piece's y coordinate
        """
        return self.__coordinateY
    
    def getColor(self):
        """
        returns piece's color
        """
        return self.__color

    def setCoordX(self, x):
        self.__coordinateX = x

    def setCoordY(self, y):
        self.__coordinateY = y

    def isFirstMove(self):
        """
        returns True if the pawn hasn't moved yet False otherwise
        """
        if self.getColor() == 'black' and self.getCoordY() == 1:
            return True
        if self.getColor() == 'white' and self.getCoordY() == 6:
            return True
        return False


    def canMove(self, y, x, board):
        """
        returns True if the piece can move to the tile(x, y) False otherwise
        """
        coordX = self.getCoordX()
        coordY = self.getCoordY()
        if self.getColor() == 'black':
            direction = 1
        else:
            direction = -1
        moves = [(coordY + direction, coordX + 1), (coordY + direction, coordX - 1), (coordY + direction, coordX), (coordY + 2*direction, coordX)]
        if not ((y, x) in moves) or (x < 0) or (x > 7) or (y < 0) or (y > 7):
            return False
        if board[y][x] is None:
            if (y, x) in moves[:2]:
                return False
            elif (y, x) == moves[2]:
                return True
            elif (y, x) == moves[3] and self.isFirstMove() and board[coordY + direction][coordX] is None:
                return True
        if (y, x) in moves[:2]:
            return True
        if (y, x) == moves[3]:
            return False
        if (y, x) == moves[2]:
            return False
                
class knight:
    def __init__(self, coordY, coordX, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.name  = 'knight'

    def getCoordX(self):
        """
        returns piece's x coordinate
        """
        return self.__coordinateX
    
    def getCoordY(self):
        """
        returns piece's y coordinate
        """
        return self.__coordinateY
    
    def getColor(self):
        """
        returns piece's color
        """
        return self.__color

    def setCoordX(self, x):
        self.__coordinateX = x

    def setCoordY(self, y):
        self.__coordinateY = y

    def canMove(self, y, x, board):
        """
        returns True if the piece can move to the tile(x, y) False otherwise
        """
        coordX = self.getCoordX()
        coordY = self.getCoordY()
        color = self.getColor()
        moves = [(coordX + 1, coordY + 2), (coordX + 2, coordY + 1), (coordX - 1, coordY + 2), (coordX - 2, coordY + 1), (coordX + 1, coordY - 2),(coordX + 2, coordY - 1), (coordX - 1, coordY - 2), (coordX - 2, coordY - 1)]
        if (x, y) in moves and not (x < 0) or (x > 7) or (y < 0) or (y > 7):
            if board[y][x] == None or board[y][x].getColor() != color:
                return True
            else:
                return False
        else:
            return False

class rook:
    def __init__(self, coordY, coordX, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.name  = 'rook'

    def getCoordX(self):
        """
        returns piece's x coordinate
        """
        return self.__coordinateX
    
    def getCoordY(self):
        """
        returns piece's y coordinate
        """
        return self.__coordinateY
    
    def getColor(self):
        """
        returns piece's color
        """
        return self.__color

    def setCoordX(self, x):
        self.__coordinateX = x

    def setCoordY(self, y):
        self.__coordinateY = y
    
    def canMove(self, y, x, board):
        """
        returns True if the piece can move to the tile(x, y) False otherwise
        """
        coordX = self.getCoordX()
        coordY = self.getCoordY()
        color = self.getColor()
        if board[y][x] == None or board[y][x].getColor() != color:
            if x == coordX and (y != coordY and (y <= 7 and y >= 0)):
                for i in range(1, abs(coordY - y)):
                    if board[coordY + i][coordX] != None:
                        return False
                return True
            elif (x != coordX and (x <= 7 and x >= 0)) and y == coordY:
                for i in range(1, abs(coordX - x)):
                    if board[coordY][coordX + i] != None:
                        return False
                return True
        else:
            return False

class bishop:
    def __init__(self, coordY, coordX, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.name  = 'bishop'

    def getCoordX(self):
        """
        returns piece's x coordinate
        """
        return self.__coordinateX
    
    def getCoordY(self):
        """
        returns piece's y coordinate
        """
        return self.__coordinateY
    
    def getColor(self):
        """
        returns piece's color
        """
        return self.__color

    def setCoordX(self, x):
        self.__coordinateX = x

    def setCoordY(self, y):
        self.__coordinateY = y

    def canMove(self, y, x, board):
        """
        returns True if the piece can move to the tile(x, y) False otherwise
        """
        coordX = self.getCoordX()
        coordY = self.getCoordY()
        if x < 0 or x > 7 or y < 0 or y > 7 or (coordX-x)**2 != (coordY-y)**2 or x == coordX or y == coordY:  #if it isn't in the board or if it doesn't move in a diagonal
            return False
        directionX = int((x - coordX)/abs(x - coordX))  # X vector
        directionY = int((y - coordY)/abs(y - coordY))  # Y vector

        for i in range(1, abs(coordX - x)):
            if board[coordY + i*directionY][coordX + i*directionX] != None: #if there's a piece on the diagonal
                return False
            
        if board[x][y] != None:
            if board[x][y].getColor() == self.getColor():   # If the color of the piece on the targeted tile is the same as the moved piece
                return False
            
        return True

class queen:
    def __init__(self, coordY, coordX, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.name  = 'queen'

    def getCoordX(self):
        """
        returns piece's x coordinate
        """
        return self.__coordinateX
    
    def getCoordY(self):
        """
        returns piece's y coordinate
        """
        return self.__coordinateY
    
    def getColor(self):
        """
        returns piece's color
        """
        return self.__color

    def setCoordX(self, x):
        self.__coordinateX = x

    def setCoordY(self, y):
        self.__coordinateY = y
        
    def canMove(self, y, x, board):
        """
        returns True if the piece can move to the tile(x, y) False otherwise
        """
        coordX = self.getCoordX()
        coordY = self.getCoordY()
        if x < 0 or x > 7 or y < 0 or y > 7:  #if it isn't in the board or if it doesn't move in a diagonal nor in a straight line
            return False
        
        if ((coordX-x)**2 != (coordY-y)**2) and not(x == coordX and (y != coordY )) and not((x != coordX) and y == coordY):
            return False

        # bishop part
        if (coordX-x)**2 == (coordY-y)**2:
            if x == coordX or y == coordY:
                return False
            directionX = int((x - coordX)/abs(x - coordX))  # X vector
            directionY = int((y - coordY)/abs(y - coordY))  # Y vector
            for i in range(1, abs(coordX - x)):
                if board[coordY + i*directionY][coordX + i*directionX] != None: #if there's a piece on the diagonal
                    return False
            return True
        
        # rook part
        color = self.getColor()
        if board[y][x] == None or board[y][x].getColor() != color:
            if x == coordX and (y != coordY and (y <= 7 and y >= 0)):
                for i in range(1, abs(coordY - y)):
                    if board[coordY + i][coordX] != None:
                        return False
                return True
            elif (x != coordX and (x <= 7 and x >= 0)) and y == coordY:
                for i in range(1, abs(coordX - x)):
                    if board[coordY][coordX + i] != None:
                        return False
                return True
            else:
                False
        else:
            return False     

class king:
    def __init__(self, coordY, coordX, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.name  = 'king'

    def getCoordX(self):
        """
        returns piece's x coordinate
        """
        return self.__coordinateX
    
    def getCoordY(self):
        """
        returns piece's y coordinate
        """
        return self.__coordinateY
    
    def getColor(self):
        """
        returns piece's color
        """
        return self.__color

    def setCoordX(self, x):
        self.__coordinateX = x

    def setCoordY(self, y):
        self.__coordinateY = y

    def canMove(self, y, x, board):
        """
        returns True if the piece can move to the tile(x, y) False otherwise
        """
        coordX = self.getCoordX()
        coordY = self.getCoordY()
        color = self.getColor()
        moves = [(coordX + 1, coordY + 1), (coordX + 1, coordY), (coordX, coordY + 1), (coordX + 1, coordY - 1), (coordX - 1, coordY + 1), (coordX - 1, coordY - 1), (coordX - 1, coordY), (coordX, coordY - 1)]
        if (x, y) in moves and not (x < 0) or (x > 7) or (y < 0) or (y > 7):
            if board[y][x] == None or board[y][x].getColor() != color:
                return True
            else:
                return False
        else:
            return False