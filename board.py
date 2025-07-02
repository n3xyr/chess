
class board:
    def __init__(self):
        self.matrix = [[None for _ in range(8)] for _ in range(8)]

    def fillBoard(self):
        '''
        Fills an empty board with pieces.
        '''
        for i in range(8):                                    # black pawns
            self.matrix[1][i] = pawn(i, 1, 'black')
        for i in range(8):                                    # white pawns
            self.matrix[6][i] = pawn(i, 6, 'white')

        for i in [0, 7]:                                      # black rooks
            self.matrix[0][i] = rook(i, 0, 'black')
        for i in [0, 7]:                                      # white rooks
            self.matrix[7][i] = rook(i, 7, 'white')

        for i in [1, 6]:                                      # black knights
            self.matrix[0][i] = knight(i, 0, 'black')
        for i in [1, 6]:                                      # white knights
            self.matrix[7][i] = knight(i, 0, 'white')

        for i in [2, 5]:                                      # black bishops
            self.matrix[0][i] = bishop(i, 0, 'black')
        for i in [2, 5]:                                      # white bishops
            self.matrix[7][i] = bishop(i, 0, 'white')

        self.matrix[0][3] = queen(3, 0, 'black')               # black queen
        self.matrix[7][3] = queen(3, 0, 'white')               # white queen

        self.matrix[0][4] = king(4, 0, 'black')                # black king
        self.matrix[7][4] = king(4, 0, 'white')                # white king

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