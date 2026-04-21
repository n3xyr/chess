import pygame
import style_elements
import globals
import builtins
import json

# Import theme
with open("theme.json", "r", encoding="utf-8") as t:
    theme = json.load(t)

fullTransparencyColor = theme['fullTransparency']
settingsContainerBorderColor = theme['settingsContainerBorder']
settingsContainerBoxColor = theme['settingsContainerBox']
categoryBodyBackgroundColor = theme['categoryBodyBackground']
categoryTitleColor = theme['categoryTitle']
categoryHeaderColor = theme['categoryHeader']
accentColor = theme['accent']
subCatTitleTextColor = theme['subCatTitleText']
subCatLineColor = theme['subCatLine']
primaryColor = theme['primary']
secondaryColor = theme['secondary']
switchCircleColor = theme['switchCircle']
arrowBackgroundColor = theme['arrowBackground']
arrowColor = theme['arrow']

def importThemeColors():
    global fullTransparencyColor, settingsContainerBorderColor, settingsContainerBoxColor, categoryBodyBackgroundColor, categoryTitleColor, categoryHeaderColor, accentColor, subCatTitleTextColor, subCatLineColor, primaryColor, secondaryColor, switchCircleColor, arrowBackgroundColor, arrowColor
    
    # Import theme
    with open("theme.json", "r", encoding="utf-8") as t:
        theme = json.load(t)
        
    fullTransparencyColor = theme['fullTransparency']
    settingsContainerBorderColor = theme['settingsContainerBorder']
    settingsContainerBoxColor = theme['settingsContainerBox']
    categoryBodyBackgroundColor = theme['categoryBodyBackground']
    categoryTitleColor = theme['categoryTitle']
    categoryHeaderColor = theme['categoryHeader']
    accentColor = theme['accent']
    subCatTitleTextColor = theme['subCatTitleText']
    subCatLineColor = theme['subCatLine']
    primaryColor = theme['primary']
    secondaryColor = theme['secondary']
    switchCircleColor = theme['switchCircle']
    arrowBackgroundColor = theme['arrowBackground']
    arrowColor = theme['arrow']

    g = builtins.globals()
    try:
        if 'primaryColorEntry' in g:
            primaryColorEntry.accentColor = accentColor
            primaryColorEntry.defaultTextContent = userSettings.get('primaryColor', primaryColorEntry.defaultTextContent)
    except Exception:
        pass
    try:
        if 'secondaryColorEntry' in g:
            secondaryColorEntry.accentColor = accentColor
            secondaryColorEntry.defaultTextContent = userSettings.get('secondaryColor', secondaryColorEntry.defaultTextContent)
    except Exception:
        pass

originalImages = {}
scaledImages = {}

with open("user_settings.json", "r", encoding="utf-8") as f:
    userSettings = json.load(f)

def getOriginalImage(name):
    if name not in originalImages:
        originalImages[name] = pygame.image.load(f"piecesImages/{name}.png").convert_alpha()
    return originalImages[name]

def getScaledImage(name, size):
    key = (name, size)
    if key not in scaledImages:
        scaledImages[key] = pygame.transform.smoothscale(getOriginalImage(name), (size, size))
    return scaledImages[key]

def showSettingsFunc(bool):
    globals.showSettings = bool

def drawMainContainer(SCALE, settingsSurface, BORDER_WIDTH):
    settingsContainer = style_elements.Container(int(50 * SCALE), int(200 * SCALE), int(700 * SCALE), int(600 * SCALE), settingsContainerBorderColor, settingsContainerBoxColor, int(40 * SCALE), int(40 * SCALE), int(40 * SCALE), int(40 * SCALE), BORDER_WIDTH, SCALE)
    settingsContainer.drawBox(settingsSurface)
    
def drawTitle(SCALE, settingsSurface, BORDER_WIDTH):
    importThemeColors()
    titleContainer = style_elements.Container(int(100 * SCALE), int(246 * SCALE), int(156 * SCALE), int(60 * SCALE), categoryBodyBackgroundColor, categoryBodyBackgroundColor, int(10 * SCALE), int(10 * SCALE), int(10 * SCALE), int(10 * SCALE), BORDER_WIDTH, SCALE)
    titleContainer.drawBox(settingsSurface)
    titleContainer.drawText(settingsSurface, int(128 * SCALE), int(266 * SCALE - int(6 * SCALE)), int(27 * SCALE), "Settings", categoryTitleColor)

def drawClose(SCALE, settingsSurface, HEIGHT):
    global closeButton
    importThemeColors()
    closeButton = style_elements.Button(int(640 * SCALE), int(246 * SCALE), int(60 * SCALE), int(60 * SCALE), "", lambda: showSettingsFunc(False), 0, int(10 * SCALE), SCALE, HEIGHT, 0)
    closeButton.draw(settingsSurface, categoryBodyBackgroundColor, fullTransparencyColor, fullTransparencyColor)
    pygame.draw.aaline(settingsSurface, categoryTitleColor, (int(659 * SCALE), int(264 * SCALE)), (int(680 * SCALE), int(285 * SCALE)))
    pygame.draw.aaline(settingsSurface, categoryTitleColor, (int(680 * SCALE), int(264 * SCALE)), (int(659 * SCALE), int(285 * SCALE)))
    
def drawAppearanceCatHeader(SCALE, settingsSurface):
    importThemeColors()
    appearanceCatHeader = style_elements.Container(int(100 * SCALE), int(326 * SCALE), int(600 * SCALE), int(50 * SCALE), fullTransparencyColor, categoryHeaderColor, int(10 * SCALE), int(10 * SCALE), 0, 0, 0, SCALE)
    appearanceCatHeader.drawBox(settingsSurface)
    appearanceCatHeader.drawAccent(settingsSurface, int(11 * SCALE), int(50 * SCALE), accentColor)
    appearanceCatHeader.drawText(settingsSurface, int(131 * SCALE), int(341 * SCALE - int(6 * SCALE)), int(25 * SCALE), "Appearance", categoryTitleColor)
    
def drawAppearanceCatBody(SCALE, settingsSurface):
    importThemeColors()
    appearanceCatBody = style_elements.Container(int(100 * SCALE), int(376 * SCALE), int(600 * SCALE), int(179 * SCALE), fullTransparencyColor, categoryBodyBackgroundColor, 0, 0, int(10 * SCALE), int(10 * SCALE), 0, SCALE)
    appearanceCatBody.drawBox(settingsSurface)
    appearanceCatBody.drawText(settingsSurface, int(120 * SCALE), int(396 * SCALE - int(2 * SCALE)), int(20 * SCALE), "Primary color", subCatTitleTextColor)
    pygame.draw.aaline(settingsSurface, subCatLineColor, (int(100 * SCALE), int(436 * SCALE)), (int(400 * SCALE), int(436 * SCALE)))
    appearanceCatBody.drawText(settingsSurface, int(120 * SCALE), int(456 * SCALE - int(2 * SCALE)), int(20 * SCALE), "Secondary color", subCatTitleTextColor)
    pygame.draw.aaline(settingsSurface, subCatLineColor, (int(100 * SCALE), int(496 * SCALE)), (int(400 * SCALE), int(496 * SCALE)))
    appearanceCatBody.drawText(settingsSurface, int(120 * SCALE), int(516 * SCALE - int(3 * SCALE)), int(20 * SCALE), "Pieces style", subCatTitleTextColor)
    drawExampleBoard(SCALE, settingsSurface)
        
def drawExampleBoard(SCALE, settingsSurface):
    importThemeColors()
    squareSize = int(50 * SCALE)
    pygame.draw.rect(settingsSurface, secondaryColor, (int(443 * SCALE), int(391 * SCALE), squareSize, squareSize), border_top_left_radius=int(10 * SCALE))
    pygame.draw.rect(settingsSurface, secondaryColor, (int(443 * SCALE), int(491 * SCALE), squareSize, squareSize), border_bottom_left_radius=int(10 * SCALE))
    pygame.draw.rect(settingsSurface, primaryColor, (int(593 * SCALE), int(391 * SCALE), squareSize, squareSize), border_top_right_radius=int(10 * SCALE))
    pygame.draw.rect(settingsSurface, primaryColor, (int(593 * SCALE), int(491 * SCALE), squareSize, squareSize), border_bottom_right_radius=int(10 * SCALE))
    for i in range(2):
        for j in range(2):
            if j % 2 == 0:
                fillColor = primaryColor
            else:
                fillColor = secondaryColor
            pygame.draw.rect(settingsSurface, fillColor, (int((493 + 50 * j) * SCALE), int((391 + 100 * i) * SCALE), squareSize, squareSize))
    for i in range(4):
        if i % 2 == 0:
            fillColor = primaryColor
        else:
            fillColor = secondaryColor
        pygame.draw.rect(settingsSurface, fillColor, (int((443 + 50 * i) * SCALE), int(441 * SCALE), squareSize, squareSize))
    
    bp = getScaledImage("bp", squareSize)
    bb = getScaledImage("bb", squareSize)
    bk = getScaledImage("bk", squareSize)
    bn = getScaledImage("bn", squareSize)
    bq = getScaledImage("bq", squareSize)
    br = getScaledImage("br", squareSize)
    wp = getScaledImage("wp", squareSize)
    wb = getScaledImage("wb", squareSize)
    wk = getScaledImage("wk", squareSize)
    wn = getScaledImage("wn", squareSize)
    wq = getScaledImage("wq", squareSize)
    wr = getScaledImage("wr", squareSize)
    
    placements = [(443, 391, bb), (493, 391, bq), (543, 391, bk), (593, 391, br), (443, 441, bp), (493, 441, bn),
                  (543, 441, wn), (593, 441, wp), (443, 491, wb), (493, 491, wq), (543, 491, wk), (593, 491, wr)]
    
    for staticX, staticY, imageName in placements:
        x = int(staticX * SCALE)
        y = int(staticY * SCALE)
        settingsSurface.blit(imageName, (x, y))

def drawPrimaryColorEntry(SCALE, settingsSurface, BORDER_WIDTH):
    global primaryColorEntry
    importThemeColors()
    primaryHexPossibleCaracters = [
        pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
        pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,
        pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4,
        pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9,
        pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f
        ]

    primaryPythonGlobalList = builtins.globals()
    if 'primaryColorEntry' in primaryPythonGlobalList:
        primaryExistingObject = primaryPythonGlobalList['primaryColorEntry']
        if getattr(primaryExistingObject, 'scale') != SCALE:
            primaryOldText = getattr(primaryExistingObject, 'typingText', '')
            primaryOldWritingState = getattr(primaryExistingObject, 'isWriting', False)
            primaryColorEntry = style_elements.EntryBox(SCALE, int(251 * SCALE), int(392 * SCALE), int(110 * SCALE), int(28 * SCALE), primaryHexPossibleCaracters, 6, accentColor, userSettings['primaryColor'])
            primaryColorEntry.typingText = primaryOldText
            primaryColorEntry.isWriting = primaryOldWritingState
    else:
        primaryColorEntry = style_elements.EntryBox(SCALE, int(251 * SCALE), int(392 * SCALE), int(110 * SCALE), int(28 * SCALE), primaryHexPossibleCaracters, 6, accentColor, userSettings['primaryColor'])
    
    primaryTextX, primaryTextY = 281, 396
    primaryColorEntry.drawBox(settingsSurface, categoryHeaderColor, int(10 * SCALE), BORDER_WIDTH)
    primaryColorEntry.drawLabel(settingsSurface, int(265 * SCALE), int(396 * SCALE + int(10 * SCALE)), '#', subCatTitleTextColor, int(17 * SCALE))
    primaryColorEntry.drawText(settingsSurface, int(primaryTextX * SCALE), int(primaryTextY * SCALE + int(10 * SCALE)), categoryTitleColor, int(17 * SCALE), userSettings['primaryColor'])
    primaryColorEntry.drawBlinker(settingsSurface, int(3 * SCALE), int(18 * SCALE), 600)
    if primaryColorEntry.isWriting and len(primaryColorEntry.typingText) == 0:
        primaryColorEntry.drawDefaultText(settingsSurface, int((primaryTextX + 6) * SCALE), int((primaryTextY + 0.5) * SCALE + int(10 * SCALE)), subCatTitleTextColor, int(15 * SCALE))

def drawSecondaryColorEntry(SCALE, settingsSurface, BORDER_WIDTH):
    global secondaryColorEntry
    importThemeColors()
    secondaryHexPossibleCaracters = [
        pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
        pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,
        pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4,
        pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9,
        pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f
        ]

    secondaryPythonGlobalList = builtins.globals()
    if 'secondaryColorEntry' in secondaryPythonGlobalList:
        secondaryExistingObject = secondaryPythonGlobalList['secondaryColorEntry']
        if getattr(secondaryExistingObject, 'scale') != SCALE:
            secondaryOldText = getattr(secondaryExistingObject, 'typingText', '')
            secondaryOldWritingState = getattr(secondaryExistingObject, 'isWriting', False)
            secondaryColorEntry = style_elements.EntryBox(SCALE, int(276 * SCALE), int(452 * SCALE), int(110 * SCALE), int(28 * SCALE), secondaryHexPossibleCaracters, 6, accentColor, userSettings['secondaryColor'])
            secondaryColorEntry.typingText = secondaryOldText
            secondaryColorEntry.isWriting = secondaryOldWritingState
    else:
        secondaryColorEntry = style_elements.EntryBox(SCALE, int(276 * SCALE), int(452 * SCALE), int(110 * SCALE), int(28 * SCALE), secondaryHexPossibleCaracters, 6, accentColor, userSettings['secondaryColor'])
    
    secondaryTextX, secondaryTextY = 306, 456
    secondaryColorEntry.drawBox(settingsSurface, categoryHeaderColor, int(10 * SCALE), BORDER_WIDTH)
    secondaryColorEntry.drawLabel(settingsSurface, int(290 * SCALE), int(456 * SCALE + int(10 * SCALE)), '#', subCatTitleTextColor, int(17 * SCALE))
    secondaryColorEntry.drawText(settingsSurface, int(secondaryTextX * SCALE), int(secondaryTextY * SCALE + int(10 * SCALE)), categoryTitleColor, int(17 * SCALE), userSettings['secondaryColor'])
    secondaryColorEntry.drawBlinker(settingsSurface, int(3 * SCALE), int(18 * SCALE), 600)
    if secondaryColorEntry.isWriting and len(secondaryColorEntry.typingText) == 0:
        secondaryColorEntry.drawDefaultText(settingsSurface, int((secondaryTextX + 6) * SCALE), int((secondaryTextY + 0.5) * SCALE + int(9 * SCALE)), subCatTitleTextColor, int(15 * SCALE))

def drawPieceChoiceDropdown(SCALE, settingsSurface, BORDER_WIDTH):
    global pieceChoiceDropdown
    importThemeColors()
    
    currentSelectedOption = userSettings['pieceChoice']
    
    pieceChoicePythonGlobalList = builtins.globals()
    if 'pieceChoiceDropdown' in pieceChoicePythonGlobalList:
        pieceChoiceExistingObject = pieceChoicePythonGlobalList['pieceChoiceDropdown']
        if getattr(pieceChoiceExistingObject, 'scale') != SCALE:
            pieceChoiceOldSelectedOption = getattr(pieceChoiceExistingObject, 'selectedOption')
            pieceChoiceOldState = getattr(pieceChoiceExistingObject, 'isOpened', False)
            pieceChoiceDropdown = style_elements.DropdownBox(SCALE, ["Neo", "Classic", "pls don't"], int(246 * SCALE), int(512 * SCALE), int(120 * SCALE), int(28 * SCALE), currentSelectedOption)
            pieceChoiceDropdown.selectedOption = pieceChoiceOldSelectedOption
            pieceChoiceDropdown.isOpened = pieceChoiceOldState
    else:        
        pieceChoiceDropdown = style_elements.DropdownBox(SCALE, ["Neo", "Classic", "pls don't"], int(246 * SCALE), int(512 * SCALE), int(120 * SCALE), int(28 * SCALE), currentSelectedOption)
    
    pieceChoiceDropdown.drawBox(settingsSurface, categoryHeaderColor, fullTransparencyColor, int(10 * SCALE), BORDER_WIDTH, categoryTitleColor, int(15 * SCALE), arrowColor, arrowBackgroundColor, accentColor)
    if not pieceChoiceDropdown.isOpened:
        pieceChoiceDropdown.drawText(settingsSurface, categoryTitleColor, int(15 * SCALE))
    
def drawGameplayCatHeader(SCALE, settingsSurface):
    importThemeColors()
    gameplayCatHeader = style_elements.Container(int(100 * SCALE), int(584 * SCALE), int(600 * SCALE), int(50 * SCALE), fullTransparencyColor, categoryHeaderColor, int(10 * SCALE), int(10 * SCALE), 0, 0, 0, SCALE)
    gameplayCatHeader.drawBox(settingsSurface)
    gameplayCatHeader.drawAccent(settingsSurface, int(11 * SCALE), int(50 * SCALE), accentColor)
    gameplayCatHeader.drawText(settingsSurface, int(131 * SCALE), int(599 * SCALE - int(6 * SCALE)), int(25 * SCALE), "Gameplay", categoryTitleColor)
   
def drawGameplayCatBody(SCALE, settingsSurface):
    importThemeColors()
    gameplayCatBody = style_elements.Container(int(100 * SCALE), int(634 * SCALE), int(600 * SCALE), int(120 * SCALE), fullTransparencyColor, categoryBodyBackgroundColor, 0, 0, int(10 * SCALE), int(10 * SCALE), 0, SCALE)
    gameplayCatBody.drawBox(settingsSurface)
    gameplayCatBody.drawText(settingsSurface, int(120 * SCALE), int(654 * SCALE - int(2 * SCALE)), int(20 * SCALE), "Show possible moves", subCatTitleTextColor)
    pygame.draw.aaline(settingsSurface, subCatLineColor, (int(100 * SCALE), int(694 * SCALE)), (int(700 * SCALE), int(694 * SCALE)))
    gameplayCatBody.drawText(settingsSurface, int(120 * SCALE), int(714 * SCALE - int(2 * SCALE)), int(20 * SCALE), "Disable sounds", subCatTitleTextColor)
    
def drawShowPossibleMovesSwitch(SCALE, settingsSurface):
    importThemeColors()
    global showPossibleMovesSwitch
    if userSettings['showPossibleMoves']:
        isActivatedBool = True
    else:
        isActivatedBool = False
        
    showPossibleMovesSwitch = style_elements.Switch(int(623 * SCALE), int(655 * SCALE), accentColor, subCatLineColor, switchCircleColor, isActivatedBool, SCALE)
    showPossibleMovesSwitch.drawSwitch(settingsSurface)
    
def drawDisableSoundsSwitch(SCALE, settingsSurface):
    importThemeColors()
    global disableSoundsSwitch
    if userSettings['disableSounds']:
        isActivatedBool = True
    else:
        isActivatedBool = False
    disableSoundsSwitch = style_elements.Switch(int(623 * SCALE), int(713 * SCALE), accentColor, subCatLineColor, switchCircleColor, isActivatedBool, SCALE)
    disableSoundsSwitch.drawSwitch(settingsSurface)
    
def RGBToHex(RGBCode):
    hexValue = '%02x%02x%02x%02x' % tuple(RGBCode)
    return hexValue[:6]
    
def showSettings(SCALE, screen):
    importThemeColors()
    width = screen.get_width()
    height = screen.get_height()
    settingsSurface = pygame.Surface((width, height), pygame.SRCALPHA)
    settingsSurface.fill(fullTransparencyColor)
    BORDER_WIDTH = max(1, width // 600)
    
    drawMainContainer(SCALE, settingsSurface, BORDER_WIDTH)
    drawTitle(SCALE, settingsSurface, BORDER_WIDTH)
    drawClose(SCALE, settingsSurface, height)
    drawAppearanceCatHeader(SCALE, settingsSurface)
    drawAppearanceCatBody(SCALE, settingsSurface)
    drawPrimaryColorEntry(SCALE, settingsSurface, BORDER_WIDTH)
    drawSecondaryColorEntry(SCALE, settingsSurface, BORDER_WIDTH)
    drawGameplayCatHeader(SCALE, settingsSurface)
    drawGameplayCatBody(SCALE, settingsSurface)
    drawShowPossibleMovesSwitch(SCALE, settingsSurface)
    drawDisableSoundsSwitch(SCALE, settingsSurface)
    drawPieceChoiceDropdown(SCALE, settingsSurface, BORDER_WIDTH)

    globals.settingsButtonsDrawn = True
    
    screen.blit(settingsSurface, (0, 0))