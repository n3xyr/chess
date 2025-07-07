import board
import piecesImages
import time
import datetime
import pygame
import sys

# Initialize Pygame
pygame.init()
bp = pygame.transform.scale(pygame.image.load("piecesImages/bp.png"), (100, 100))
bb = pygame.transform.scale(pygame.image.load("piecesImages/bb.png"), (100, 100))
bk = pygame.transform.scale(pygame.image.load("piecesImages/bk.png"), (100, 100))
bn = pygame.transform.scale(pygame.image.load("piecesImages/bn.png"), (100, 100))
bq = pygame.transform.scale(pygame.image.load("piecesImages/bq.png"), (100, 100))
br = pygame.transform.scale(pygame.image.load("piecesImages/br.png"), (100, 100))
wp = pygame.transform.scale(pygame.image.load("piecesImages/wp.png"), (100, 100))
wb = pygame.transform.scale(pygame.image.load("piecesImages/wb.png"), (100, 100))
wk = pygame.transform.scale(pygame.image.load("piecesImages/wk.png"), (100, 100))
wn = pygame.transform.scale(pygame.image.load("piecesImages/wn.png"), (100, 100))
wq = pygame.transform.scale(pygame.image.load("piecesImages/wq.png"), (100, 100))
wr = pygame.transform.scale(pygame.image.load("piecesImages/wr.png"), (100, 100))

# Define window size
TOPMARGIN = 100
BOTTOMMARGIN = 100
LEFTMARGIN = 0
RIGHTMARGIN = 0
WIDTH, HEIGHT = LEFTMARGIN + 800 + RIGHTMARGIN, 800 + BOTTOMMARGIN + TOPMARGIN
GAME = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# Define colors
WHITE = (255, 255, 255)
LIGHT = (235, 236, 208)
DARK = (73, 95, 52)
ULTRADARK = (38, 36, 33)
BACKGROUND = (48, 46, 43)

# Define tiles size
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

turn = 'white'

def draw_board(game):
    """Draw board"""
    game.fill(BACKGROUND)
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 1:
                pygame.draw.rect(game, DARK, (col * SQUARE_SIZE, TOPMARGIN + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(game, LIGHT, (col * SQUARE_SIZE, TOPMARGIN + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            currentLoadingPiece = board.test.matrix[row][col]
            if currentLoadingPiece != None:
                if currentLoadingPiece.getColor() == 'black':
                    if currentLoadingPiece.name == 'knight':
                        game.blit(bn, (col * SQUARE_SIZE, TOPMARGIN + row * SQUARE_SIZE))    # black knight
                    if currentLoadingPiece.name == 'rook':
                        game.blit(br, (col * SQUARE_SIZE, TOPMARGIN + row * SQUARE_SIZE))    # black rook
                    if currentLoadingPiece.name == 'pawn':
                        game.blit(bp, (col * SQUARE_SIZE, TOPMARGIN + row * SQUARE_SIZE))    # black pawn
                    if currentLoadingPiece.name == 'bishop':
                        game.blit(bb, (col * SQUARE_SIZE, TOPMARGIN + row * SQUARE_SIZE))    # black bishop
                    if currentLoadingPiece.name == 'queen':
                        game.blit(bq, (col * SQUARE_SIZE, TOPMARGIN + row * SQUARE_SIZE))    # black queen
                    if currentLoadingPiece.name == 'king':
                        game.blit(bk, (col * SQUARE_SIZE, TOPMARGIN + row * SQUARE_SIZE))    # black king
                else:
                    if currentLoadingPiece.name == 'knight':
                        game.blit(wn, (col * SQUARE_SIZE, TOPMARGIN + row * SQUARE_SIZE))    # white knight
                    if currentLoadingPiece.name == 'rook':
                        game.blit(wr, (col * SQUARE_SIZE, TOPMARGIN + row * SQUARE_SIZE))    # white rook
                    if currentLoadingPiece.name == 'pawn':
                        game.blit(wp, (col * SQUARE_SIZE, TOPMARGIN + row * SQUARE_SIZE))    # white pawn
                    if currentLoadingPiece.name == 'bishop':
                        game.blit(wb, (col * SQUARE_SIZE, TOPMARGIN + row * SQUARE_SIZE))    # white bishop
                    if currentLoadingPiece.name == 'queen':
                        game.blit(wq, (col * SQUARE_SIZE, TOPMARGIN + row * SQUARE_SIZE))    # white queen
                    if currentLoadingPiece.name == 'king':
                        game.blit(wk, (col * SQUARE_SIZE, TOPMARGIN + row * SQUARE_SIZE))    # white king

def switchTurn():
    global turn
    if turn == 'white':
        turn = 'black'
    else:
        turn = 'white'

def main():
    clock = pygame.time.Clock()
    run = True
    selected = None

    while run:
        global turn
        clock.tick(60)  # 60 FPS cap

        # if len(moveList) == 0:
        #     timer = time.time()
        #     lastTime = timer
        # else:
        #     if timer - lastTime >= 1:
        #         lastTime = timer

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            mouseX = pygame.mouse.get_pos()[0]  # gets x position of the mouse in the window
            mouseY = pygame.mouse.get_pos()[1]  # gets y position of the mouse in the window

            if WIDTH - RIGHTMARGIN > mouseX > LEFTMARGIN and HEIGHT - BOTTOMMARGIN > mouseY > TOPMARGIN:
                mouseXTab = int((mouseX - LEFTMARGIN) / ((WIDTH - LEFTMARGIN - RIGHTMARGIN) / 8))   # x position in board coordinates
                mouseYTab = int((mouseY - TOPMARGIN) / ((HEIGHT - TOPMARGIN - BOTTOMMARGIN) / 8))   # y position in board coordinates

            if event.type == pygame.MOUSEBUTTONDOWN:    # if mouse clicked
                if event.button == 1:   # left click
                    if selected != None:
                        if selected.canMove(mouseYTab, mouseXTab, board.test.matrix):
                            switchTurn()
                        board.test.movePiece(selected, mouseYTab, mouseXTab)
                        selected = None
                    if board.test.matrix[mouseYTab][mouseXTab] != None and board.test.matrix[mouseYTab][mouseXTab].getColor() == turn:
                        selected = board.test.matrix[mouseYTab][mouseXTab]
                    else:
                        selected = None
                    if selected != None:
                        print(selected.name)
                    else:
                        print(None)
        draw_board(GAME)
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
