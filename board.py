import pieces
import pygame
import time
import copy

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
        self.matrix[0][3] = self.bq                                   # black queen
        self.matrix[7][3] = self.wq                                   # white queen


        self.bk = pieces.king(0, 4, 'black')
        self.wk = pieces.king(7, 4, 'white')
        self.matrix[0][4] = self.bk                                   # black king
        self.matrix[7][4] = self.wk                                   # white king


    def getAvailableMoves(self, selectedTile):
        if selectedTile == None:
            return []
        if selectedTile.getColor() == self.turn:
           return selectedTile.possibleMoves(self)
        return []


    def manageMove(self, selectedTile, mouseYTab, mouseXTab, clickedTile, moveList, promotingPawn):
        if selectedTile:
            if selectedTile.canMove(mouseYTab, mouseXTab, self) and selectedTile.getColor() == self.turn:
                act = self.movePiece(selectedTile, mouseYTab, mouseXTab)
                if self.matrix[mouseYTab][mouseXTab] is not None:
                    movedPiece = self.matrix[mouseYTab][mouseXTab]

                if movedPiece.name == 'P' and movedPiece.isAbleToPromote():
                    promotingPawn = movedPiece
                selectedTile = None
                moveList.append(
                    movedPiece.getName() + act + chr(97 + mouseXTab) + str(8 - mouseYTab)
                )
                return selectedTile, promotingPawn

            elif clickedTile:
                return clickedTile, promotingPawn

        return clickedTile, promotingPawn


    def movePiece(self, piece, y, x):

        target = self.matrix[y][x]
        self.matrix[y][x] = piece
        self.matrix[piece.getCoordY()][piece.getCoordX()] = None

        piece.setCoordY(y)
        piece.setCoordX(x)

        if self.turn == 'white':
            opponentKing = self.bk
        else:
            opponentKing = self.wk

        isCheckemated = self.checkMate(opponentKing)
        print('is', opponentKing.getColor(), 'getting checkmated ?', isCheckemated)
        if isCheckemated:
            print(opponentKing.getColor(), "lost")

        self.switchTurn()

        if target != None:
            if target.getColor() != piece.getColor():
                eatSound.play()
                return 'x'
        moveSound.play()
        return ''
        
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
    

    def generateIsCheckingPiecesList(self):
        '''
        Returns a list of pieces that can move to the king's position.
        whiteList -> white pieces that can move to the black king's position
        blackList -> black pieces that can move to the white king's position
        '''
        whiteList = []
        blackList = []
        for i in range(8):
            for j in range(8):
                if self.matrix[i][j] is not None:
                    if self.matrix[i][j].canMove(self.wk.getCoordY(), self.wk.getCoordX(), self):
                        blackList.append(self.matrix[i][j])
                    elif self.matrix[i][j].canMove(self.bk.getCoordY(), self.bk.getCoordX(), self):
                        whiteList.append(self.matrix[i][j])
        return whiteList, blackList

    def createSimulatedBoard(self):
        simulatedBoard = board()
        simulatedBoard.matrix = [[None for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                piece = self.matrix[i][j]
                if piece is not None:
                    simulatedPiece = copy.deepcopy(piece)
                    simulatedBoard.matrix[i][j] = simulatedPiece
                    simulatedPiece.setCoordY(i)
                    simulatedPiece.setCoordX(j)
        simulatedBoard.wk = copy.deepcopy(self.wk)
        simulatedBoard.bk = copy.deepcopy(self.bk)
        return simulatedBoard

    def simulateMovePiece(self, piece, y, x, boardToSimulate):
        initalY = piece.getCoordY()
        initalX = piece.getCoordX()
        boardToSimulate.matrix[y][x] = piece
        boardToSimulate.matrix[initalY][initalX] = None
        piece.setCoordY(y)
        piece.setCoordX(x)

    def nextMoveIsCheck(self, king, piece, y, x):
        simulatedBoard = self.createSimulatedBoard()
        simPiece = simulatedBoard.matrix[piece.getCoordY()][piece.getCoordX()]
        simulatedBoard.simulateMovePiece(simPiece, y, x, simulatedBoard)
        if king.getColor() == 'white':
            simKing = simulatedBoard.wk
        else:
            simKing = simulatedBoard.bk
        return simKing.isChecked(simulatedBoard, checkNext=False)

    def checkMate(self, king):
        if king.isChecked(self):
            pieces = []
            for i in range(8):
                for j in range(8):
                    currentPiece = self.matrix[i][j]
                    if currentPiece is not None and currentPiece.getColor() == king.getColor() and currentPiece.getName() != 'K':
                        pieces.append(currentPiece)
                    elif currentPiece is not None and currentPiece.getColor() == king.getColor() and currentPiece.getName() == 'K':
                        simKing = currentPiece
                        pieces.append(simKing)
                    
            for piece in pieces:
                initialY = piece.getCoordY()
                initialX = piece.getCoordX()
                possibleMoves = piece.possibleMoves(self)
                for move in possibleMoves:
                    simulatedBoard = self.createSimulatedBoard()
                    simulatedBoard.consoleDisplay()
                    simulatedBoard.simulateMovePiece(piece, move[0], move[1], simulatedBoard)
                    simulatedBoard.consoleDisplay()
                    if not simKing.isChecked(simulatedBoard, checkNext=False):
                        return False
                    simulatedBoard.simulateMovePiece(piece, initialY, initialX, simulatedBoard)
            return True
        else:
            return False
    
    def consoleDisplay(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] is not None:
                    print(self.matrix[i][j].name.lower(), ' ', end='')
                else:
                    print('   ', end='')
            print('')

displayedBoard = board()
displayedBoard.fillBoard()
simulatedBoard = board()