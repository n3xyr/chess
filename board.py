import pieces

class board:
    def __init__(self):
        self.matrix = [[None for _ in range(8)] for _ in range(8)]

    def fillBoard(self):
        '''
        Fills an empty board with pieces.
        '''
        for i in range(8):                                    # black pawns
            self.matrix[1][i] = pieces.pawn(1, i, 'black')
        for i in range(8):                                    # white pawns
            self.matrix[6][i] = pieces.pawn(6, i, 'white')

        for i in [0, 7]:                                      # black rooks
            self.matrix[0][i] = pieces.rook(0, i, 'black')
        for i in [0, 7]:                                      # white rooks
            self.matrix[7][i] = pieces.rook(7, i, 'white')

        for i in [1, 6]:                                      # black knights
            self.matrix[0][i] = pieces.knight(0, i, 'black')
        for i in [1, 6]:                                      # white knights
            self.matrix[7][i] = pieces.knight(0, i, 'white')

        for i in [2, 5]:                                      # black bishops
            self.matrix[0][i] = pieces.bishop(0, i, 'black')
        for i in [2, 5]:                                      # white bishops
            self.matrix[7][i] = pieces.bishop(0, i, 'white')

        self.matrix[0][3] = pieces.queen(0, 3, 'black')               # black queen
        self.matrix[7][3] = pieces.queen(0, 3, 'white')               # white queen

        self.matrix[0][4] = pieces.king(0, 4, 'black')                # black king
        self.matrix[7][4] = pieces.king(0, 4, 'white')                # white king

    def movePiece(self, piece, y, x):
        if piece == None:
            return
        elif piece.canMove(y, x, self.matrix):
            self.matrix[y][x] = piece
            self.matrix[piece.getCoordY()][piece.getCoordX()] = None
            piece.setCoordY() = y
            piece.setCoordX() = x

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

test = board()
test.fillBoard()
test.print()
print('----------------------------------------------------------------')

# Knight

# print(test.matrix[0][1].canMove(2, 2, test.matrix)) # True
# print(test.matrix[0][1].canMove(2, 3, test.matrix)) # False
# print(test.matrix[0][1].canMove(3, 2, test.matrix)) # False
# print(test.matrix[0][1].canMove(3, 2, test.matrix)) # False
# print(test.matrix[0][1].canMove(-1, 3, test.matrix)) # False

# Rook

# print(test.matrix[0][0].canMove(0, 2, test.matrix)) # False
# test.matrix[1][0] = None
# print(test.matrix[0][0].canMove(0, 2, test.matrix)) # True
# test.matrix[1][0] = pieces.pawn(0, 1, 'black')

# King

# print(test.matrix[0][4].canMove(3, 1, test.matrix)) # False
# test.matrix[1][3] = None
# print(test.matrix[0][4].canMove(3, 1, test.matrix)) # True
# test.matrix[1][3] = pieces.pawn(3, 1, 'black')

# Pawn

# print(test.matrix[1][0].getColor()) # 'black'
# print(test.matrix[1][0].canMove(3, 0, test.matrix)) #True

# Bishop

# test.matrix[1][1] = None
# test.matrix[1][0] = None
# test.matrix[2][1] = pieces.pawn(2, 1, 'black')
# test.matrix[2][0] = pieces.pawn(2, 0, 'black')
# test.print()
# print(test.matrix[0][2].canMove(2, 4, test.matrix)) # False
# print(test.matrix[0][2].canMove(2, 0, test.matrix)) # False
# print(test.matrix[0][2].canMove(1, 1, test.matrix)) # True
# print(test.matrix[0][2].canMove(2, 2, test.matrix)) # False

# Queen

# for i in range(8):
#     test.matrix[1][i] = None
# test.print()
# print(test.matrix[0][3].canMove(5, 2, test.matrix)) # False
# print(test.matrix[0][3].canMove(4, 3, test.matrix)) # True
# print(test.matrix[0][3].canMove(3, 0, test.matrix)) # True
# print(test.matrix[0][3].canMove(0, 4, test.matrix)) # False
