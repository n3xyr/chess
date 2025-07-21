import board
import time
import datetime
import pygame
import sys
import pygame_widgets
from pygame_widgets.button import Button

# Initialize Pygame
pygame.init()

# Define window size
SCALE = float(0.5)

TILESIZE = int(100 * SCALE)
TOPMARGIN = int(100 * SCALE)
BOTTOMMARGIN = int(100 * SCALE)
LEFTMARGIN = 0
RIGHTMARGIN = 0
WIDTH, HEIGHT = LEFTMARGIN + 8 * TILESIZE + RIGHTMARGIN, 8 * TILESIZE + BOTTOMMARGIN + TOPMARGIN
GAME = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
BIGCLOCKWIDTH, SMALLCLOCKWIDTH, CLOCKHEIGHT = int(150 * SCALE), int(125 * SCALE), int(54 * SCALE)
pygame.display.set_caption("Chess")

bp = pygame.transform.scale(pygame.image.load("piecesImages/bp.png"), (TILESIZE, TILESIZE))
bb = pygame.transform.scale(pygame.image.load("piecesImages/bb.png"), (TILESIZE, TILESIZE))
bk = pygame.transform.scale(pygame.image.load("piecesImages/bk.png"), (TILESIZE, TILESIZE))
bn = pygame.transform.scale(pygame.image.load("piecesImages/bn.png"), (TILESIZE, TILESIZE))
bq = pygame.transform.scale(pygame.image.load("piecesImages/bq.png"), (TILESIZE, TILESIZE))
br = pygame.transform.scale(pygame.image.load("piecesImages/br.png"), (TILESIZE, TILESIZE))
wp = pygame.transform.scale(pygame.image.load("piecesImages/wp.png"), (TILESIZE, TILESIZE))
wb = pygame.transform.scale(pygame.image.load("piecesImages/wb.png"), (TILESIZE, TILESIZE))
wk = pygame.transform.scale(pygame.image.load("piecesImages/wk.png"), (TILESIZE, TILESIZE))
wn = pygame.transform.scale(pygame.image.load("piecesImages/wn.png"), (TILESIZE, TILESIZE))
wq = pygame.transform.scale(pygame.image.load("piecesImages/wq.png"), (TILESIZE, TILESIZE))
wr = pygame.transform.scale(pygame.image.load("piecesImages/wr.png"), (TILESIZE, TILESIZE))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT = (235, 236, 208)
DARK = (115, 149, 82)
LIGHTSELECT = (202, 203, 179)
DARKSELECT = (99, 128, 70)
ULTRADARK = (38, 36, 33)
BACKGROUND = (48, 46, 43)
LIGHTGREY = (200, 200, 200)

# Create a surface with per-pixel alpha
DarkSurfaceRGBA = pygame.Surface((TILESIZE, TILESIZE), pygame.SRCALPHA)
LightSurfaceRGBA = pygame.Surface((TILESIZE, TILESIZE), pygame.SRCALPHA)

# Draw a semi-transparent circle (RGBA) on canCaptureSurfaceRGBA
pygame.draw.circle(DarkSurfaceRGBA, (99, 128, 70, 192), (TILESIZE // 2, TILESIZE // 2), TILESIZE // 2, TILESIZE // 10)
pygame.draw.circle(LightSurfaceRGBA, (202, 203, 179, 192), (TILESIZE // 2, TILESIZE // 2), TILESIZE // 2, TILESIZE // 10)

# Define text
pygame.font.init()
robotoFont = pygame.font.SysFont('Roboto', int(50 * SCALE))

# Define tiles size
ROWS, COLS = 8, 8

buttons = []
pieces = [
    {'name': 'whiteQueen', 'img': wq, 'pos': (160, 50)},
    {'name': 'whiteKnight', 'img': wn, 'pos': (160, 150)},
    {'name': 'whiteRook', 'img': wr, 'pos': (160, 250)},
    {'name': 'whiteBishop', 'img': wb, 'pos': (160, 350)},
    {'name': 'blackQueen', 'img': bq, 'pos': (160, 50)},
    {'name': 'blackKnight', 'img': bn, 'pos': (160, 150)},
    {'name': 'blackRook', 'img': br, 'pos': (160, 250)},
    {'name': 'blackBishop', 'img': bb, 'pos': (160, 350)},
]

promoImageSize = int(100 * SCALE)
promoImageSpacing = int(5 * SCALE)
promoInnerMargin = int(10 * SCALE)

promoBlockWidth = promoImageSize + 2 * promoInnerMargin
promoBlockHeight = 4 * promoImageSize + (4 - 1) * promoImageSpacing + 2 * promoInnerMargin

promoBlockX = WIDTH // 2 - promoBlockWidth // 2
promoBlockY = HEIGHT // 2 - promoBlockHeight // 2

promoBackground = pygame.Rect(promoBlockX, promoBlockY, promoBlockWidth, promoBlockHeight)

promoIconPos = []
for i in range(4):
    x = promoBlockX + promoBlockWidth // 2
    y = promoBlockY + promoInnerMargin + i * (promoImageSize + promoImageSpacing)
    promoIconPos.append((x, y))

promoOrder = {
    'white': [wq, wn, wr, wb],
    'black': [bq, bn, br, bb]
}

promoIconRects = []

for i in range(len(pieces)):
    pos = promoIconPos[i % 4]
    img = pieces[i]['img']
    img_rect = img.get_rect(center=pos)
    pieces[i]['rect'] = img_rect


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
                    if currentLoadingPiece.name == 'N':
                        game.blit(bn, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # black knight
                    if currentLoadingPiece.name == 'R':
                        game.blit(br, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # black rook
                    if currentLoadingPiece.name == 'P':
                        game.blit(bp, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # black pawn
                    if currentLoadingPiece.name == 'B':
                        game.blit(bb, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # black bishop
                    if currentLoadingPiece.name == 'Q':
                        game.blit(bq, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # black queen
                    if currentLoadingPiece.name == 'K':
                        game.blit(bk, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # black king
                else:
                    if currentLoadingPiece.name == 'N':
                        game.blit(wn, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # white knight
                    if currentLoadingPiece.name == 'R':
                        game.blit(wr, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # white rook
                    if currentLoadingPiece.name == 'P':
                        game.blit(wp, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # white pawn
                    if currentLoadingPiece.name == 'B':
                        game.blit(wb, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # white bishop
                    if currentLoadingPiece.name == 'Q':
                        game.blit(wq, (col * TILESIZE, TOPMARGIN + row * TILESIZE))    # white queen
                    if currentLoadingPiece.name == 'K':
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


def initClock():
    initialTime = time.time()
    lastTime = initialTime
    timer = 0
    return initialTime, lastTime, timer


def doClock(initialTime, lastTime, timer):
    global SCALE
    currentTime = time.time()
    if currentTime - lastTime >= 1:
        lastTime = currentTime
        timer = int(currentTime - initialTime)
    if timer >= 3600:
        pygame.draw.rect(GAME, ULTRADARK, (int(615 * SCALE), int(23 * SCALE), BIGCLOCKWIDTH, CLOCKHEIGHT))
        GAME.blit(robotoFont.render(str(datetime.timedelta(seconds=timer)), False, WHITE), (int(630 * SCALE), int(35 * SCALE)))
    else:
        pygame.draw.rect(GAME, ULTRADARK, (int(630 * SCALE), int(23 * SCALE), SMALLCLOCKWIDTH, CLOCKHEIGHT))
        GAME.blit(robotoFont.render(str(datetime.timedelta(seconds=timer))[2:], False, WHITE), (int(648 * SCALE), int(35 * SCALE)))


def displayAvailableMoves(availableMoves, selectedTile):
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

def main():
    clock = pygame.time.Clock()
    run = True
    moveList = []
    selectedTile = None
    availableMoves = []

    while run:
        clock.tick(60)  # 60 FPS cap

        drawBoard(GAME)
        for move in availableMoves:
            y, x = move
            target = board.displayedBoard.matrix[y][x]
            if target and selectedTile:
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
            initialTime, lastTime, timer = initClock()
        else:
            doClock(initialTime, lastTime, timer)

        promoIconRects.clear()
        if selectedTile is not None and selectedTile.name == 'P' and selectedTile.isAbleToPromote():
            pygame.draw.rect(GAME, WHITE, promoBackground)
            for idx, img in enumerate(promoOrder[selectedTile.getColor()]):
                pos = promoIconPos[idx]
                rectBg = pygame.Rect(pos[0] - img.get_width() // 2, pos[1], img.get_width(), img.get_height())
                pygame.draw.rect(GAME, LIGHTGREY, rectBg)
                GAME.blit(img, (pos[0] - img.get_width() // 2, pos[1]))
                promoIconRects.append((rectBg, ['queen','knight','rook','bishop'][idx]))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseX, mouseY = pygame.mouse.get_pos()

                if promoIconRects:  # if a pawn is promoting
                    for rect, pieceName in promoIconRects:
                        if rect.collidepoint((mouseX, mouseY)):
                            board.displayedBoard.promote(selectedTile, pieceName)
                            promoIconRects.clear()
                            selectedTile = None
                            availableMoves = []
                            break
                    continue  # don't do anything if something else than a promotion is clicked

                if LEFTMARGIN < mouseX < WIDTH - RIGHTMARGIN and TOPMARGIN < mouseY < HEIGHT - BOTTOMMARGIN:
                    mouseXTab = int((mouseX - LEFTMARGIN) / TILESIZE)
                    mouseYTab = int((mouseY - TOPMARGIN) / TILESIZE)
                    clickedTile = board.displayedBoard.matrix[mouseYTab][mouseXTab]

                    if selectedTile:
                        if selectedTile.canMove(mouseYTab, mouseXTab, board.displayedBoard.matrix):
                            act = board.displayedBoard.movePiece(selectedTile, mouseYTab, mouseXTab)
                            if board.displayedBoard.matrix[mouseYTab][mouseXTab] is not None:
                                movedPiece = board.displayedBoard.matrix[mouseYTab][mouseXTab]

                            if movedPiece.name == 'P' and movedPiece.isAbleToPromote():
                                selectedTile = movedPiece
                            else:
                                selectedTile = None

                            availableMoves = []
                            moveList.append(
                                movedPiece.getName() + act + chr(97 + mouseXTab) + str(8 - mouseYTab)
                            )

                        elif clickedTile:
                            selectedTile = clickedTile

                    else:
                        selectedTile = clickedTile

                    if selectedTile and selectedTile.getColor() == board.displayedBoard.turn:
                        availableMoves = selectedTile.possibleMoves(board.displayedBoard.matrix)
                    else:
                        availableMoves = []

        pygame_widgets.update(events)
        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
