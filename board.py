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
        self.boardHistoric = []
        self.soundHistoric = []
        self.historicIndic = 0


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
        

        self.boardHistoric = [copy.deepcopy(self.matrix)]  # Initial historic state
        self.historicIndic = len(self.boardHistoric) - 1


    def getAvailableMoves(self, selectedTile):
        if selectedTile == None:
            return []
        if selectedTile.getColor() == self.turn:
           return selectedTile.possibleMoves(self)
        return []


    def getKing(self, piece):
        if piece.getColor() == 'white':
            return self.wk
        else:
            return self.bk


    def getActTypes(self, piece, y, x):
        result = ''

        if piece.getColor() == 'white':
            king = self.wk
        else:
            king =  self.bk

        if self.nextMoveGivesCheck(piece, y, x):
            if self.checkMate(king):
                result += '#,'
            else:
                result += '+,'
                
        if self.matrix[y][x]:
            result += 'x,'

        if piece.name == 'K':
            if (piece.getCoordX() - x) ** 2 > 1:
                if piece.getCoordX() - x > 0:
                    result += 'O-O-O,'
                else:
                    result += 'O-O,'

        if piece.name == '':
            if y in (0, 7):
                result += '=,'
            elif (piece.getCoordY() - y) ** 2 == 1 and (piece.getCoordX() - x) ** 2 == 1 and self.matrix[y][x] is None:
                result += 'e.p,'

        return result[0:-1]


    def addMoveToHistoric(self, moveList, actList, piece, y, x):
        resultMove = piece.name

        if resultMove == '' and 'x' in actList:
            resultMove += chr(97 + piece.getCoordX())
        if piece.name != '':
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix)):
                    matrixPiece = self.matrix[i][j]
                    if matrixPiece:
                        if matrixPiece.name == piece.name:
                            if matrixPiece.canMove(y, x, self):
                                if matrixPiece.getCoordX() != piece.getCoordX():
                                    resultMove += chr(97 + piece.getCoordX())
                                elif matrixPiece.getCoordY() != piece.getCoordY():
                                    resultMove += str(8 - piece.getCoordY())


        if 'x' in actList:
            resultMove += 'x'

        resultMove += chr(97 + x) + str(8 - y)

        if '=' in actList:
            resultMove += '=' + self.matrix[piece.getCoordY()][piece.getCoordX()].name

        if 'O-O-O' in actList:
            resultMove = 'O-O-O' + resultMove
        elif 'O-O' in actList:
            resultMove = 'O-O' + resultMove
        
        if '+' in actList:
            resultMove += '+'
        elif '#' in actList:
            resultMove += '#'

        moveList.append(resultMove)


    def manageSelection(self, selectedTile, y, x):
        clickedTile = self.matrix[y][x]

        if selectedTile and selectedTile.canMove(y, x, self) and selectedTile.getColor() == self.turn:
            return selectedTile, True
        
        return clickedTile, False

    
    def playSound(self, act):
        if 'x' in act:
            eatSound.play()
        else:
            moveSound.play()


    def addSoundToHistoric(self, act):
        if 'x' in act:
            self.soundHistoric.append('x')
        else:
            self.soundHistoric.append('')


    def movePiece(self, piece, y, x):
        actList = self.getActTypes(piece, y, x)

        self.matrix[y][x] = piece
        self.matrix[piece.getCoordY()][piece.getCoordX()] = None

        piece.setCoordY(y)
        piece.setCoordX(x)

        if piece.getColor() == 'white':
            opponentKing = self.wk
        else:
            opponentKing =  self.bk

        isCheckemated = self.checkMate(opponentKing)

        if isCheckemated:
            print(opponentKing.getColor(), "lost")

        self.switchTurn()
        
        self.playSound(actList.split(','))
        self.addSoundToHistoric(actList.split(','))


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
        return initialTime


    def getClock(self, initialTime):
        currentTime = time.time()
        return int(currentTime - initialTime)


    def createSimulatedBoard(self):
        simulatedBoard = board()
        for i in range(8):
            for j in range(8):
                piece = self.matrix[i][j]
                if piece is not None:
                    simulatedPiece = copy.deepcopy(piece)
                    simulatedBoard.matrix[i][j] = simulatedPiece
                    simulatedPiece.setCoordY(i)
                    simulatedPiece.setCoordX(j)
                    if simulatedPiece.name == 'K':
                        if simulatedPiece.getColor() == 'white':
                            simulatedBoard.wk = simulatedPiece
                        else:
                            simulatedBoard.bk = simulatedPiece
        return simulatedBoard


    def simulateMovePiece(self, piece, y, x):
        if piece:
            initalY = piece.getCoordY()
            initalX = piece.getCoordX()
            self.matrix[y][x] = piece
            self.matrix[initalY][initalX] = None
            piece.setCoordY(y)
            piece.setCoordX(x)


    def nextMoveGivesCheck(self, piece, y, x):
            simulatedBoard = self.createSimulatedBoard()
            simPiece = simulatedBoard.matrix[piece.getCoordY()][piece.getCoordX()]
            simulatedBoard.simulateMovePiece(simPiece, y, x)

            if piece.getColor() == 'white':
                simKing = simulatedBoard.bk
            else:
                simKing =  simulatedBoard.wk

            return simKing.isChecked(simulatedBoard, checkNext=False)


    def nextMoveIsCheck(self, piece, y, x):
        simulatedBoard = self.createSimulatedBoard()
        simPiece = simulatedBoard.matrix[piece.getCoordY()][piece.getCoordX()]
        simulatedBoard.simulateMovePiece(simPiece, y, x)

        if piece.getColor() == 'white':
            simKing = simulatedBoard.wk
        else:
            simKing =  simulatedBoard.bk

        return simKing.isChecked(simulatedBoard, checkNext=False)
    

    def checkMate(self, king):
        if king.isChecked(self):
            pieces = []
            
            simulatedBoard = self.createSimulatedBoard()

            if king.getColor() == 'white':
                simKing = simulatedBoard.wk
            else:
                simKing = simulatedBoard.bk   

            for i in range(8):
                for j in range(8):
                    currentPiece = simulatedBoard.matrix[i][j]
                    if currentPiece is not None and currentPiece.getColor() == simKing.getColor():
                        pieces.append(currentPiece)
            
            for piece in pieces:
                initialY = piece.getCoordY()
                initialX = piece.getCoordX()
                possibleMoves = piece.possibleMoves(self)
                for move in possibleMoves:
                    simulatedBoard = self.createSimulatedBoard()
                    simulatedBoard.simulateMovePiece(piece, move[0], move[1])
                    if not simKing.isChecked(simulatedBoard, checkNext=False):
                        return False
                    piece.setCoordY(initialY)
                    piece.setCoordX(initialX)
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


    def consoleDisplayHistoric(self):
        print('Historic:')
        for i, state in enumerate(self.boardHistoric):
            print(f'State {i}:')
            for row in state:
                for piece in row:
                    if piece is not None:
                        if piece.name == '':
                            print('p', ' ', end='')
                        else:
                            print(piece.name.lower(), ' ', end='')
                    else:
                        print('   ', end='')
                print('')
            print('---')


displayedBoard = board()
displayedBoard.fillBoard()
simulatedBoard = board()