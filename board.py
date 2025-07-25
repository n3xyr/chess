import pieces
import pygame
import time

pygame.mixer.init()
moveSound = pygame.mixer.Sound('soundEffects/moveSound.wav')
eatSound = pygame.mixer.Sound('soundEffects/eatSound.wav')

class board:
    def __init__(self):
        self.matrix = [[None for _ in range(8)] for _ in range(8)]
        self.turn = 'white'


    def switchTurn(self):
        if self.turn == 'white':
            self.turn = 'black'
        else:
            self.turn = 'white'
        

    def fillBoard(self):
        '''
        Fills an empty board with pieces.
        '''
        for i in range(8):                                            # black pawns
            self.matrix[1][i] = pieces.pawn(1, i, 'black')
        for i in range(8):                                            # white pawns
            self.matrix[6][i] = pieces.pawn(6, i, 'white')

        for i in [0, 7]:                                              # black rooks
            self.matrix[0][i] = pieces.rook(0, i, 'black')
        for i in [0, 7]:                                              # white rooks
            self.matrix[7][i] = pieces.rook(7, i, 'white')

        for i in [1, 6]:                                              # black knights
            self.matrix[0][i] = pieces.knight(0, i, 'black')
        for i in [1, 6]:                                              # white knights
            self.matrix[7][i] = pieces.knight(7, i, 'white')

        for i in [2, 5]:                                              # black bishops
            self.matrix[0][i] = pieces.bishop(0, i, 'black')
        for i in [2, 5]:                                              # white bishops
            self.matrix[7][i] = pieces.bishop(7, i, 'white')


        self.bq = pieces.queen(0, 3, 'black')  
        self.wq = pieces.queen(7, 3, 'white')  
        self.matrix[0][3] = self.bq                                        # black queen
        self.matrix[7][3] = self.wq                                        # white queen


        self.bk = pieces.king(0, 4, 'black')
        self.wk = pieces.king(7, 4, 'white')
        self.matrix[0][4] = self.bk                                        # black king
        self.matrix[7][4] = self.wk                                        # white king


    def getAvailableMoves(self, selectedTile):
        if selectedTile == None:
            return []
        if selectedTile.getColor() == self.turn:
           return selectedTile.possibleMoves(self)
        return []


    def movePiece(self, piece, y, x):

        target = self.matrix[y][x]
        self.matrix[y][x] = piece
        self.matrix[piece.getCoordY()][piece.getCoordX()] = None

        piece.setCoordY(y)
        piece.setCoordX(x)

        if self.turn == 'white':
            oponentKing = self.bk
        else:
            oponentKing = self.wk

        if self.isChecking(piece, oponentKing):
            oponentKing.checked = True

        self.switchTurn()

        if target != None:
            if target.getColor() != piece.getColor():
                eatSound.play()
                return 'x'
        moveSound.play()
        return ''
    
    
    def isChecking(self, pieceChecking, pieceChecked):
        return pieceChecking.canMove((pieceChecked.getCoordY(), pieceChecked.getCoordX()), self)


    def promote(self, piece, newPieceName):
        coordX = piece.getCoordX()
        coordY = piece.getCoordY()
        color = piece.getColor()
        self.matrix[piece.getCoordY()][piece.getCoordX()] = None
        if newPieceName == 'queen':
            self.matrix[coordY][coordX] = pieces.queen(coordY, coordX, color)
        elif newPieceName == 'knight':
            self.matrix[coordY][coordX] = pieces.knight(coordY, coordX, color)
        elif newPieceName == 'rook':
            self.matrix[coordY][coordX] = pieces.rook(coordY, coordX, color)
        elif newPieceName == 'bishop':
            self.matrix[coordY][coordX] = pieces.bishop(coordY, coordX, color)


    def initClock(self):
        initialTime = time.time()
        lastTime = initialTime
        return initialTime, lastTime


    def getClock(self, initialTime):
        currentTime = time.time()
        return int(currentTime - initialTime)
    

displayedBoard = board()
displayedBoard.fillBoard()