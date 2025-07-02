class pawn:
    def __init__(self, coordX, coordY, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color

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


class knight:
    def __init__(self, coordX, coordY, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color

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