import pieces
import pygame

# moveSound = pygame.mixer.Sound('moveSound.mp3')
# eatSound = pygame.mixer.Sound('eatSound.mp3')

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

        self.matrix[0][3] = pieces.queen(0, 3, 'black')               # black queen
        self.matrix[7][3] = pieces.queen(7, 3, 'white')               # white queen

        self.matrix[0][4] = pieces.king(0, 4, 'black')                # black king
        self.matrix[7][4] = pieces.king(7, 4, 'white')                # white king

    def getAvailableMoves(self, selectedTile):
        if selectedTile == None:
            return []
        if selectedTile.getColor() == self.turn:
           return selectedTile.possibleMoves(self.matrix)


    def manageMove(self, selectedTile, mouseYTab, mouseXTab, moveList):
        clickedTile = self.matrix[mouseYTab][mouseXTab]

        if selectedTile != None:

            if selectedTile.canMove(mouseYTab, mouseXTab, self.matrix):
                act = self.movePiece(selectedTile, mouseYTab, mouseXTab)
                moveList.append(selectedTile.getName() + act + chr(97 + mouseXTab) + str(8 - mouseYTab))
                print(moveList)
                return None
            elif clickedTile != None:
                return clickedTile

        else:
            return clickedTile

    def movePiece(self, piece, y, x):

        if piece.getColor() == self.turn and piece.canMove(y, x, self.matrix):
            target = self.matrix[y][x]
            self.matrix[y][x] = piece
            self.matrix[piece.getCoordY()][piece.getCoordX()] = None

            piece.setCoordY(y)
            piece.setCoordX(x)

            self.switchTurn()

            if target !=None:
                if target.getColor() != piece.getColor():
                    return 'x'
        return ''
    def print(self):
        '''
        Shows the board.
        '''
        for i in range(8):
            line = []
            for j in range(8):
                if self.matrix[i][j] == None:
                    line.append('    ')
                else:
                    line.append(self.matrix[i][j].name)
            print(line)

displayedBoard = board()
displayedBoard.fillBoard()