import board
import datetime
import pygame
import sys
import pygame_widgets
from screeninfo import get_monitors
from pygame_widgets.button import Button
import display_assistant
from copy import deepcopy

# Initialize Pygame
pygame.init()

# Get monitor(s) specs
def getMonitorResolution():
    for m in get_monitors():
        if m.is_primary:
            return m.width, m.height


def adjustWindowSize(newWidth, newHeight):
    global WIDTH, HEIGHT, LEFTMARGIN, RIGHTMARGIN, TOPMARGIN, BOTTOMMARGIN, TILESIZE, SCALE, GAME, BIGCLOCKWIDTH, SMALLCLOCKWIDTH, BIGCLOCKPOS, SMALLCLOCKPOS, CLOCKHEIGHT, robotoFont
    global bp, bb, bk, bn, bq, br, wp, wb, wk, wn, wq, wr
    
    oldHeight = HEIGHT
    oldWidth = WIDTH
    if WIDTH == newWidth and HEIGHT != newHeight:
        SCALE = newHeight / oldHeight
    else:
        SCALE = newWidth / oldWidth
        
    HEIGHT = int(oldHeight * SCALE) // 8 * 8
    WIDTH = int(oldWidth * SCALE) // 8 * 8
    
    BASESCALE =  WIDTH / 800
    TILESIZE = int((WIDTH - LEFTMARGIN - RIGHTMARGIN) / 8)
    TOPMARGIN = TILESIZE
    BOTTOMMARGIN = TILESIZE
    LEFTMARGIN = 0
    RIGHTMARGIN = 0
    BIGCLOCKWIDTH, SMALLCLOCKWIDTH, CLOCKHEIGHT = int(150 * BASESCALE), int(125 * BASESCALE), int(54 * BASESCALE)
    BIGCLOCKPOS, SMALLCLOCKPOS = (int(615 * BASESCALE), int(23 * BASESCALE)), (int(630 * BASESCALE), int(23 * BASESCALE))

    GAME = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    
    robotoFont = pygame.font.SysFont('Roboto', int(50 * BASESCALE))
    
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


def adjustPromoSize():
    global pieces, promoImageSize, promoImageSpacing, promoInnerMargin, promoBlockWidth, promoBlockHeight, promoBlockX, promoBlockY, promoBackground, promoIconPos, promoOrder, promoIconRects, pos, img, img_rect
    global WIDTH, HEIGHT, SCALE, TILESIZE
    global wq, wn, wr, wb, bq, bn, br, bb
    
    promoImageSize = TILESIZE
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
SCALE = float(SCREENHEIGHT * 0.8) / 1000
TILESIZE = int(100 * SCALE)
TOPMARGIN = int(100 * SCALE)
BOTTOMMARGIN = int(100 * SCALE)
LEFTMARGIN = 0
RIGHTMARGIN = 0
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
ORANGERGBA = (237, 127, 16, 128)

# Create a surface with per-pixel alpha
darkSurfaceRGBA = pygame.Surface((TILESIZE, TILESIZE), pygame.SRCALPHA)
lightSurfaceRGBA = pygame.Surface((TILESIZE, TILESIZE), pygame.SRCALPHA)
arrowSurfaceRGBA = pygame.Surface((TILESIZE * 8, TILESIZE * 8), pygame.SRCALPHA)

# Draw a semi-transparent circle (RGBA) on canCaptureSurfaceRGBA
pygame.draw.circle(darkSurfaceRGBA, (99, 128, 70, 192), (TILESIZE // 2, TILESIZE // 2), TILESIZE // 2, TILESIZE // 10)
pygame.draw.circle(lightSurfaceRGBA, (202, 203, 179, 192), (TILESIZE // 2, TILESIZE // 2), TILESIZE // 2, TILESIZE // 10)

# Define text
pygame.font.init()
robotoFont = pygame.font.SysFont('Roboto', int(50 * SCALE))

# Define tiles size
ROWS, COLS = 8, 8

promoImageSize = TILESIZE
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

display_assistant.displayAssistantConstructor(TILESIZE, TOPMARGIN, LEFTMARGIN, LIGHTSELECT, DARKSELECT)
adjustPromoSize()


def drawBoard(game, skipPiece=None):
    game.fill(BACKGROUND)
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 1:
                pygame.draw.rect(game, DARK, (col * TILESIZE, TOPMARGIN + row * TILESIZE, TILESIZE, TILESIZE))
            else:
                pygame.draw.rect(game, LIGHT, (col * TILESIZE, TOPMARGIN + row * TILESIZE, TILESIZE, TILESIZE))

            # Draw tiles
            currentLoadingPiece = board.displayedBoard.matrix[row][col]
            if currentLoadingPiece:
                game.blit(getPieceImage(currentLoadingPiece), (currentLoadingPiece.rectX, currentLoadingPiece.rectY))

def setPiecesCoordinates():
    """
    Initialize pieces coordinates
    """
    for row in range(ROWS):
        for col in range(COLS):
            currentLoadingPiece = board.displayedBoard.matrix[row][col]
            if currentLoadingPiece is not None:
                currentLoadingPiece.rectX = col * TILESIZE + LEFTMARGIN
                currentLoadingPiece.rectY = row * TILESIZE + TOPMARGIN


def getTileColor(coordinates):
    y = coordinates[0]
    x = coordinates[1]
    return 'LIGHT' if (y + x) % 2 == 0 else 'DARK'


def displayTime(timer):
    BASESCALE = WIDTH / 800
    if timer >= 3600:
        pygame.draw.rect(GAME, ULTRADARK, (BIGCLOCKPOS[0], BIGCLOCKPOS[1], BIGCLOCKWIDTH, CLOCKHEIGHT))
        GAME.blit(robotoFont.render(str(datetime.timedelta(seconds=timer)), False, WHITE), (int(630 * BASESCALE), int(35 * BASESCALE)))
    else:
        pygame.draw.rect(GAME, ULTRADARK, (SMALLCLOCKPOS[0], SMALLCLOCKPOS[1], SMALLCLOCKWIDTH, CLOCKHEIGHT))
        GAME.blit(robotoFont.render(str(datetime.timedelta(seconds=timer))[2:], False, WHITE), (int(648 * BASESCALE), int(35 * BASESCALE)))


def displayAvailableMoves(availableMoves, selectedTile):
    for move in availableMoves:
        y, x = move
        target = board.displayedBoard.matrix[y][x]
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
            if len(board.displayedBoard.boardHistoric) > 1 and board.displayedBoard.historicIndic > 0:
                board.displayedBoard.historicIndic -= 1
                board.displayedBoard.matrix = board.displayedBoard.boardHistoric[board.displayedBoard.historicIndic]
                board.displayedBoard.playSound(board.displayedBoard.soundHistoric[board.displayedBoard.historicIndic])

        if event.key == pygame.K_RIGHT:  # Go forward one move
            if len(board.displayedBoard.boardHistoric) - 1 > board.displayedBoard.historicIndic:
                board.displayedBoard.historicIndic += 1
                board.displayedBoard.matrix = board.displayedBoard.boardHistoric[board.displayedBoard.historicIndic]
                board.displayedBoard.playSound(board.displayedBoard.soundHistoric[board.displayedBoard.historicIndic - 1])

        if event.key == pygame.K_UP:  # Go to the last move
            if len(board.displayedBoard.boardHistoric) > 0 and board.displayedBoard.historicIndic != len(board.displayedBoard.boardHistoric) - 1:
                board.displayedBoard.historicIndic = len(board.displayedBoard.boardHistoric) - 1
                board.displayedBoard.matrix = board.displayedBoard.boardHistoric[board.displayedBoard.historicIndic]
                board.displayedBoard.playSound('')

        if event.key == pygame.K_DOWN:  # Go to the first move
            if len(board.displayedBoard.boardHistoric) > 0 and board.displayedBoard.historicIndic != 0:
                board.displayedBoard.historicIndic = 0
                board.displayedBoard.matrix = board.displayedBoard.boardHistoric[board.displayedBoard.historicIndic]
                board.displayedBoard.playSound('')


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

    steps = 24  # Number of steps for the sliding animation
    for step in range(steps):
        piece.rectX += deltaX / steps
        piece.rectY += deltaY / steps
        drawBoard(GAME, skipPiece=piece)
        GAME.blit(getPieceImage(piece), (piece.rectX, piece.rectY))
        GAME.blit(arrowSurfaceRGBA, (LEFTMARGIN, TOPMARGIN))
        pygame.display.flip()
        pygame.time.delay(8)  # Delay for animation effect

    setPiecesCoordinates()  # Update the coordinates after sliding


def main():
    clock = pygame.time.Clock()
    run = True
    moveList = []
    selectedTile = None
    availableMoves = []
    firstMovePlayed = False
    rightClickDown = False
    arrows = []
    promotingPawn = None
    movingPiece = False
    canPlay = True
    setPiecesCoordinates()

    while run:
        clock.tick(60)  # 60 FPS cap

        if board.displayedBoard.historicIndic != len(board.displayedBoard.boardHistoric) - 1:
            canPlay = False
        else:
            canPlay = True

        drawBoard(GAME)

        displayAvailableMoves(availableMoves, selectedTile)
        
        arrowSurfaceRGBA = pygame.Surface((TILESIZE * 8, TILESIZE * 8), pygame.SRCALPHA)
        
        for arrow in arrows:
            display_assistant.drawArrow(arrowSurfaceRGBA, ORANGERGBA, arrow[0], arrow[1], TILESIZE / 5, 43 * TILESIZE / 100, 35.5)

        GAME.blit(arrowSurfaceRGBA, (LEFTMARGIN, TOPMARGIN))

        if not firstMovePlayed and len(moveList) != 0:
            firstMovePlayed = True
            initialTime = board.displayedBoard.initClock()
        elif firstMovePlayed:
            timer = board.displayedBoard.getClock(initialTime)
            displayTime(timer)

        tryDrawPromotionMenu(promotingPawn)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False

            tryMoveThroughHistoric(event)

            if event.type == pygame.VIDEORESIZE:
                adjustWindowSize(event.w, event.h)
                adjustPromoSize()
                display_assistant.displayAssistantConstructor(TILESIZE, TOPMARGIN, LEFTMARGIN, LIGHTSELECT, DARKSELECT)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and firstMovePlayed and not rightClickDown:
                rightClickDown = True
                mouseX, mouseY = pygame.mouse.get_pos()

                mouseXTab = int((mouseX - LEFTMARGIN) / TILESIZE)
                mouseYTab = int((mouseY - TOPMARGIN) / TILESIZE)

                if 0 <= mouseXTab <= 7 and 0 <= mouseYTab <= 7:
                    arrowStart = (mouseYTab, mouseXTab)
            
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
                    
                    selectedTile, movingPiece = board.displayedBoard.manageSelection(selectedTile, mouseYTab, mouseXTab)

                    if movingPiece:
                        if selectedTile.canMove(mouseYTab, mouseXTab, board.displayedBoard) and selectedTile.getColor() == board.displayedBoard.turn:
                            actList = (board.displayedBoard.getActTypes(selectedTile, mouseYTab, mouseXTab)).split(',')
                            board.displayedBoard.movePiece(selectedTile, mouseYTab, mouseXTab)
                            slidePieceToTile(lastSelectedTile, (mouseXTab, mouseYTab))
                            
                            if selectedTile.name == '' and selectedTile.isAbleToPromote():
                                promotingPawn = selectedTile
                            selectedTile = None
                            
                    availableMoves = board.displayedBoard.getAvailableMoves(selectedTile)

                if promoIconRects:  # if a pawn is promoting
                    for rect, pieceName in promoIconRects:
                        if rect.collidepoint((mouseX, mouseY)):
                            board.displayedBoard.promote(promotingPawn, pieceName)
                            board.displayedBoard.addMoveToHistoric(moveList, actList, promotingPawn, mouseYTab, mouseXTab)
                            board.displayedBoard.boardHistoric.append(deepcopy(board.displayedBoard.matrix))
                            board.displayedBoard.historicIndic = len(board.displayedBoard.boardHistoric) - 1
                            promoIconRects.clear()
                            movingPiece = False
                            promotingPawn = None
                            availableMoves = []
                            break
                    continue  # don't do anything if something else than a promotion is clicked

                if movingPiece and not promotingPawn:
                    board.displayedBoard.boardHistoric.append(deepcopy(board.displayedBoard.matrix))
                    board.displayedBoard.historicIndic = len(board.displayedBoard.boardHistoric) - 1
                    board.displayedBoard.addMoveToHistoric(moveList, actList, lastSelectedTile, mouseYTab, mouseXTab)
                    movingPiece = False

        pygame_widgets.update(events)
        pygame.display.update()

    pygame.quit()
    sys.exit()
 

if __name__ == "__main__":
    main()
