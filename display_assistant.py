import math
import pygame

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
        length =  2 * TILESIZE - headHeight / 2 + width / 2
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
            center = (arrowEndXY[0] - ((TILESIZE + width / 2) / 2) * (dX / abs(dX)), arrowEndXY[1])
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
            center = (arrowEndXY[0], arrowEndXY[1] - ((TILESIZE + width / 2) / 2) * (dY / abs(dY)))
            angle = angleY
            drawTiltedRect(surface, color, center, length, angle, width)

            # Setting arrow head angle
            return angle + math.radians(90)


def drawArrow(surface, color, start, end, width=20, headLength=40, headAngle=30):

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
        arrowEndWithHeadXY = (arrowEndXY[0] - headHeight * math.cos(angle), arrowEndXY[1] - headHeight * math.sin(angle)) # We remove some length so it doesn t go on arrow head
        
        center = ((arrowStartXY[0] + arrowEndXY[0]) / 2, (arrowStartXY[1] + arrowEndXY[1]) / 2) # head is part of the arrow
        length = ((arrowStartXY[0] - arrowEndWithHeadXY[0]) ** 2 + (arrowStartXY[1] - arrowEndWithHeadXY[1]) ** 2) ** (1/2)

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