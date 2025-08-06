class pawn:
    def __init__(self, coordY, coordX, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.rectX = 0
        self.rectX = 0
        self.name  = ''
        self.value = 1

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
    
    def getName(self):
        """
        returns piece's name
        """
        return self.name

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


    def canMove(self, y, x, board, checkNext = True):
        """
        returns True if the piece can move to the tile(x, y) False otherwise
        """

        if self.getColor() == 'black':
            direction = 1
            king =  board.bk
        else:
            direction = -1
            king = board.wk
        
        coordX = self.getCoordX()
        coordY = self.getCoordY()
        moves = [(coordY + direction, coordX + 1), (coordY + direction, coordX - 1), (coordY + direction, coordX), (coordY + 2*direction, coordX)]

        if not ((y, x) in moves) or (x < 0) or (x > 7) or (y < 0) or (y > 7):
            return False
        
        if checkNext:
            if board.nextMoveIsCheck(self, y, x):
                return False
        
        if board.matrix[y][x]:
            if board.matrix[y][x].getColor() == self.getColor():
                return False
        
            elif (y, x) in moves[:2]:
                return True
        
        else:
            if (y, x) == moves[2]:    # Goes forwards by one
                return True
            
            elif (y, x) == moves[3] and self.isFirstMove() and board.matrix[coordY + direction][coordX] is None:   # Goes forward by two
                return True
            return False
        
        return False
          
    def possibleMoves(self, board):
        """
        returns a list of coordinates (y, x) corresponding to the available moves 
        """
        coordX = self.getCoordX()
        coordY = self.getCoordY()
        
        if self.getColor() == 'black':
            direction = 1
        else:
            direction = -1
        
        pieceMoves = [(coordY + direction, coordX + 1), (coordY + direction, coordX - 1), (coordY + direction, coordX), (coordY + 2 * direction, coordX)]
        return [move for move in pieceMoves if self.canMove(move[0], move[1], board)]
    

    def isAbleToPromote(self):
        color = self.getColor()
        coordY = self.getCoordY()
        if color == 'white':
            if coordY == 0:
                return True
            else:
                return False
        else:
            if coordY == 7:
                return True
            else:
                return False


class knight:
    def __init__(self, coordY, coordX, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.rectX = 0
        self.rectY = 0
        self.name  = 'N'
        self.value = 3

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
    
    def getName(self):
        """
        returns piece's name
        """
        return self.name

    def setCoordX(self, x):
        self.__coordinateX = x

    def setCoordY(self, y):
        self.__coordinateY = y

    def canMove(self, y, x, board, checkNext = True):
        """
        returns True if the piece can move to the tile(x, y) False otherwise
        """
        if self.getColor() == 'white':
            king = board.wk
        else:
            king =  board.bk

        coordX = self.getCoordX()
        coordY = self.getCoordY()
        color = self.getColor()
        moves = [(coordY + 2, coordX + 1), (coordY + 2, coordX - 1), (coordY + 1, coordX + 2), (coordY - 1, coordX + 2), (coordY + 1, coordX - 2), (coordY - 1, coordX - 2), (coordY - 2, coordX + 1), (coordY - 2, coordX - 1)]

        if (y, x) in moves and 0 <= x <= 7 and 0 <= y <= 7:
            if checkNext:
                if board.nextMoveIsCheck(self, y, x):
                    return False
                
            if board.matrix[y][x] == None or board.matrix[y][x].getColor() != color:
                return True
                        
        return False

    def possibleMoves(self, board):
        """
        returns a list of coordinates corresponding to the available moves
        """
        coordX = self.getCoordX()
        coordY = self.getCoordY()

        pieceMoves = [(coordY + 2, coordX + 1), (coordY + 2, coordX - 1), (coordY + 1, coordX + 2), (coordY - 1, coordX + 2), (coordY + 1, coordX - 2), (coordY - 1, coordX - 2), (coordY - 2, coordX + 1), (coordY - 2, coordX - 1)]
        return [move for move in pieceMoves if self.canMove(move[0], move[1], board)]


class rook:
    def __init__(self, coordY, coordX, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.rectX = 0
        self.rectY = 0
        self.name  = 'R'
        self.value = 5

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
    
    def getName(self):
        """
        returns piece's name
        """
        return self.name

    def setCoordX(self, x):
        self.__coordinateX = x

    def setCoordY(self, y):
        self.__coordinateY = y
    
    def canMove(self, y, x, board, checkNext = True):
        """
        returns True if the piece can move to the tile(x, y) False otherwise
        """
        if self.getColor() == 'white':
            king = board.wk
        else:
            king =  board.bk

        coordX = self.getCoordX()
        coordY = self.getCoordY()
        color = self.getColor()
        
        if checkNext:
            if board.nextMoveIsCheck(self, y, x):
                return False
        
        if board.matrix[y][x] == None or board.matrix[y][x].getColor() != color:
            if x == coordX and (y != coordY and (y <= 7 and y >= 0)):
                directionY = int((y - coordY)/abs(y - coordY))  # Y vector
                
                for i in range(1, abs(coordY - y)):
                    if board.matrix[coordY + i * directionY][coordX] != None:
                        return False
                return True
            
            elif (x != coordX and (x <= 7 and x >= 0)) and y == coordY:
                directionX = int((x - coordX)/abs(x - coordX))  # X vector
                
                for i in range(1, abs(coordX - x)):
                    if board.matrix[coordY][coordX + i * directionX] != None:
                        return False
                return True
        
        else:
            return False
    
    def possibleMoves(self, board):
        """
        returns a list of coordinates corresponding to the available moves
        """
        if self.getColor() == 'white':
            king = board.wk
        else:
            king =  board.bk

        coordX = self.getCoordX()
        coordY = self.getCoordY()
        pieceMoves = []
        
        for i in range(8):
            pieceMoves.append((i, coordX))
            pieceMoves.append((coordY, i))
        
        return [move for move in pieceMoves if self.canMove(move[0], move[1], board)]

    def pathToKing(self, board):
        """
        return a list of tiles between the rook and the opposit king if it puts the king in check
        """
        if self.getColor() == 'white':
            king = board.wk
        else:
            king =  board.bk

        kX = king.getCoordX()
        kY = king.getCoordY()
        rX = self.getCoordX()
        rY = self.getCoordY()

        tiles = [(rY, rX)]

        if self.canMove(kY, kX, board):
            dX = abs(kX - rX)
            dY = abs(kY - rY)
            
            if dY == 0:
                for move in self.possibleMoves(board):
                    piece = board.matrix[move[0]][move[1]]
                    pX = abs(kX - piece.getCoordX())

                    if pX < dX:
                        tiles.append((piece.getCoordY(), piece.getCoordX()))
            else:
                for move in self.possibleMoves(board):
                    piece = board.matrix[move[0]][move[1]]
                    pY = abs(kY - piece.getCoordY())

                    if pY < dY:
                        tiles.append((piece.getCoordY(), piece.getCoordX()))


        return tiles


class bishop:
    def __init__(self, coordY, coordX, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.rectX = 0
        self.rectY = 0
        self.name  = 'B'
        self.value = 3

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

    def getName(self):
        """
        returns piece's name
        """
        return self.name

    def setCoordX(self, x):
        self.__coordinateX = x

    def setCoordY(self, y):
        self.__coordinateY = y

    def canMove(self, y, x, board, checkNext = True):
        """
        returns True if the piece can move to the tile(x, y) False otherwise
        """
        if self.getColor() == 'white':
            king = board.wk
        else:
            king =  board.bk

        coordX = self.getCoordX()
        coordY = self.getCoordY()
        
        if checkNext:
            if board.nextMoveIsCheck(self, y, x):
                return False
        
        if x < 0 or x > 7 or y < 0 or y > 7 or (coordX-x)**2 != (coordY-y)**2 or (x == coordX and y == coordY):  #if it isn't in the board or if it doesn't move in a diagonal
            return False
        
        directionX = int((x - coordX)/abs(x - coordX))  # X vector
        directionY = int((y - coordY)/abs(y - coordY))  # Y vector
        
        for i in range(1, abs(coordX - x)):
            if board.matrix[coordY + i*directionY][coordX + i*directionX] != None: # If there's a piece on the diagonal
                return False
            
        if board.matrix[y][x] != None:
            if board.matrix[y][x].getColor() == self.getColor():   # If the color of the piece on the targeted tile is the same as the moved piece
                return False
            
        return True
    
    def possibleMoves(self, board):
        """
        returns a list of coordinates corresponding to the available moves
        """
        coordX = self.getCoordX()
        coordY = self.getCoordY()
        pieceMoves = []
        
        for i in range(64):
            y = i // 8
            x = i % 8
            
            if (coordX-x)**2 == (coordY-y)**2:
                pieceMoves.append((y, x))
        
        return [move for move in pieceMoves if self.canMove(move[0], move[1], board)]

    def pathToKing(self, board):
        """
        return a list of tiles between the bishop and the opposit king if it puts the king in check
        """
        if self.getColor() == 'white':
            king = board.wk
        else:
            king =  board.bk

        kX = king.getCoordX()
        kY = king.getCoordY()
        bX = self.getCoordX()
        bY = self.getCoordY()

        tiles = [(bY, bX)]

        if self.canMove(kY, kX, board):
            dX = abs(kX - bX)
            dY = abs(kY - bY)

            for move in self.possibleMoves(board):
                piece = board.matrix[move[0]][move[1]]
                pX = abs(kX - piece.getCoordX())
                pY = abs(kY - piece.getCoordY())

                if pX < dX and pY < dY:
                    tiles.append((piece.getCoordY(), piece.getCoordX()))

        return tiles


class queen:
    def __init__(self, coordY, coordX, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.rectX = 0
        self.rectY = 0
        self.name  = 'Q'
        self.value = 9

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
    
    def getName(self):
        """
        returns piece's name
        """
        return self.name

    def setCoordX(self, x):
        self.__coordinateX = x

    def setCoordY(self, y):
        self.__coordinateY = y
        
    def canMove(self, y, x, board, checkNext = True):
        """
        returns True if the piece can move to the tile(x, y) False otherwise
        """
        if self.getColor() == 'white':
            king = board.wk
        else:
            king =  board.bk

        coordX = self.getCoordX()
        coordY = self.getCoordY()
                
        if checkNext:
            if board.nextMoveIsCheck(self, y, x):
                return False
        
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
                if board.matrix[coordY + i*directionY][coordX + i*directionX] != None: #if there's a piece on the diagonal
                    return False
            
            if board.matrix[y][x] != None:
                if board.matrix[y][x].getColor() == self.getColor():   # If the color of the piece on the targeted tile is the same as the moved piece
                    return False
            
            return True
        
        # rook part
        color = self.getColor()
        
        if board.matrix[y][x] == None or board.matrix[y][x].getColor() != color:
            if x == coordX and (y != coordY and (y <= 7 and y >= 0)):
                directionY = int((y - coordY)/abs(y - coordY))  # Y vector
                
                for i in range(1, abs(coordY - y)):
                    if board.matrix[coordY + i * directionY][coordX] != None:
                        return False
                return True
            
            elif (x != coordX and (x <= 7 and x >= 0)) and y == coordY:
                directionX = int((x - coordX)/abs(x - coordX))  # X vector
                
                for i in range(1, abs(coordX - x)):
                    if board.matrix[coordY][coordX + i * directionX] != None:
                        return False
                
                return True
            
            else:
                False
        
        else:
            return False     

    def possibleMoves(self, board):
        """
        returns a list of coordinates corresponding to the available moves
        """
        coordX = self.getCoordX()
        coordY = self.getCoordY()
        pieceMoves = []

        # bishop part
        for i in range(64):
            y = i // 8
            x = i % 8
            if (coordX-x)**2 == (coordY-y)**2:
                pieceMoves.append((y, x))

        # rook part
        for i in range(8):
            pieceMoves.append((i, coordX))
            pieceMoves.append((coordY, i))

        return [move for move in pieceMoves if self.canMove(move[0], move[1], board)]
        

    def pathToKing(self, board):
        """
        return a list of tiles between the queen and the opposit king if it puts the king in check
        """
        if self.getColor() == 'white':
            king = board.wk
        else:
            king =  board.bk

        kX = king.getCoordX()
        kY = king.getCoordY()
        qX = self.getCoordX()
        qY = self.getCoordY()

        tiles = [(qY, qX)]

        if self.canMove(kY, kX, board):
            dX = abs(kX - qX)
            dY = abs(kY - qY)

            if ((kX-qX)**2 != (kY-qY)**2):  # Bishop-like path

                for move in self.possibleMoves(board):
                    piece = board.matrix[move[0]][move[1]]
                    pX = abs(kX - piece.getCoordX())
                    pY = abs(kY - piece.getCoordY())

                    if pX < dX and pY < dY:
                        tiles.append((piece.getCoordY(), piece.getCoordX()))

            else:   # Rook-like path

                if dY == 0:
                    for move in self.possibleMoves(board):
                        piece = board.matrix[move[0]][move[1]]
                        pX = abs(kX - piece.getCoordX())

                        if pX < dX:
                            tiles.append((piece.getCoordY(), piece.getCoordX()))
                else:
                    for move in self.possibleMoves(board):
                        piece = board.matrix[move[0]][move[1]]
                        pY = abs(kY - piece.getCoordY())

                        if pY < dY:
                            tiles.append((piece.getCoordY(), piece.getCoordX()))

        return tiles


class king:
    def __init__(self, coordY, coordX, color):
        self.__coordinateX = coordX
        self.__coordinateY = coordY 
        self.__color = color
        self.rectX = 0
        self.rectY = 0
        self.name  = 'K'
        self.value = 0

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
    
    def getName(self):
        """
        returns piece's name
        """
        return self.name

    def setCoordX(self, x):
        self.__coordinateX = x

    def setCoordY(self, y):
        self.__coordinateY = y

    def canMove(self, y, x, board, checkNext = True):
        """
        returns True if the piece can move to the tile(x, y) False otherwise
        """
        if self.getColor() == 'white':
            king = board.wk
        else:
            king =  board.bk

        coordX = self.getCoordX()
        coordY = self.getCoordY()
        color = self.getColor()
        moves = [(coordY + 1, coordX + 1), (coordY, coordX + 1), (coordY - 1, coordX + 1), (coordY + 1, coordX), (coordY - 1, coordX), (coordY + 1, coordX - 1), (coordY, coordX - 1), (coordY - 1, coordX - 1)]
            
        if (y, x) in moves and not (x < 0) and not (x > 7) and not (y < 0) and not (y > 7): 
            if checkNext:
                if board.nextMoveIsCheck(self, y, x):
                    return False
            if board.matrix[y][x] == None or board.matrix[y][x].getColor() != color:
                return True
            
        return False
        
    def possibleMoves(self, board):
        """
        returns a list of coordinates corresponding to the available moves
        """
        coordX = self.getCoordX()
        coordY = self.getCoordY()

        pieceMoves = [(coordY + 1, coordX + 1), (coordY, coordX + 1), (coordY - 1, coordX + 1), (coordY + 1, coordX), (coordY - 1, coordX), (coordY + 1, coordX - 1), (coordY, coordX - 1), (coordY - 1, coordX - 1)]
        
        return [move for move in pieceMoves if self.canMove(move[0], move[1], board)]

    def isChecked(self, board, checkNext = True):
        """
        Returns True if the king is in check, False otherwise.
        """
        for i in range(8):
            for j in range(8):
                piece = board.matrix[i][j]
                if piece is not None and piece.getColor() != self.getColor():
                    if piece.canMove(self.getCoordY(), self.getCoordX(), board, checkNext):
                        return True
        return False