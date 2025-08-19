import board
import pygame
import sys
import pygame_widgets
from screeninfo import get_monitors
from pygame_widgets.button import Button
import display_assistant
from copy import deepcopy
import chess_clock
import end_screen

# Initialize Pygame
pygame.init()
pygame.font.init()

# Get monitor(s) specs
def getMonitorResolution():
    for m in get_monitors():
        if m.is_primary:
            return m.width, m.height


INIT_LEFTMARGIN = 0
INIT_RIGHTMARGIN = 350
INIT_TOPMARGIN = 100
INIT_BOTTOMMARGIN = 100
INIT_TILESIZE = 100
INIT_WIDTH = INIT_LEFTMARGIN + 8 * INIT_TILESIZE + INIT_RIGHTMARGIN
INIT_HEIGHT = 8 * INIT_TILESIZE + INIT_BOTTOMMARGIN + INIT_TOPMARGIN

LEFTMARGIN = INIT_LEFTMARGIN
RIGHTMARGIN = INIT_RIGHTMARGIN
TOPMARGIN = INIT_TOPMARGIN
BOTTOMMARGIN = INIT_BOTTOMMARGIN
TILESIZE = INIT_TILESIZE
SCALE = 1


def adjustWindowSize(newWidth, newHeight):
    global WIDTH, HEIGHT, LEFTMARGIN, RIGHTMARGIN, TOPMARGIN, BOTTOMMARGIN, TILESIZE, SCALE, GAME
    global bp, bb, bk, bn, bq, br, wp, wb, wk, wn, wq, wr, bpFigurine, bbFigurine, bkFigurine, bnFigurine, bqFigurine, brFigurine, bCastleFigurine, wpFigurine, wbFigurine, wkFigurine, wnFigurine, wqFigurine, wrFigurine, wCastleFigurine, nothingness
    global robotoFont, robotoMedium, darkSurfaceRGBA, lightSurfaceRGBA, arrowSurfaceRGBA
    
    if newWidth == int(INIT_WIDTH * SCALE) and newHeight != INIT_HEIGHT * SCALE:
        SCALE = newHeight / INIT_HEIGHT
    elif newHeight == int(INIT_HEIGHT * SCALE) and newWidth != INIT_WIDTH * SCALE:
        SCALE = newWidth / INIT_WIDTH
    else:
        SCALE = min(newWidth / INIT_WIDTH, newHeight / INIT_HEIGHT)
    
    TILESIZE = int(INIT_TILESIZE * SCALE)
    LEFTMARGIN = int(INIT_LEFTMARGIN * SCALE)
    RIGHTMARGIN = int(INIT_RIGHTMARGIN * SCALE)
    TOPMARGIN = int(INIT_TOPMARGIN * SCALE)
    BOTTOMMARGIN = int(INIT_BOTTOMMARGIN * SCALE)

    WIDTH, HEIGHT = INIT_WIDTH * SCALE, INIT_HEIGHT * SCALE
    GAME = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    robotoFont = pygame.font.SysFont('Roboto', int(50 * SCALE))
    robotoMedium = pygame.font.Font('fonts/Roboto-Medium.ttf', int(25 * SCALE))
    
    darkSurfaceRGBA = pygame.Surface((TILESIZE, TILESIZE), pygame.SRCALPHA)
    lightSurfaceRGBA = pygame.Surface((TILESIZE, TILESIZE), pygame.SRCALPHA)
    arrowSurfaceRGBA = pygame.Surface((TILESIZE * 8, TILESIZE * 8), pygame.SRCALPHA)
    
    pygame.draw.circle(darkSurfaceRGBA, (99, 128, 70, 192), (TILESIZE // 2, TILESIZE // 2), TILESIZE // 2, TILESIZE // 10)
    pygame.draw.circle(lightSurfaceRGBA, (202, 203, 179, 192), (TILESIZE // 2, TILESIZE // 2), TILESIZE // 2, TILESIZE // 10)
        
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

    bpFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/bpFigurine.png"), (int(TILESIZE), int(TILESIZE)))
    bbFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/bbFigurine.png"), (int(TILESIZE), int(TILESIZE)))
    bkFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/bkFigurine.png"), (int(TILESIZE), int(TILESIZE)))
    bnFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/bnFigurine.png"), (int(TILESIZE), int(TILESIZE)))
    bqFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/bqFigurine.png"), (int(TILESIZE), int(TILESIZE)))
    brFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/brFigurine.png"), (int(TILESIZE), int(TILESIZE)))
    wpFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/wpFigurine.png"), (int(TILESIZE), int(TILESIZE)))
    wbFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/wbFigurine.png"), (int(TILESIZE), int(TILESIZE)))
    wkFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/wkFigurine.png"), (int(TILESIZE), int(TILESIZE)))
    wnFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/wnFigurine.png"), (int(TILESIZE), int(TILESIZE)))
    wqFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/wqFigurine.png"), (int(TILESIZE), int(TILESIZE)))
    wrFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/wrFigurine.png"), (int(TILESIZE), int(TILESIZE)))
    wCastleFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/wCastleFigurine.png"), (int(TILESIZE), int(TILESIZE)))
    bCastleFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/bCastleFigurine.png"), (int(TILESIZE), int(TILESIZE)))
    nothingness = pygame.image.load("piecesFigurines/nothingness.png")


def adjustPromoSize():
    global pieces, promoImageSize, promoImageSpacing, promoInnerMargin, promoBlockWidth, promoBlockHeight, promoBlockX, promoBlockY, promoBackground, promoIconPos, promoOrder, promoIconRects, pos, img, img_rect
    global WIDTH, HEIGHT, SCALE, TILESIZE
    global wq, wn, wr, wb, bq, bn, br, bb
    
    promoImageSize = TILESIZE
    promoImageSpacing = int(5 * SCALE)
    promoInnerMargin = int(10 * SCALE)

    promoBlockWidth = promoImageSize + 2 * promoInnerMargin
    promoBlockHeight = 4 * promoImageSize + (4 - 1) * promoImageSpacing + 2 * promoInnerMargin
    promoBlockX = LEFTMARGIN + 4 * TILESIZE - promoBlockWidth // 2
    promoBlockY = HEIGHT // 2 - promoBlockHeight // 2

    promoBackground = pygame.Rect(promoBlockX, promoBlockY, promoBlockWidth, promoBlockHeight)

    promoIconPos = []
    for i in range(4):
        x = promoBlockX + promoBlockWidth // 2
        y = promoBlockY + promoInnerMargin + i * (promoImageSize + promoImageSpacing)
        promoIconPos.append((x, y))
        
    pieces = [
    {'name': 'whiteQueen', 'img': wq, 'pos': (int(WIDTH / 2), int(HEIGHT / 2 - promoImageSize * 1.5 - promoImageSpacing * 1.5))},
    {'name': 'whiteKnight', 'img': wn, 'pos': (int(WIDTH / 2), int(HEIGHT / 2 - promoImageSize * 0.5 - promoImageSpacing * 0.5))},
    {'name': 'whiteRook', 'img': wr, 'pos': (int(WIDTH / 2), int(HEIGHT / 2 + promoImageSize * 0.5 + promoImageSpacing * 0.5))},
    {'name': 'whiteBishop', 'img': wb, 'pos': (int(WIDTH / 2), int(HEIGHT / 2 + promoImageSize * 1.5 + promoImageSpacing * 1.5))},
    {'name': 'blackQueen', 'img': bq, 'pos': (int(WIDTH / 2), 50)},
    {'name': 'blackKnight', 'img': bn, 'pos': (int(WIDTH / 2), 150)},
    {'name': 'blackRook', 'img': br, 'pos': (int(WIDTH / 2), 250)},
    {'name': 'blackBishop', 'img': bb, 'pos': (int(WIDTH / 2), 350)},
    ]
    
    for i in range(len(pieces)):
        pos = promoIconPos[i % 4]
        img = pieces[i]['img']
        img_rect = img.get_rect(center=pos)
        pieces[i]['rect'] = img_rect


SCREENWIDTH, SCREENHEIGHT = getMonitorResolution()
WIDTH, HEIGHT = LEFTMARGIN + 8 * TILESIZE + RIGHTMARGIN, 8 * TILESIZE + BOTTOMMARGIN + TOPMARGIN
GAME = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
BIGCLOCKWIDTH, SMALLCLOCKWIDTH, CLOCKHEIGHT = int(150 * SCALE), int(125 * SCALE), int(54 * SCALE)
BIGCLOCKPOS, SMALLCLOCKPOS = (int(615 * SCALE), int(23 * SCALE)), (int(630 * SCALE), int(23 * SCALE))
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

bpFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/bpFigurine.png"), (int(TILESIZE * 0.5), int(TILESIZE * 0.5)))
bbFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/bbFigurine.png"), (int(TILESIZE * 0.5), int(TILESIZE * 0.5)))
bkFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/bkFigurine.png"), (int(TILESIZE * 0.5), int(TILESIZE * 0.5)))
bnFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/bnFigurine.png"), (int(TILESIZE * 0.5), int(TILESIZE * 0.5)))
bqFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/bqFigurine.png"), (int(TILESIZE * 0.5), int(TILESIZE * 0.5)))
brFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/brFigurine.png"), (int(TILESIZE * 0.5), int(TILESIZE * 0.5)))
wpFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/wpFigurine.png"), (int(TILESIZE * 0.5), int(TILESIZE * 0.5)))
wbFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/wbFigurine.png"), (int(TILESIZE * 0.5), int(TILESIZE * 0.5)))
wkFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/wkFigurine.png"), (int(TILESIZE * 0.5), int(TILESIZE * 0.5)))
wnFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/wnFigurine.png"), (int(TILESIZE * 0.5), int(TILESIZE * 0.5)))
wqFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/wqFigurine.png"), (int(TILESIZE * 0.5), int(TILESIZE * 0.5)))
wrFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/wrFigurine.png"), (int(TILESIZE * 0.5), int(TILESIZE * 0.5)))
wCastleFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/wCastleFigurine.png"), (int(TILESIZE * 0.5), int(TILESIZE * 0.5)))
bCastleFigurine = pygame.transform.scale(pygame.image.load("piecesFigurines/bCastleFigurine.png"), (int(TILESIZE * 0.5), int(TILESIZE * 0.5)))
nothingness = pygame.image.load("piecesFigurines/nothingness.png")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT = (235, 236, 208)
DARK = (115, 149, 82)
LIGHTSELECT = (202, 203, 179)
DARKSELECT = (99, 128, 70)
ULTRADARK = (38, 36, 33)
ULTRALIGHT = (217, 219, 222)
BACKGROUND = (48, 46, 43)
LIGHTGREY = (200, 200, 200)
DARKGREY = (150, 150, 150)
HISTORICSELECTGREY = (72, 71, 69)
HISTORICSELECTLIGHTGREY = (91, 90, 88)
ORANGERGBA = (237, 127, 16, 128)
HISTORICLIGHTBG = (42, 41, 38)
HISTORICDARKBG = (38, 37, 34)
HISTORICSECONDARY = (144, 146, 140)

# Create a surface with per-pixel alpha
darkSurfaceRGBA = pygame.Surface((TILESIZE, TILESIZE), pygame.SRCALPHA)
lightSurfaceRGBA = pygame.Surface((TILESIZE, TILESIZE), pygame.SRCALPHA)
arrowSurfaceRGBA = pygame.Surface((TILESIZE * 8, TILESIZE * 8), pygame.SRCALPHA)

# Draw a semi-transparent circle (RGBA) on canCaptureSurfaceRGBA
pygame.draw.circle(darkSurfaceRGBA, (99, 128, 70, 192), (TILESIZE // 2, TILESIZE // 2), TILESIZE // 2, TILESIZE // 10)
pygame.draw.circle(lightSurfaceRGBA, (202, 203, 179, 192), (TILESIZE // 2, TILESIZE // 2), TILESIZE // 2, TILESIZE // 10)

# Define text
pygame.font.init()
robotoFont = pygame.font.Font('fonts/Roboto_Condensed-Regular.ttf', int(50 * SCALE))
robotoMedium = pygame.font.Font('fonts/Roboto-Medium.ttf', int(25 * SCALE))

# Define tiles size
ROWS, COLS = 8, 8

promoImageSize = TILESIZE
promoImageSpacing = int(5 * SCALE)
promoInnerMargin = int(10 * SCALE)

promoBlockWidth = promoImageSize + 2 * promoInnerMargin
promoBlockHeight = 4 * promoImageSize + (4 - 1) * promoImageSpacing + 2 * promoInnerMargin

promoBlockX = LEFTMARGIN + 4 * TILESIZE - promoBlockWidth // 2
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

pieces = [
    {'name': 'whiteQueen', 'img': wq, 'pos': (int(WIDTH / 2), int(HEIGHT / 2 - promoImageSize * 1.5 + promoImageSpacing))},
    {'name': 'whiteKnight', 'img': wn, 'pos': (int(WIDTH / 2), int(HEIGHT / 2 - promoImageSize * 0.5 + promoImageSpacing))},
    {'name': 'whiteRook', 'img': wr, 'pos': (int(WIDTH / 2), int(HEIGHT / 2 + promoImageSize * 0.5 + promoImageSpacing))},
    {'name': 'whiteBishop', 'img': wb, 'pos': (int(WIDTH / 2), int(HEIGHT / 2 + promoImageSize * 1.5 + promoImageSpacing))},
    {'name': 'blackQueen', 'img': bq, 'pos': (int(WIDTH / 2), int(HEIGHT / 2 - promoImageSize * 1.5 + promoImageSpacing))},
    {'name': 'blackKnight', 'img': bn, 'pos': (int(WIDTH / 2), int(HEIGHT / 2 - promoImageSize * 0.5 + promoImageSpacing))},
    {'name': 'blackRook', 'img': br, 'pos': (int(WIDTH / 2), int(HEIGHT / 2 + promoImageSize * 0.5 + promoImageSpacing))},
    {'name': 'blackBishop', 'img': bb, 'pos': (int(WIDTH / 2), int(HEIGHT / 2 + promoImageSize * 1.5 + promoImageSpacing))},
]

for i in range(len(pieces)):
    pos = promoIconPos[i % 4]
    img = pieces[i]['img']
    img_rect = img.get_rect(center=pos)
    pieces[i]['rect'] = img_rect

historicScroll = 0
    
def drawBoard(game, skipPiece=None):
    game.fill(BACKGROUND)
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 1:
                pygame.draw.rect(game, DARK, (col * TILESIZE, TOPMARGIN + row * TILESIZE, TILESIZE, TILESIZE))
            else:
                pygame.draw.rect(game, LIGHT, (col * TILESIZE, TOPMARGIN + row * TILESIZE, TILESIZE, TILESIZE))

            # Draw tiles
            currentLoadingPiece = displayedBoard.matrix[row][col]
            if currentLoadingPiece:
                if skipPiece:
                    if not(skipPiece.getCoordX() == currentLoadingPiece.getCoordX() and skipPiece.getCoordY() == currentLoadingPiece.getCoordY()):
                        game.blit(getPieceImage(currentLoadingPiece), (currentLoadingPiece.rectX, currentLoadingPiece.rectY))
                else:
                    game.blit(getPieceImage(currentLoadingPiece), (currentLoadingPiece.rectX, currentLoadingPiece.rectY))

def setPiecesCoordinates():
    """
    Initialize pieces coordinates for display
    """
    for row in range(ROWS):
        for col in range(COLS):
            currentLoadingPiece = displayedBoard.matrix[row][col]
            if currentLoadingPiece is not None:
                currentLoadingPiece.rectX = col * TILESIZE + LEFTMARGIN
                currentLoadingPiece.rectY = row * TILESIZE + TOPMARGIN

def getTileColor(coordinates):
    y = coordinates[0]
    x = coordinates[1]
    return 'LIGHT' if (y + x) % 2 == 0 else 'DARK'

def displayAvailableMoves(availableMoves, selectedTile):
    for move in availableMoves:
        y, x = move
        target = displayedBoard.matrix[y][x]
        if target and selectedTile:
            if target.getColor() != selectedTile.getColor():
                if getTileColor(move) == 'DARK':
                    GAME.blit(darkSurfaceRGBA, (LEFTMARGIN + x * TILESIZE, TOPMARGIN + y * TILESIZE))
                else:
                    GAME.blit(lightSurfaceRGBA, (LEFTMARGIN + x * TILESIZE, TOPMARGIN + y * TILESIZE))
            else:
                display_assistant.drawPossibleTile(GAME, move)
        else:
            display_assistant.drawPossibleTile(GAME, move)

def tryDrawPromotionMenu(promotingPawn):
    promoIconRects.clear()
    if promotingPawn is not None and promotingPawn.name == '' and promotingPawn.isAbleToPromote():
        pygame.draw.rect(GAME, WHITE, promoBackground)
        for idx, img in enumerate(promoOrder[promotingPawn.getColor()]):
            img = pygame.transform.scale(img, (promoImageSize, promoImageSize))
            pos = promoIconPos[idx]
            rectBg = pygame.Rect(pos[0] - TILESIZE // 2, pos[1], TILESIZE, TILESIZE)
            pygame.draw.rect(GAME, LIGHTGREY, rectBg)
            GAME.blit(img, (pos[0] - TILESIZE // 2, pos[1]))
            promoIconRects.append((rectBg, ['queen','knight','rook','bishop'][idx]))

def tryMoveThroughHistoric(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:  # Go back one move
            if len(displayedBoard.boardHistoric) > 1 and displayedBoard.historicIndic > 0:
                displayedBoard.historicIndic -= 1
                displayedBoard.matrix = displayedBoard.boardHistoric[displayedBoard.historicIndic]
                setPiecesCoordinates()
                displayedBoard.playSound(displayedBoard.soundHistoric[displayedBoard.historicIndic])

        if event.key == pygame.K_RIGHT:  # Go forward one move
            if len(displayedBoard.boardHistoric) - 1 > displayedBoard.historicIndic:
                displayedBoard.historicIndic += 1
                displayedBoard.matrix = displayedBoard.boardHistoric[displayedBoard.historicIndic]
                setPiecesCoordinates()
                displayedBoard.playSound(displayedBoard.soundHistoric[displayedBoard.historicIndic - 1])

        if event.key == pygame.K_UP:  # Go to the last move
            if len(displayedBoard.boardHistoric) > 0 and displayedBoard.historicIndic != len(displayedBoard.boardHistoric) - 1:
                displayedBoard.historicIndic = len(displayedBoard.boardHistoric) - 1
                displayedBoard.matrix = displayedBoard.boardHistoric[displayedBoard.historicIndic]
                setPiecesCoordinates()
                displayedBoard.playSound('')

        if event.key == pygame.K_DOWN:  # Go to the first move
            if len(displayedBoard.boardHistoric) > 0 and displayedBoard.historicIndic != 0:
                displayedBoard.historicIndic = 0
                displayedBoard.matrix = displayedBoard.boardHistoric[displayedBoard.historicIndic]
                setPiecesCoordinates()
                displayedBoard.playSound('')


def getPieceImage(piece):
    """
    Get the image of a piece based on its color and name.
    """
    if piece.getColor() == 'black':
        if piece.name == 'N':
            return bn
        elif piece.name == 'R':
            return br
        elif piece.name == '':
            return bp
        elif piece.name == 'B':
            return bb
        elif piece.name == 'Q':
            return bq
        elif piece.name == 'K':
            return bk
    else:
        if piece.name == 'N':
            return wn
        elif piece.name == 'R':
            return wr
        elif piece.name == '':
            return wp
        elif piece.name == 'B':
            return wb
        elif piece.name == 'Q':
            return wq
        elif piece.name == 'K':
            return wk
    return None


def slidePieceToTile(piece, targetTile):
    """
    Slide a piece to a target tile.
    """
    startX, startY = piece.getCoordX() * TILESIZE + LEFTMARGIN, piece.getCoordY() * TILESIZE + TOPMARGIN
    targetX, targetY = targetTile[0] * TILESIZE + LEFTMARGIN, targetTile[1] * TILESIZE + TOPMARGIN
    deltaX, deltaY = targetX - startX, targetY - startY

    steps = 12  # Number of steps for the sliding animation
    for step in range(steps):
        piece.rectX += deltaX / steps
        piece.rectY += deltaY / steps
        drawBoard(GAME, skipPiece=piece)
        chessClock.drawClock(GAME, TOPMARGIN, LEFTMARGIN, TILESIZE, 'white', ULTRADARK, ULTRALIGHT)
        chessClock.drawClock(GAME, TOPMARGIN, LEFTMARGIN, TILESIZE, 'black', ULTRALIGHT, ULTRADARK)
        drawHistoric(moveList)
        GAME.blit(getPieceImage(piece), (piece.rectX, piece.rectY))
        GAME.blit(arrowSurfaceRGBA, (LEFTMARGIN, TOPMARGIN))
        pygame.display.flip()
        pygame.time.delay(4)  # Delay for animation effect

def drawFigurine(move, col):
    if col == 0:
        if move[0] == 'R':
            return wrFigurine
        elif move[0] == 'N':
            return wnFigurine
        elif move[0] == 'B':
            return wbFigurine
        elif move[0] == 'Q':
            return wqFigurine
        elif move[0] == 'K':
            return wkFigurine
        elif move[0] == 'O':
            return wCastleFigurine
        else:
            return wpFigurine
    else:
        if move[0] == 'R':
            return brFigurine
        elif move[0] == 'N':
            return bnFigurine
        elif move[0] == 'B':
            return bbFigurine
        elif move[0] == 'Q':
            return bqFigurine
        elif move[0] == 'K':
            return bkFigurine
        elif move[0] == '0' or move[0] == 'O':
            return bCastleFigurine
        else:
            return bpFigurine

def drawHistoric(moveList):
    pygame.draw.rect(GAME, HISTORICDARKBG, (WIDTH - RIGHTMARGIN + TILESIZE // 4, TOPMARGIN + int(10 * SCALE), int(3 * TILESIZE), HEIGHT - TOPMARGIN - BOTTOMMARGIN - int(20 * SCALE)), 0, int(15 * SCALE))
    pygame.draw.aaline(GAME, HISTORICSECONDARY, (WIDTH - RIGHTMARGIN + TILESIZE // 4 + int(25 * SCALE), TOPMARGIN + int(40 * SCALE)), (WIDTH - RIGHTMARGIN + TILESIZE // 4 + int(275 * SCALE), TOPMARGIN + int(40 * SCALE)))
    pygame.draw.aaline(GAME, HISTORICSECONDARY, (WIDTH - RIGHTMARGIN + TILESIZE // 4 + int(25 * SCALE), TOPMARGIN + int(100 * SCALE)), (WIDTH - RIGHTMARGIN + TILESIZE // 4 + int(275 * SCALE), TOPMARGIN + int(100 * SCALE)))

    historicTitle = robotoMedium.render("Moves History", True, LIGHTGREY)
    GAME.blit(historicTitle, (WIDTH - RIGHTMARGIN + TILESIZE // 4 + int(70 * SCALE), TOPMARGIN + int(55 * SCALE)))

    for i, move in enumerate(moveList):
        col = i % 2
        row = i // 2
        textPosX = WIDTH - RIGHTMARGIN + col * (TILESIZE * 1.3) + int(120 * SCALE)
        textPosY = TOPMARGIN + row * (TILESIZE // 2) + int(120 * SCALE) + historicScroll
        counterText = robotoMedium.render(str(row + 1) + ".", True, HISTORICSECONDARY)
        if col == 0:
            if row % 2 == 0:
                pygame.draw.rect(GAME, HISTORICLIGHTBG, (WIDTH - RIGHTMARGIN + TILESIZE // 4, textPosY, int(3 * TILESIZE), TILESIZE // 2))
                GAME.blit(counterText, (WIDTH - RIGHTMARGIN + int(40 * SCALE), textPosY + int(11 * SCALE)))
            else:
                pygame.draw.rect(GAME, HISTORICDARKBG, (WIDTH - RIGHTMARGIN + TILESIZE // 4, textPosY, int(3 * TILESIZE), TILESIZE // 2))
                GAME.blit(counterText, (WIDTH - RIGHTMARGIN + int(40 * SCALE), textPosY + int(11 * SCALE)))

        sizeX, sizeY = robotoMedium.size(move)
        if i == displayedBoard.historicIndic - 1:
            pygame.draw.rect(GAME, HISTORICSELECTLIGHTGREY, (textPosX - int(37 * SCALE), textPosY + int(15 * SCALE), sizeX + int(38 * SCALE), sizeY), border_radius=int(4 * SCALE))
            pygame.draw.rect(GAME, HISTORICSELECTGREY, (textPosX - int(37 * SCALE), textPosY + int(8 * SCALE), sizeX + int(38 * SCALE), sizeY + int(4 * SCALE)), border_radius=int(4 * SCALE))

        moveTextFont = pygame.font.Font('fonts/Roboto-Medium.ttf', int(21 * SCALE))
        moveText = moveTextFont.render(move, True, LIGHTGREY)
        GAME.blit(moveText, (textPosX, textPosY + int(13 * SCALE)))
        GAME.blit(pygame.transform.scale(drawFigurine(move, col), (int(TILESIZE * 0.35), int(TILESIZE * 0.35))), (textPosX - int(35 * SCALE), textPosY + int(6 * SCALE)))

display_assistant.displayAssistantConstructor(TILESIZE, TOPMARGIN, LEFTMARGIN, LIGHTSELECT, DARKSELECT)
adjustPromoSize()

def slideBothPiecesToTile(piece1, piece2, targetTile1, targetTile2):
    """
    Slide two pieces to their respective target tiles.
    """
    startX1, startY1 = piece1.getCoordX() * TILESIZE + LEFTMARGIN, piece1.getCoordY() * TILESIZE + TOPMARGIN
    startX2, startY2 = piece2.getCoordX() * TILESIZE + LEFTMARGIN, piece2.getCoordY() * TILESIZE + TOPMARGIN
    targetX1, targetY1 = targetTile1[0] * TILESIZE + LEFTMARGIN, targetTile1[1] * TILESIZE + TOPMARGIN
    targetX2, targetY2 = targetTile2[0] * TILESIZE + LEFTMARGIN, targetTile2[1] * TILESIZE + TOPMARGIN
    deltaX1, deltaY1 = targetX1 - startX1, targetY1 - startY1
    deltaX2, deltaY2 = targetX2 - startX2, targetY2 - startY2

    steps = 12  # Number of steps for the sliding animation
    for step in range(steps):
        piece1.rectX += deltaX1 / steps
        piece1.rectY += deltaY1 / steps
        piece2.rectX += deltaX2 / steps
        piece2.rectY += deltaY2 / steps
        drawBoard(GAME)
        chessClock.drawClock(GAME, TOPMARGIN, LEFTMARGIN, TILESIZE, 'white', ULTRADARK, ULTRALIGHT)
        chessClock.drawClock(GAME, TOPMARGIN, LEFTMARGIN, TILESIZE, 'black', ULTRALIGHT, ULTRADARK)
        drawHistoric(moveList)
        GAME.blit(getPieceImage(piece1), (piece1.rectX, piece1.rectY))
        GAME.blit(getPieceImage(piece2), (piece2.rectX, piece2.rectY))
        GAME.blit(arrowSurfaceRGBA, (LEFTMARGIN, TOPMARGIN))
        pygame.display.flip()
        pygame.time.delay(4)  # Delay for animation effect

def hasSomeoneWon(clock):
    isSomeoneTimeUp = clock.checkClock0()
    if isSomeoneTimeUp != False and isSomeoneTimeUp == 'black':
        return 'white'
    elif isSomeoneTimeUp != False and isSomeoneTimeUp == 'white':
        return 'black'
    
    blackKing = displayedBoard.bk
    whiteKing = displayedBoard.wk
    isWhiteCheckemated = displayedBoard.checkMate(whiteKing)
    isBlackCheckemated = displayedBoard.checkMate(blackKing)
    if isWhiteCheckemated and not isBlackCheckemated:
        return 'black'
    elif not isWhiteCheckemated and isBlackCheckemated:
        return 'white'
        
def drawEndGameScreen(winner):
    import end_screen
    winCondition = "temp win condition"
    end_screen.drawEndScreen(GAME, winner, winCondition, SCALE, TILESIZE)

def main(clockTime, clockIncrement):
    global displayedBoard, chessClock, historicScroll, moveList
    adjustPromoSize()
    adjustWindowSize(WIDTH, HEIGHT)
    clock = pygame.time.Clock()
    run = True
    moveList = []
    selectedTile = None
    availableMoves = []
    firstMovePlayed = False
    rightClickDown = False
    arrows = []
    promotingPawn = None
    clockTime, clockIncrement = (3, 5)
    chessClock = chess_clock.chessClock(clockTime, clockIncrement)
    displayedBoard = board.board()
    displayedBoard.fillBoard()
    movingPiece = False
    canPlay = True
    setPiecesCoordinates()

    while run:
        clock.tick(60)  # 60 FPS cap

        if displayedBoard.historicIndic != len(displayedBoard.boardHistoric) - 1:
            canPlay = False
        else:
            canPlay = True

        drawBoard(GAME)

        displayAvailableMoves(availableMoves, selectedTile)

        arrowSurfaceRGBA = pygame.Surface((TILESIZE * 8, TILESIZE * 8), pygame.SRCALPHA)

        for arrow in arrows:
            display_assistant.drawArrow(arrowSurfaceRGBA, ORANGERGBA, arrow[0], arrow[1], TILESIZE / 5, 43 * TILESIZE / 100, 35.5)

        GAME.blit(arrowSurfaceRGBA, (LEFTMARGIN, TOPMARGIN))

        if firstMovePlayed:
            chessClock.updateTime()
            chessClock.updateLastTime()

            chessClock.drawClock(GAME, TOPMARGIN, LEFTMARGIN, TILESIZE, 'white', ULTRADARK, ULTRALIGHT)
            chessClock.drawClock(GAME, TOPMARGIN, LEFTMARGIN, TILESIZE, 'black', ULTRALIGHT, ULTRADARK)

        tryDrawPromotionMenu(promotingPawn)

        drawHistoric(moveList)
        
        potentialWinner = hasSomeoneWon(chessClock)
        
        if potentialWinner is not None:
            endScreenDef = end_screen.EndScreen(potentialWinner, "test", WIDTH, HEIGHT, TILESIZE)
            endScreenDef.defineButtons(SCALE, TILESIZE, WIDTH, HEIGHT)
            endScreenDef.draw(GAME, SCALE, TILESIZE)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            
            if potentialWinner is None:

                tryMoveThroughHistoric(event)

                if event.type == pygame.VIDEORESIZE:
                    adjustWindowSize(event.w, event.h)
                    adjustPromoSize()
                    setPiecesCoordinates()
                    display_assistant.displayAssistantConstructor(TILESIZE, TOPMARGIN, LEFTMARGIN, LIGHTSELECT, DARKSELECT)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and firstMovePlayed and not rightClickDown:
                    rightClickDown = True
                    mouseX, mouseY = pygame.mouse.get_pos()

                    mouseXTab = int((mouseX - LEFTMARGIN) / TILESIZE)
                    mouseYTab = int((mouseY - TOPMARGIN) / TILESIZE)

                    if 0 <= mouseXTab <= 7 and 0 <= mouseYTab <= 7:
                        arrowStart = (mouseYTab, mouseXTab)                

                if event.type == pygame.MOUSEWHEEL:
                    maxScroll = 0
                    extraSpace = 3 * (TILESIZE // 2)
                    minScroll = min(0, HEIGHT - (len(moveList) // 2) * (TILESIZE // 2) - 150 - extraSpace)
                    historicScroll = max(minScroll, min(maxScroll, historicScroll + event.y * 20 * SCALE))

                if event.type == pygame.MOUSEBUTTONUP and event.button == 3 and firstMovePlayed and rightClickDown:
                    rightClickDown = False
                    mouseX, mouseY = pygame.mouse.get_pos()

                    mouseXTab = int((mouseX - LEFTMARGIN) / TILESIZE)
                    mouseYTab = int((mouseY - TOPMARGIN) / TILESIZE)

                    if 0 <= mouseXTab <= 7 and 0 <= mouseYTab <= 7 and (mouseYTab, mouseXTab) != arrowStart:
                        arrowEnd = (mouseYTab, mouseXTab)

                        if (arrowStart, arrowEnd) in arrows:
                            arrows.pop(arrows.index((arrowStart, arrowEnd)))
                        else:
                            arrows.append((arrowStart, arrowEnd))

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    arrows = []

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and canPlay:
                    mouseX, mouseY = pygame.mouse.get_pos()

                    if LEFTMARGIN < mouseX < WIDTH - RIGHTMARGIN and TOPMARGIN < mouseY < HEIGHT - BOTTOMMARGIN:
                        mouseXTab = int((mouseX - LEFTMARGIN) / TILESIZE)
                        mouseYTab = int((mouseY - TOPMARGIN) / TILESIZE)
                        lastSelectedTile = deepcopy(selectedTile)

                        selectedTile, movingPiece = displayedBoard.manageSelection(selectedTile, mouseYTab, mouseXTab)

                        if movingPiece:
                            if selectedTile.canMove(mouseYTab, mouseXTab, displayedBoard) and selectedTile.getColor() == displayedBoard.turn:
                                actList = (displayedBoard.getActTypes(selectedTile, mouseYTab, mouseXTab)).split(',')

                                if displayedBoard.isCastleMove(lastSelectedTile, mouseXTab):

                                    if selectedTile.getCoordX() > mouseXTab:
                                        rook = displayedBoard.matrix[mouseYTab][0]
                                        slideBothPiecesToTile(rook, selectedTile, (mouseXTab + 1, mouseYTab), (mouseXTab, mouseYTab))

                                        displayedBoard.movePiece(selectedTile, mouseYTab, mouseXTab)
                                        displayedBoard.movePiece(rook, mouseYTab, mouseXTab + 1, doSound=False)

                                    else:
                                        rook = displayedBoard.matrix[mouseYTab][7]
                                        slideBothPiecesToTile(rook, selectedTile, (mouseXTab - 1, mouseYTab), (mouseXTab, mouseYTab))

                                        displayedBoard.movePiece(selectedTile, mouseYTab, mouseXTab)
                                        displayedBoard.movePiece(rook, mouseYTab, mouseXTab - 1, doSound=False)

                                else:
                                    slidePieceToTile(selectedTile, (mouseXTab, mouseYTab))
                                    displayedBoard.movePiece(selectedTile, mouseYTab, mouseXTab)

                                if len(moveList) == 0:
                                    firstMovePlayed = True
                                    chessClock.updateLastTime()

                                if selectedTile.name == '' and selectedTile.isAbleToPromote():
                                    promotingPawn = selectedTile
                                selectedTile = None
                                
                        availableMoves = displayedBoard.getAvailableMoves(selectedTile)

                    if promoIconRects:  # if a pawn is promoting
                        for rect, pieceName in promoIconRects:
                            if rect.collidepoint((mouseX, mouseY)):
                                displayedBoard.promote(promotingPawn, pieceName)
                                if displayedBoard.turn == 'white':
                                    chessClock.whiteTime += chessClock.increment
                                else:
                                    chessClock.blackTime += chessClock.increment

                                displayedBoard.switchTurn()
                                chessClock.setTurn(displayedBoard.turn)
                                displayedBoard.addMoveToHistoric(moveList, actList, promotingPawn, mouseYTab, mouseXTab)
                                setPiecesCoordinates()
                                displayedBoard.boardHistoric.append(deepcopy(displayedBoard.matrix))
                                displayedBoard.historicIndic = len(displayedBoard.boardHistoric) - 1
                                movingPiece = False
                                promoIconRects.clear()
                                promotingPawn = None
                                availableMoves = []

                    if movingPiece and not promotingPawn:
                        if displayedBoard.turn == 'white':
                            chessClock.whiteTime += chessClock.increment
                        else:
                            chessClock.blackTime += chessClock.increment

                        displayedBoard.switchTurn()
                        chessClock.setTurn(displayedBoard.turn)
                        setPiecesCoordinates()
                        displayedBoard.boardHistoric.append(deepcopy(displayedBoard.matrix))
                        displayedBoard.historicIndic = len(displayedBoard.boardHistoric) - 1
                        displayedBoard.addMoveToHistoric(moveList, actList, lastSelectedTile, mouseYTab, mouseXTab)
                        movingPiece = False
            else:
                if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    endScreenDef.handleEvents(event)

        pygame_widgets.update(events)
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main(0, 0)
