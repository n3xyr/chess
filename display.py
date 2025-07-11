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
TILESIZE = 100
TOPMARGIN = 100
BOTTOMMARGIN = 100
LEFTMARGIN = 0
RIGHTMARGIN = 0
WIDTH, HEIGHT = LEFTMARGIN + 8 * TILESIZE + RIGHTMARGIN, 8 * TILESIZE + BOTTOMMARGIN + TOPMARGIN
GAME = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT = (235, 236, 208)
DARK = (115, 149, 82)
LIGHTSELECT = (202, 203, 179)
DARKSELECT = (99, 128, 70)
ULTRADARK = (38, 36, 33)
BACKGROUND = (48, 46, 43)

# Create a surface with per-pixel alpha
DarkSurfaceRGBA = pygame.Surface((TILESIZE, TILESIZE), pygame.SRCALPHA)
LightSurfaceRGBA = pygame.Surface((TILESIZE, TILESIZE), pygame.SRCALPHA)

# Draw a semi-transparent circle (RGBA) on canCaptureSurfaceRGBA
pygame.draw.circle(DarkSurfaceRGBA, (99, 128, 70, 192), (TILESIZE // 2, TILESIZE // 2), TILESIZE // 2, TILESIZE // 10)
pygame.draw.circle(LightSurfaceRGBA, (202, 203, 179, 192), (TILESIZE // 2, TILESIZE // 2), TILESIZE // 2, TILESIZE // 10)

# Define text
pygame.font.init()
robotoFont = pygame.font.SysFont('Roboto', 50)

# Define tiles size
ROWS, COLS = 8, 8


def drawBoard(game):
    """
    Draw board
    """
    game.fill(BACKGROUND)
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 1:
                pygame.draw.rect(game, DARK, (col * TILESIZE, TOPMARGIN + row * TILESIZE, TILESIZE, TILESIZE))
            else:
                pygame.draw.rect(game, LIGHT, (col * TILESIZE, TOPMARGIN + row * TILESIZE, TILESIZE, TILESIZE))

            currentLoadingPiece = board.displayedBoard.matrix[row][col]
            if currentLoadingPiece != None:
                if currentLoadingPiece.getColor() == 'black':
                    if currentLoadingPiece.name == 'knight':
                        game.blit(bn, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # black knight
                    if currentLoadingPiece.name == 'rook':
                        game.blit(br, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # black rook
                    if currentLoadingPiece.name == 'pawn':
                        game.blit(bp, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # black pawn
                    if currentLoadingPiece.name == 'bishop':
                        game.blit(bb, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # black bishop
                    if currentLoadingPiece.name == 'queen':
                        game.blit(bq, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # black queen
                    if currentLoadingPiece.name == 'king':
                        game.blit(bk, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # black king
                else:
                    if currentLoadingPiece.name == 'knight':
                        game.blit(wn, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # white knight
                    if currentLoadingPiece.name == 'rook':
                        game.blit(wr, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # white rook
                    if currentLoadingPiece.name == 'pawn':
                        game.blit(wp, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # white pawn
                    if currentLoadingPiece.name == 'bishop':
                        game.blit(wb, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # white bishop
                    if currentLoadingPiece.name == 'queen':
                        game.blit(wq, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # white queen
                    if currentLoadingPiece.name == 'king':
                        game.blit(wk, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # white king


def getTileColor(coordinates):
    y = coordinates[0]
    x = coordinates[1]
    return 'LIGHT' if (y + x) % 2 == 0 else 'DARK'


def drawPossibleTile(game, tabCoordinates):
    if getTileColor(tabCoordinates) == 'LIGHT':
        pygame.draw.circle(game, LIGHTSELECT, (LEFTMARGIN + tabCoordinates[1] * TILESIZE + TILESIZE / 2, TOPMARGIN + tabCoordinates[0] * TILESIZE + TILESIZE/2), TILESIZE/6)
    else:
        pygame.draw.circle(game, DARKSELECT, (LEFTMARGIN + tabCoordinates[1] * TILESIZE + TILESIZE / 2, TOPMARGIN + tabCoordinates[0] * TILESIZE + TILESIZE/2), TILESIZE/6)


def initClock(moveList):
    initialTime = time.time()
    lastTime = initialTime
    timer = 0
    moveList.append(1)
    return initialTime, lastTime, timer


def doClock(initialTime, lastTime, timer):
    currentTime = time.time()
    if currentTime - lastTime >= 1:
        lastTime = currentTime
        timer = int(currentTime - initialTime)
    if timer >= 3600:
        pygame.draw.rect(GAME, ULTRADARK, (615, 23, 150, 54))
        GAME.blit(robotoFont.render(str(datetime.timedelta(seconds=timer)), False, WHITE), (630, 35))
    else:
        pygame.draw.rect(GAME, ULTRADARK, (630, 23, 125, 54))
        GAME.blit(robotoFont.render(str(datetime.timedelta(seconds=timer))[2:], False, WHITE), (648, 35))


def main():
    drawBoard(GAME)
    clock = pygame.time.Clock()
    run = True
    moveList = []
    selectedTile = None
    availableMoves = []

    while run:
        clock.tick(60)  # 60 FPS cap
        drawBoard(GAME)
        for move in availableMoves:
            y = move[0]
            x = move[1]
            target = board.displayedBoard.matrix[y][x]
            if target != None and selectedTile != None:
                if target.getColor() != selectedTile.getColor():
                    if getTileColor(move) == 'DARK':
                        GAME.blit(DarkSurfaceRGBA, (LEFTMARGIN + x * TILESIZE, TOPMARGIN + y * TILESIZE))
                    else:
                        GAME.blit(LightSurfaceRGBA, (LEFTMARGIN + x * TILESIZE, TOPMARGIN + y * TILESIZE))
                else:
                    drawPossibleTile(GAME, move)
            else:
                    drawPossibleTile(GAME, move)


        if len(moveList) == 0:
            initialTime, lastTime, timer = initClock(moveList)
        else:
            doClock(initialTime, lastTime, timer)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            mouseX = pygame.mouse.get_pos()[0]  # gets x position of the mouse in the window
            mouseY = pygame.mouse.get_pos()[1]  # gets y position of the mouse in the window

            if WIDTH - RIGHTMARGIN > mouseX > LEFTMARGIN and HEIGHT - BOTTOMMARGIN > mouseY > TOPMARGIN:
                mouseXTab = int((mouseX - LEFTMARGIN) / ((WIDTH - LEFTMARGIN - RIGHTMARGIN) / 8))   # x position in board coordinates
                mouseYTab = int((mouseY - TOPMARGIN) / ((HEIGHT - TOPMARGIN - BOTTOMMARGIN) / 8))   # y position in board coordinates

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:        # Left click up
                clickedTile = board.displayedBoard.matrix[mouseYTab][mouseXTab]

                if selectedTile != None:

                    if selectedTile.canMove(mouseYTab, mouseXTab, board.displayedBoard.matrix):
                        board.displayedBoard.movePiece(selectedTile, mouseYTab, mouseXTab)
                        availableMoves = []
                        selectedTile = None
                    elif clickedTile != None:
                        selectedTile = clickedTile

                else:
                    selectedTile = clickedTile

                if selectedTile != None:
                    if selectedTile.getColor() == board.displayedBoard.turn:
                        availableMoves = selectedTile.possibleMoves(board.displayedBoard.matrix)
                    else:
                        availableMoves = []

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()