import pieces

class board:
    def buildBoard():
        """
        Initialize the starting board with all the pieces in place.
        """
        board = [[None for _ in range(8)] for _ in range(8)]  # empty board

        for i in range(8):                                    # black pawns
            board[1][i] = pieces.pawn(i, 1, 'black')
        for i in range(8):                                    # white pawns
            board[6][i] = pieces.pawn(i, 6, 'white')

        for i in [0, 7]:                                      # black rooks
            board[0][i] = pieces.rook(i, 0, 'black')
        for i in [0, 7]:                                      # white rooks
            board[7][i] = pieces.rook(i, 7, 'white')

        for i in [1, 6]:                                      # black knights
            board[0][i] = pieces.knight(i, 0, 'black')
        for i in [1, 6]:                                      # white knights
            board[7][i] = pieces.knight(i, 0, 'white')

        for i in [1, 6]:                                      # black knights
            board[0][i] = pieces.bishop(i, 0, 'black')
        for i in [1, 6]:                                      # white knights
            board[7][i] = pieces.bishop(i, 0, 'white')

        board[0, 3] = pieces.queen(3, 0, 'black')             # black queen
        board[7, 3] = pieces.queen(3, 0, 'white')             # white queen

        board[0, 4] = pieces.queen(4, 0, 'black')             # black king
        board[7, 4] = pieces.queen(4, 0, 'white')             # white king

board.buildBoard()