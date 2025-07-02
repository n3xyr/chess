class board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def fillBoard(self):
        '''
        Fills an empty board with pieces.
        '''
        for i in range(8):                                    # black pawns
            self.board[1][i] = pawn(i, 1, 'black')
        for i in range(8):                                    # white pawns
            self.board[6][i] = pawn(i, 6, 'white')

        for i in [0, 7]:                                      # black rooks
            self.board[0][i] = rook(i, 0, 'black')
        for i in [0, 7]:                                      # white rooks
            self.board[7][i] = rook(i, 7, 'white')

        for i in [1, 6]:                                      # black knights
            self.board[0][i] = knight(i, 0, 'black')
        for i in [1, 6]:                                      # white knights
            self.board[7][i] = knight(i, 0, 'white')

        for i in [2, 5]:                                      # black knights
            self.board[0][i] = bishop(i, 0, 'black')
        for i in [2, 5]:                                      # white knights
            self.board[7][i] = bishop(i, 0, 'white')

        self.board[0][3] = queen(3, 0, 'black')        # black queen
        self.board[7][3] = queen(3, 0, 'white')        # white queen

        self.board[0][4] = king(4, 0, 'black')         # black king
        self.board[7][4] = king(4, 0, 'white')         # white king

    def print(self):
        '''
        Shows the board.
        '''
        for i in range(8):
            line = []
            for j in range(8):
                if self.board[i][j] == None:
                    line.append('    ')
                else:
                    line.append(self.board[i][j].name)
            print(line)

class pawn:
    def __init__(self, coordX, coordY, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.name  = 'pawn'

    def getCoordX(self):
        """
        returns piece's x coordinate
        """
        return self.__coordinatesX
    
    def getCoordY(self):
        """
        returns piece's y coordinate
        """
        return self.__coordinatesY
    
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
        if self.getColor() == 'black' and self.getCoordY() == 6:
            return True
        if self.getColor() == 'white' and self.getCoordY() == 1:
            return True
        return False

    def availableMoves(self):
        """
        returns a list of coordinates where the piece could go
        """
        moves = []
        if self.isFirstMove():
            moves.append((self.getCoordX(), self.getCoordY() + 2))
        moves.append(self.getCoordX(), self.getCoordY() + 1)
        moves.append(self.getCoordX() + 1, self.getCoordY() + 1)
        moves.append(self.getCoordX() - 1, self.getCoordY() + 1)
        return moves

    def canMove(self, coordX, coordY):
        """
        returns True if the piece can move to the tile(coordX, coordY) False otherwise
        """
        moves = self.availableMoves()
        if not (coordX, coordY) in moves:
            return False

class knight:
    def __init__(self, coordX, coordY, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.name  = 'knight'

    def getCoordX(self):
        """
        returns piece's x coordinate
        """
        return self.__coordinatesX
    
    def getCoordY(self):
        """
        returns piece's y coordinate
        """
        return self.__coordinatesY
    
    def getColor(self):
        """
        returns piece's color
        """
        return self.__color

    def setCoordX(self, x):
        self.__coordinateX = x

    def setCoordY(self, y):
        self.__coordinateY = y


class rook:
    def __init__(self, coordX, coordY, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.name  = 'rook'

    def getCoordX(self):
        """
        returns piece's x coordinate
        """
        return self.__coordinatesX
    
    def getCoordY(self):
        """
        returns piece's y coordinate
        """
        return self.__coordinatesY
    
    def getColor(self):
        """
        returns piece's color
        """
        return self.__color

    def setCoordX(self, x):
        self.__coordinateX = x

    def setCoordY(self, y):
        self.__coordinateY = y
        

class bishop:
    def __init__(self, coordX, coordY, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.name  = 'bishop'

    def getCoordX(self):
        """
        returns piece's x coordinate
        """
        return self.__coordinatesX
    
    def getCoordY(self):
        """
        returns piece's y coordinate
        """
        return self.__coordinatesY
    
    def getColor(self):
        """
        returns piece's color
        """
        return self.__color

    def setCoordX(self, x):
        self.__coordinateX = x

    def setCoordY(self, y):
        self.__coordinateY = y


class queen:
    def __init__(self, coordX, coordY, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.name  = 'queen'

    def getCoordX(self):
        """
        returns piece's x coordinate
        """
        return self.__coordinatesX
    
    def getCoordY(self):
        """
        returns piece's y coordinate
        """
        return self.__coordinatesY
    
    def getColor(self):
        """
        returns piece's color
        """
        return self.__color

    def setCoordX(self, x):
        self.__coordinateX = x

    def setCoordY(self, y):
        self.__coordinateY = y


class king:
    def __init__(self, coordX, coordY, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.name  = 'king'

    def getCoordX(self):
        """
        returns piece's x coordinate
        """
        return self.__coordinatesX
    
    def getCoordY(self):
        """
        returns piece's y coordinate
        """
        return self.__coordinatesY
    
    def getColor(self):
        """
        returns piece's color
        """
        return self.__color

    def setCoordX(self, x):
        self.__coordinateX = x

    def setCoordY(self, y):
        self.__coordinateY = y

test = board()
test.fillBoard()
test.print()
