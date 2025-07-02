import pieces

class board:
    def __init__(self):
        self.matrix = [[None for _ in range(8)] for _ in range(8)]

    def fillBoard(self):
        '''
        Fills an empty board with pieces.
        '''
        for i in range(8):                                    # black pawns
            self.matrix[1][i] = pieces.pawn(i, 1, 'black')
        for i in range(8):                                    # white pawns
            self.matrix[6][i] = pieces.pawn(i, 6, 'white')

        for i in [0, 7]:                                      # black rooks
            self.matrix[0][i] = pieces.rook(i, 0, 'black')
        for i in [0, 7]:                                      # white rooks
            self.matrix[7][i] = pieces.rook(i, 7, 'white')

        for i in [1, 6]:                                      # black knights
            self.matrix[0][i] = pieces.knight(i, 0, 'black')
        for i in [1, 6]:                                      # white knights
            self.matrix[7][i] = pieces.knight(i, 0, 'white')

        for i in [2, 5]:                                      # black bishops
            self.matrix[0][i] = pieces.bishop(i, 0, 'black')
        for i in [2, 5]:                                      # white bishops
            self.matrix[7][i] = pieces.bishop(i, 0, 'white')

        self.matrix[0][3] = pieces.queen(3, 0, 'black')               # black queen
        self.matrix[7][3] = pieces.queen(3, 0, 'white')               # white queen

        self.matrix[0][4] = pieces.king(4, 0, 'black')                # black king
        self.matrix[7][4] = pieces.king(4, 0, 'white')                # white king

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


# Knight
print(test.matrix[0][1].canMove(2, 2, test.matrix)) # True
print(test.matrix[0][1].canMove(2, 3, test.matrix)) # False
print(test.matrix[0][1].canMove(3, 2, test.matrix)) # False
print(test.matrix[0][1].canMove(3, 2, test.matrix)) # False

# Rook
print(test.matrix[0][0].canMove(0, 2, test.matrix)) # False

# print(test.matrix[1][0].getColor())
# print(test.matrix[1][0].canMove(3, 0, test.matrix))