import math
import pygame
import json

def getColorsFromTheme(primaryColor, secondaryColor):
    #====== display_board ======#
    primaryHSVColor = rgbToHsv(primaryColor)
    secondaryHSVColor = rgbToHsv(secondaryColor)
    
    # primary select
    if (sum(primaryColor) - 255) / 3 >= 128:
        primarySelectHSVColor = (primaryHSVColor[0], max(0, primaryHSVColor[1] - 0.25), primaryHSVColor[2] - 0.25)
        primarySelectColor = hsvToRgb(primarySelectHSVColor)
    else:
        primarySelectHSVColor = (primaryHSVColor[0], max(0, primaryHSVColor[1] - 0.25), primaryHSVColor[2] + 0.25)
        primarySelectColor = hsvToRgb(primarySelectHSVColor)
        
    # secondary select
    if (sum(secondaryColor) - 255) / 3 >= 128:
        secondarySelectHSVColor = (secondaryHSVColor[0], max(0, secondaryHSVColor[1] - 0.25), secondaryHSVColor[2] - 0.25)
        secondarySelectColor = hsvToRgb(secondarySelectHSVColor)
    else:
        secondarySelectHSVColor = (secondaryHSVColor[0], max(0, secondaryHSVColor[1] - 0.25), secondaryHSVColor[2] + 0.25)
        secondarySelectColor = hsvToRgb(secondarySelectHSVColor)
         
    ultraDarkPrimaryColor = ((primaryColor[0] + 7 * 38) // 8, (primaryColor[1] + 7 * 36) // 8, (primaryColor[2] + 7 * 33) // 8)
    ultraLightSecondaryColor = ((secondaryColor[0] + 7 * 217) // 8, (secondaryColor[1] + 7 * 219) // 8, (secondaryColor[2] + 7 * 222) // 8)
    backgroundColor = ((primaryColor[0] + 7 * 48) // 8, (primaryColor[1] + 7 * 46) // 8, (primaryColor[2] + 7 * 43) // 8)
    historyDarkBgColor = (min(ultraDarkPrimaryColor[0] + 1, 255), min(ultraDarkPrimaryColor[1] + 1, 255), min(ultraDarkPrimaryColor[2] + 1, 255))
    historyLightBgColor = (min(historyDarkBgColor[0] + 4, 255), min(historyDarkBgColor[1] + 4, 255), min(historyDarkBgColor[2] + 4, 255))
    historySelectDarkGreyColor = (min(historyDarkBgColor[0] + 34, 255), min(historyDarkBgColor[1] + 34, 255), min(historyDarkBgColor[2] + 34, 255))
    historySelectLightGreyColor = (min(historySelectDarkGreyColor[0] + 19, 255), min(historySelectDarkGreyColor[1] + 19, 255), min(historySelectDarkGreyColor[2] + 19, 255))
    historySecondaryColor = (min(historyDarkBgColor[0] + 106, 255), min(historyDarkBgColor[1] + 106, 255), min(historyDarkBgColor[2] + 106, 255))
    
    #====== end_screen ======#
    endBoxOutlineColor = (min(backgroundColor[0] + 12, 255), min(backgroundColor[1] + 12, 255), min(backgroundColor[2] + 13, 255))
    endBoxOutlineTransparentColor = (min(backgroundColor[0] + 12, 255), min(backgroundColor[1] + 12, 255), min(backgroundColor[2] + 13, 255), 240)
    endBoxBackgroundColor= (max(backgroundColor[0] - 17, 0), max(backgroundColor[1] - 15, 0), max(backgroundColor[2] - 15, 0), 240)
    titleTextColor = (min(backgroundColor[0] + 169, 255), min(backgroundColor[1] + 171, 255), min(backgroundColor[2] + 174, 255))
    winConditionTextColor = (min(backgroundColor[0] + 96, 255), min(backgroundColor[1] + 96, 255), min(backgroundColor[2] + 96, 255))
    crossColor = winConditionTextColor

    # main button
    mainButtonSecondaryHSVColor = ((primaryHSVColor[0] + 61) % 360, min(primaryHSVColor[1] + 0.53, 1), max(primaryHSVColor[2] - 0.26, 0))
    mainButtonSecondaryColor = hsvToRgb(mainButtonSecondaryHSVColor)
    
    mainButtonPrimaryHSVColor = ((primaryHSVColor[0] + 58) % 360, min(primaryHSVColor[1] + 0.44, 1), min(primaryHSVColor[2] + 0.1, 1))
    mainButtonPrimaryColor = hsvToRgb(mainButtonPrimaryHSVColor)
        
    # normal button
    normalButtonPrimaryColor = (min(backgroundColor[0] + 46, 255), min(backgroundColor[1] + 47, 255), min(backgroundColor[2] + 48, 255))
    normalButtonSecondaryColor = backgroundColor
    
    #====== menu ======#
    panelBgColor = endBoxBackgroundColor
    borderColor = normalButtonPrimaryColor
    buttonBgColor = (min(backgroundColor[0] + 2, 255), min(backgroundColor[1] + 4, 255), min(backgroundColor[2] + 7, 255))
    buttonTextColor = (min(backgroundColor[0] + 102, 255), min(backgroundColor[1] + 104, 255), min(backgroundColor[2] + 107, 255))
    textboxBgColor = (max(backgroundColor[0] - 15, 0), max(backgroundColor[1] - 15, 0), max(backgroundColor[2] - 14, 0), 240)
    textboxTextColor = borderColor
    textboxTextLineColor = (borderColor[0], borderColor[1], borderColor[2], 102)
    linkColor = (min(backgroundColor[0] + 150, 255), min(backgroundColor[1] + 152, 255), min(backgroundColor[2] + 155, 255))
    
    #====== settings_menu ======#
    fullTransparencyColor = (0, 0, 0, 0)
    settingsContainerBorderColor = (min(backgroundColor[0] + 104, 255), min(backgroundColor[1] + 106, 255), min(backgroundColor[2] + 109, 255), 100)
    settingsContainerBoxColor = (max(backgroundColor[0] - 38, 0), max(backgroundColor[1] - 36, 0), max(backgroundColor[2] - 33, 0), 100)
    categoryBodyBackgroundColor = (max(backgroundColor[0] - 10, 0), max(backgroundColor[1] - 9, 0), max(backgroundColor[2] - 9, 0))
    categoryTitleColor = (min(backgroundColor[0] + 170, 255), min(backgroundColor[1] + 172, 255), min(backgroundColor[2] + 175, 255))
    categoryHeaderColor = (min(backgroundColor[0] + 5, 255), min(backgroundColor[1] + 5, 255), min(backgroundColor[2] + 3, 255))
    accentColor = primaryColor
    subCatTitleTextColor = buttonTextColor
    subCatLineColor = borderColor
    switchCircleColor = (min(backgroundColor[0] + 169, 255), min(backgroundColor[1] + 171, 255), min(backgroundColor[2] + 174, 255))
    arrowBackgroundColor = (min(backgroundColor[0] + 25, 255), min(backgroundColor[1] + 24, 255), min(backgroundColor[2] + 21, 255))
    arrowColor = (min(backgroundColor[0] + 129, 255), min(backgroundColor[1] + 131, 255), min(backgroundColor[2] + 134, 255))
    
    return {'white': (255, 255, 255),
            'black': (0, 0, 0),
            'lightgrey': (200, 200, 200),
            'darkgrey': (150, 150, 150),
            'orangeRGBA': (237, 127, 16, 127),
            'windowDarkTransparency': (0, 0, 0, 128),
            'primary': primaryColor,
            'secondary': secondaryColor,
            'primarySelect': primarySelectColor,
            'secondarySelect': secondarySelectColor,
            'ultraDarkPrimary': ultraDarkPrimaryColor,
            'ultraLightSecondary': ultraLightSecondaryColor,
            'background': backgroundColor,
            'historyDarkBg': historyDarkBgColor,
            'historyLightBg': historyLightBgColor,
            'historySelectDarkGrey': historySelectDarkGreyColor,
            'historySelectLightGrey': historySelectLightGreyColor,
            'historySecondary': historySecondaryColor,
            'endBoxOutline': endBoxOutlineColor,
            'endBoxOutlineTransparent': endBoxOutlineTransparentColor,
            'endBoxBackground': endBoxBackgroundColor,
            'titleText': titleTextColor,
            'winConditionText': winConditionTextColor,
            'cross': crossColor,
            'mainButtonSecondary': mainButtonSecondaryColor,
            'mainButtonPrimary': mainButtonPrimaryColor,
            'normalButtonPrimary': normalButtonPrimaryColor,
            'normalButtonSecondary': normalButtonSecondaryColor,
            'panelBg': panelBgColor,
            'border': borderColor,
            'buttonBg': buttonBgColor,
            'buttonText': buttonTextColor,
            'textboxBg': textboxBgColor,
            'textboxText': textboxTextColor,
            'textboxTextLine': textboxTextLineColor,
            'link': linkColor,
            'fullTransparency': fullTransparencyColor,
            'settingsContainerBorder': settingsContainerBorderColor,
            'settingsContainerBox': settingsContainerBoxColor,
            'categoryBodyBackground': categoryBodyBackgroundColor,
            'categoryTitle': categoryTitleColor,
            'categoryHeader': categoryHeaderColor,
            'accent': accentColor,
            'subCatTitleText': subCatTitleTextColor,
            'subCatLine': subCatLineColor,
            'switchCircle': switchCircleColor,
            'arrowBackground': arrowBackgroundColor,
            'arrow': arrowColor}
    
def rgbToHsv(rgbTuple):
    r, g, b, a = [x / 255.0 for x in rgbTuple]
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin
    v = cmax
    s = 0.0 if cmax == 0 else delta / cmax
    if delta == 0:
        h = 0.0
    elif cmax == r:
        h = 60 * (((g - b) / delta) % 6)
    elif cmax == g:
        h = 60 * (((b - r) / delta) + 2)
    else:
        h = 60 * (((r - g) / delta) + 4)

    return (min(360, round(h, 2)), min(1, round(s, 4)), min(1, round(v, 4)))

def hsvToRgb(hsvTuple):
    h, s, v = hsvTuple

    if s == 0:
        c = round(v * 255)
        return (c, c, c)

    h = h % 360
    i = int(h / 60)
    f = (h / 60) - i

    p = v * (1 - s)
    q = v * (1 - s * f)
    t = v * (1 - s * (1 - f))

    r, g, b = [
        (v, t, p),
        (q, v, p),
        (p, v, t),
        (p, q, v),
        (t, p, v),
        (v, p, q),
    ][i]

    return (min(255, round(r * 255)), min(255, round(g * 255)), min(255, round(b * 255)))

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