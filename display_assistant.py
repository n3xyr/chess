import math
import pygame
import json

def getColorsFromTheme(primary, secondary):
    #====== display_board ======#
    # primary select
    if sum(primary) / 3 >= 128:
        primarySelect = (max((primary[0] - 25), 0), max((primary[1] - 25), 0), max((primary[2] - 25), 0))
    else:
        primarySelect = (min((primary[0] + 25), 0), min((primary[1] + 25), 0), min((primary[2] + 25), 0))
        
    # secondary select
    if sum(secondary) / 3 >= 128:
        secondarySelect = (max((secondary[0] - 25), 0), max((secondary[1] - 25), 0), max((secondary[2] - 25), 0))
    else:
        secondarySelect = (min((secondary[0] + 25), 0), min((secondary[1] + 25), 0), min((secondary[2] + 25), 0))
        
    ultraDarkPrimary = ((primary[0] + 4 * 38) // 5, (primary[1] + 4 * 36) // 5, (primary[2] + 4 * 33) // 5)
    ultraLightSecondary = ((secondary[0] + 4 * 217) // 5, (secondary[1] + 4 * 219) // 5, (secondary[2] + 4 * 222) // 5)
    background = ((primary[0] + 4 * 48) // 5, (primary[1] + 4 * 46) // 5, (primary[2] + 4 * 43) // 5)
    historyDarkBg = (min(ultraDarkPrimary[0] + 1, 255), min(ultraDarkPrimary[1] + 1, 255), min(ultraDarkPrimary[2] + 1, 255))
    historyLightBg = (min(historyDarkBg[0] + 4, 255), min(historyDarkBg[1] + 4, 255), min(historyDarkBg[2] + 4, 255))
    historySelectDarkGrey = (min(historyDarkBg[0] + 34, 255), min(historyDarkBg[1] + 34, 255), min(historyDarkBg[2] + 34, 255))
    historySelectLightGrey = (min(historySelectDarkGrey[0] + 19, 255), min(historySelectDarkGrey[1] + 19, 255), min(historySelectDarkGrey[2] + 19, 255))
    historySecondary = (min(historyDarkBg[0] + 106, 255), min(historyDarkBg[1] + 106, 255), min(historyDarkBg[2] + 106, 255))
    
    #====== end_screen ======#
    endBoxOutline = (min(background[0] + 12, 255), min(background[1] + 12, 255), min(background[2] + 13, 255))
    endBoxOutlineTransparent = (min(background[0] + 12, 255), min(background[1] + 12, 255), min(background[2] + 13, 255), 240)
    endBoxBackground = (max(background[0] - 17, 0), max(background[1] - 15, 0), max(background[2] - 15, 0), 240)
    titleText = (min(background[0] + 169, 255), min(background[1] + 171, 255), min(background[2] + 174, 255))
    winConditionText = (min(background[0] + 96, 255), min(background[1] + 96, 255), min(background[2] + 96, 255))
    
    return {'white': (255, 255, 255),
            'black': (0, 0, 0),
            'lightgrey': (200, 200, 200),
            'darkgrey': (150, 150, 150),
            'orangeRGBA': (237, 127, 16, 127),
            'windowDarkTransparency': (0, 0, 0, 128),
            'primary': primary,
            'secondary': secondary,
            'primarySelect': primarySelect,
            'secondarySelect': secondarySelect,
            'ultraDarkPrimary': ultraDarkPrimary,
            'ultraLightSecondary': ultraLightSecondary,
            'background': background,
            'historyDarkBg': historyDarkBg,
            'historyLightBg': historyLightBg,
            'historySelectDarkGrey': historySelectDarkGrey,
            'historySelectLightGrey': historySelectLightGrey,
            'historySecondary': historySecondary}

def writeThemeColors(newColors):
    with open("theme.json", "w", encoding="utf-8") as f:
        json.dump(newColors, f, indent=4, ensure_ascii=False)

def displayAssistantConstructor(tileSize, topMargin, leftMargin, lightSelect, darkSelect):
    global TILESIZE, LIGHTSELECT, LEFTMARGIN, TOPMARGIN, DARKSELECT
    TILESIZE = tileSize
    LEFTMARGIN = leftMargin
    TOPMARGIN = topMargin
    LIGHTSELECT = lightSelect
    DARKSELECT = darkSelect


def getTileColor(coordinates):
    y = coordinates[0]
    x = coordinates[1]
    return 'LIGHT' if (y + x) % 2 == 0 else 'DARK'


def drawPossibleTile(game, tabCoordinates):
    if getTileColor(tabCoordinates) == 'LIGHT':
        pygame.draw.circle(game, LIGHTSELECT, (LEFTMARGIN + tabCoordinates[1] * TILESIZE + TILESIZE / 2, TOPMARGIN + tabCoordinates[0] * TILESIZE + TILESIZE/2), TILESIZE/6)
    else:
        pygame.draw.circle(game, DARKSELECT, (LEFTMARGIN + tabCoordinates[1] * TILESIZE + TILESIZE / 2, TOPMARGIN + tabCoordinates[0] * TILESIZE + TILESIZE/2), TILESIZE/6)


def drawTiltedRect(surface, color, center, height, angleRad, width = 20):
    cx, cy = center
    w2, h2 = width / 2, height / 2

    # Define rectangle corners (relative to center)
    corners = [
        (-w2, -h2),
        (w2, -h2),
        (w2, h2),
        (-w2, h2)
    ]

    # Rotate and translate corners
    rotated = []
    for x, y in corners:
        xr = x * math.cos(angleRad) - y * math.sin(angleRad)
        yr = x * math.sin(angleRad) + y * math.cos(angleRad)
        rotated.append((cx + xr, cy + yr))

    pygame.draw.polygon(surface, color, rotated)


def drawKnightArrow(surface, color, arrowStartXY, arrowEndXY, headHeight, width):
        length =  1.5 * TILESIZE + width
        dX = arrowEndXY[0] - arrowStartXY[0]
        dY = arrowEndXY[1] - arrowStartXY[1]

        angleX = math.atan2(dX, 0)
        angleY = math.atan2(0, dY)

        # First rectangle
        if abs(dX) < abs(dY):

            # First rectangle
            center = (arrowStartXY[0], arrowEndXY[1] + ((width - length) / 2) * (dY / abs(dY)))
            angle = angleX + math.radians(90)
            drawTiltedRect(surface, color, center, length, angle, width)

            # Second rectangle
            length = TILESIZE - headHeight + width / 2
            center = (arrowEndXY[0] - ((TILESIZE + width / 2 + headHeight) / 2) * (dX / abs(dX)), arrowEndXY[1])
            angle = angleX
            drawTiltedRect(surface, color, center, length, angle, width)

            # Setting arrow head angle
            return angle - math.radians(90)
        else:

            # First rectangle
            center = (arrowEndXY[0] + ((width - length) / 2) * (dX / abs(dX)), arrowStartXY[1])
            angle = angleY + math.radians(90)
            drawTiltedRect(surface, color, center, length, angle, width)

            # Second rectangle
            length = TILESIZE - headHeight + width / 2
            center = (arrowEndXY[0], arrowEndXY[1] - ((TILESIZE + width / 2 + headHeight) / 2) * (dY / abs(dY)))
            angle = angleY
            drawTiltedRect(surface, color, center, length, angle, width)

            # Setting arrow head angle
            return angle + math.radians(90)


def drawArrow(surface, color, start, end, width = 20, headLength=50, headAngle=30):

    headHeight = abs(headLength * math.cos(headAngle/2))

    arrowStartXY = (start[1] * TILESIZE + TILESIZE / 2, start[0] * TILESIZE + TILESIZE / 2)
    arrowEndXY = (end[1] * TILESIZE + TILESIZE / 2, end[0] * TILESIZE + TILESIZE / 2)
    knightMoves = [(start[0] + 2, start[1] + 1), (start[0] + 2, start[1] - 1), (start[0] - 2, start[1] + 1), (start[0] - 2, start[1] - 1), (start[0] + 1, start[1] + 2), (start[0] - 1, start[1] + 2), (start[0] + 1, start[1] - 2), (start[0] - 1, start[1] - 2)]

    if end in knightMoves:
        angle = drawKnightArrow(surface, color, arrowStartXY, arrowEndXY, headHeight, width)

    else:
        # Calculate direction vector
        dX = arrowEndXY[0] - arrowStartXY[0]
        dY = arrowEndXY[1] - arrowStartXY[1]
        angle = math.atan2(dY, dX)
        arrowAngle = angle + math.radians(90)
        
        # Drawing the rectangle
        rectEndXY = (arrowEndXY[0] - headHeight * math.cos(angle), arrowEndXY[1] - headHeight * math.sin(angle))
        rectStartXY = (arrowStartXY[0] + ((TILESIZE - width) / 2) * math.cos(angle), arrowStartXY[1] + ((TILESIZE - width) / 2) * math.sin(angle))

        length = ((rectEndXY[0] - rectStartXY[0]) ** 2 +(rectEndXY[1] - rectStartXY[1]) ** 2) ** (1/2)
        center = ((rectEndXY[0] + rectStartXY[0]) / 2, (rectEndXY[1] + rectStartXY[1]) / 2)

        drawTiltedRect(surface, color, center, length, arrowAngle, width)

    # Calculate arrowhead points
    angle1 = angle + math.radians(headAngle)
    angle2 = angle - math.radians(headAngle)

    x1 = arrowEndXY[0] - headLength * math.cos(angle1)
    y1 = arrowEndXY[1] - headLength * math.sin(angle1)
    x2 = arrowEndXY[0] - headLength * math.cos(angle2)
    y2 = arrowEndXY[1] - headLength * math.sin(angle2)

    # Draw triangle (arrowhead)
    pygame.draw.polygon(surface, color, [arrowEndXY, (x1, y1), (x2, y2)])