import board
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

# Define text
pygame.font.init()
robotoFont = pygame.font.SysFont('Roboto', 50)

# Define tiles size
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

turn = 'white'

def drawBoard(game):
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
    drawBoard(GAME)
    clock = pygame.time.Clock()
    run = True
    moveList = []
    selected = None

    while run:
        global turn
        clock.tick(60)  # 60 FPS cap
        drawBoard(GAME)

        if len(moveList) == 0:
            initialTime = time.time()
            lastTime = initialTime
            moveList.append(1)
        else:
            currentTime = time.time()
            if currentTime - lastTime >= 1:
                lastTime = currentTime
                timer = int(currentTime - initialTime)
                if timer >= 3600:
                    print('1h')
                    pygame.draw.rect(GAME, ULTRADARK, (615, 23, 150, 54))
                    GAME.blit(robotoFont.render(str(datetime.timedelta(seconds=timer)), False, WHITE), (630, 35))
                else:
                    pygame.draw.rect(GAME, ULTRADARK, (630, 23, 125, 54))
                    GAME.blit(robotoFont.render(str(datetime.timedelta(seconds=timer))[2:], False, WHITE), (648, 35))


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
                    clickedTile = board.test.matrix[mouseYTab][mouseXTab]
                    if selected != None:
                        print(selected.canMove(mouseYTab, mouseXTab, board.test.matrix))
                        if selected.canMove(mouseYTab, mouseXTab, board.test.matrix):
                            switchTurn()
                        board.test.movePiece(selected, mouseYTab, mouseXTab)
                        selected = None
                    if clickedTile != None:
                        if clickedTile.getColor() == turn:
                            selected = board.test.matrix[mouseYTab][mouseXTab]
                    else:
                        selected = None

                    if selected != None:
                        print(selected.name)
                    else:
                        print(None)
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()