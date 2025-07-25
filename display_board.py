import board
import datetime
import pygame
import sys
import pygame_widgets
from screeninfo import get_monitors
from pygame_widgets.button import Button
import display_assistant

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
            

def tryPromotion(promotingPawn):
    promoIconRects.clear()
    if promotingPawn is not None and promotingPawn.name == 'P' and promotingPawn.isAbleToPromote():
        pygame.draw.rect(GAME, WHITE, promoBackground)
        for idx, img in enumerate(promoOrder[promotingPawn.getColor()]):
            img = pygame.transform.scale(img, (promoImageSize, promoImageSize))
            pos = promoIconPos[idx]
            rectBg = pygame.Rect(pos[0] - TILESIZE // 2, pos[1], TILESIZE, TILESIZE)
            pygame.draw.rect(GAME, LIGHTGREY, rectBg)
            GAME.blit(img, (pos[0] - TILESIZE // 2, pos[1]))
            promoIconRects.append((rectBg, ['queen','knight','rook','bishop'][idx]))


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

    while run:
        clock.tick(60)  # 60 FPS cap

        drawBoard(GAME)
        displayAvailableMoves(availableMoves, selectedTile)
        
        arrowSurfaceRGBA = pygame.Surface((TILESIZE * 8, TILESIZE * 8), pygame.SRCALPHA)
        
        for arrow in arrows:
            display_assistant.drawArrow(arrowSurfaceRGBA, ORANGERGBA, arrow[0], arrow[1])

        GAME.blit(arrowSurfaceRGBA, (LEFTMARGIN, TOPMARGIN))


        if not firstMovePlayed and len(moveList) != 0:
            firstMovePlayed = True
            initialTime, lastTime = board.displayedBoard.initClock()
        elif firstMovePlayed:
            timer = board.displayedBoard.getClock(initialTime)
            displayTime(timer)

        tryPromotion(promotingPawn)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                
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
                mouseX, mouseY = pygame.mouse.get_pos()
                arrows = []

                if promoIconRects:  # if a pawn is promoting
                    for rect, pieceName in promoIconRects:
                        if rect.collidepoint((mouseX, mouseY)):
                            board.displayedBoard.promote(promotingPawn, pieceName)
                            promoIconRects.clear()
                            promotingPawn = None
                            availableMoves = []
                            break
                    continue  # don't do anything if something else than a promotion is clicked

                if LEFTMARGIN < mouseX < WIDTH - RIGHTMARGIN and TOPMARGIN < mouseY < HEIGHT - BOTTOMMARGIN:
                    mouseXTab = int((mouseX - LEFTMARGIN) / TILESIZE)
                    mouseYTab = int((mouseY - TOPMARGIN) / TILESIZE)
                    clickedTile = board.displayedBoard.matrix[mouseYTab][mouseXTab]

                    if selectedTile:
                        if selectedTile.canMove(mouseYTab, mouseXTab, board.displayedBoard) and selectedTile.getColor() == board.displayedBoard.turn:
                            act = board.displayedBoard.movePiece(selectedTile, mouseYTab, mouseXTab)
                            if board.displayedBoard.matrix[mouseYTab][mouseXTab] is not None:
                                movedPiece = board.displayedBoard.matrix[mouseYTab][mouseXTab]

                            if movedPiece.name == 'P' and movedPiece.isAbleToPromote():
                                promotingPawn = movedPiece
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
                        availableMoves = selectedTile.possibleMoves(board.displayedBoard)
                    else:
                        availableMoves = []

        pygame_widgets.update(events)
        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
