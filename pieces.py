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


    def canMove(self, x, y, board):
        """
        returns True if the piece can move to the tile(coordX, coordY) False otherwise
        """
        coordX = self.getCoordX()
        coordY = self.getCoordY()
        moves = [(coordX + 1, coordY + 1), (coordX - 1, coordY - 1), (coordX, coordY + 1), (coordX, coordY + 2)]
        if not (x, y) in moves:
            return False
        if not(board.matrice[x][y] is None):
            if (x,y) in moves[:2]:
                return True
            else:
                return False
        if (x, y) == moves[-1] and self.isFirstMove():
            return True
        else:
            False
                
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
