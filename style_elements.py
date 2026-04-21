import pygame
import time
import json

class Button:
    def __init__(self, x, y, w, h, text, callback, fontSize, borderRadius, SCALE, HEIGHT, BORDER_WIDTH):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback
        self.SCALE = SCALE
        self.font = pygame.font.Font('fonts/Roboto-Medium.ttf', int(fontSize * self.SCALE))
        self.borderRadius = borderRadius
        self.HEIGHT = HEIGHT
        self.BORDER_WIDTH = BORDER_WIDTH

    def draw(self, surface, BG_COLOR, BORDER_COLOR, TEXT_COLOR_1):
        pygame.draw.rect(surface, BORDER_COLOR, self.rect, border_radius=int(0.036 * self.HEIGHT))
        pygame.draw.rect(surface, BG_COLOR, (self.rect.x + self.BORDER_WIDTH, self.rect.y + self.BORDER_WIDTH, self.rect.width - self.BORDER_WIDTH * 2, self.rect.height - self.BORDER_WIDTH * 2), border_radius=int(self.borderRadius * self.SCALE))
        txt_surf = self.font.render(self.text, True, TEXT_COLOR_1)
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        surface.blit(txt_surf, txt_rect)

    def handleEvent(self, event):
        if self.rect.collidepoint((event.pos[0], event.pos[1])):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint((event.pos[0], event.pos[1])):
            self.callback()

class Container:
    def __init__(self, x, y, w, h, borderColor, boxColor, topLeftBorderRadius, topRightBorderRadius, bottomLeftBorderRadius, bottomRightBorderRadius, BORDER_WIDTH, SCALE):
        self.rect = pygame.Rect(x, y, w, h)
        self.borderColor = borderColor
        self.boxColor = boxColor
        self.topLeftBorderRadius = topLeftBorderRadius
        self.topRightBorderRadius = topRightBorderRadius
        self.bottomLeftBorderRadius = bottomLeftBorderRadius
        self.bottomRightBorderRadius = bottomRightBorderRadius
        self.BORDER_WIDTH = BORDER_WIDTH
        self.SCALE = SCALE
        
    def drawBox(self, surface):
        if self.topLeftBorderRadius == self.topRightBorderRadius == self.bottomLeftBorderRadius == self.bottomRightBorderRadius:
            pygame.draw.rect(surface, self.borderColor, self.rect, border_radius=self.topLeftBorderRadius)
            pygame.draw.rect(surface, self.boxColor, (self.rect.x + self.BORDER_WIDTH, self.rect.y + self.BORDER_WIDTH, self.rect.width - self.BORDER_WIDTH * 2, self.rect.height - self.BORDER_WIDTH * 2), border_radius=self.topLeftBorderRadius)
        else:
            pygame.draw.rect(surface, self.borderColor, self.rect, border_top_left_radius=self.topLeftBorderRadius, border_top_right_radius=self.topRightBorderRadius, border_bottom_left_radius=self.bottomLeftBorderRadius, border_bottom_right_radius=self.bottomRightBorderRadius)
            pygame.draw.rect(surface, self.boxColor, (self.rect.x + self.BORDER_WIDTH, self.rect.y + self.BORDER_WIDTH, self.rect.width - self.BORDER_WIDTH * 2, self.rect.height - self.BORDER_WIDTH * 2), border_top_left_radius=self.topLeftBorderRadius, border_top_right_radius=self.topRightBorderRadius, border_bottom_left_radius=self.bottomLeftBorderRadius, border_bottom_right_radius=self.bottomRightBorderRadius)
            
    def drawText(self, surface, x, y, fontSize, text, textColor):
        font = pygame.font.Font('fonts/Roboto-Medium.ttf', fontSize)
        textSurface = font.render(text, True, textColor)
        textRect = textSurface.get_rect(topleft=(x, y))
        surface.blit(textSurface, textRect)
        
    def drawAccent(self, surface, width, height, accentColor):
        if height >= self.rect.height - self.bottomLeftBorderRadius and not (width >= self.rect.width - self.topRightBorderRadius):
            pygame.draw.rect(surface, accentColor, (self.rect.x, self.rect.y, width, height), border_top_left_radius=self.topLeftBorderRadius, border_bottom_left_radius=self.bottomLeftBorderRadius)
        elif not (height >= self.rect.height - self.bottomLeftBorderRadius) and width >= self.rect.width - self.topRightBorderRadius:
            pygame.draw.rect(surface, accentColor, (self.rect.x, self.rect.y, width, height), border_top_left_radius=self.topLeftBorderRadius, border_top_right_radius=self.topRightBorderRadius)
        elif height >= self.rect.height - self.bottomLeftBorderRadius and width >= self.rect.width - self.topRightBorderRadius:
            pygame.draw.rect(surface, accentColor, (self.rect.x, self.rect.y, width, height), border_radius=self.topLeftBorderRadius)
        else:
            pygame.draw.rect(surface, accentColor, (self.rect.x, self.rect.y, width, height), border_top_left_radius=self.topLeftBorderRadius)

class Switch:
    def __init__(self, x, y, activatedColor, disactivatedColor, circleColor, isActivated, SCALE):
        self.SCALE = SCALE
        self.rect = pygame.Rect(x, y, int(40 * self.SCALE), int(20 * self.SCALE))
        self.activatedColor = activatedColor
        self.disactivatedColor = disactivatedColor
        self.circleColor = circleColor
        self.isActivated = isActivated
        
    def drawSwitch(self, surface):
        if self.isActivated:
            switchColor = self.activatedColor
            ellipseRect = (self.rect.x + int(21 * self.SCALE), self.rect.y + int(1.5 * self.SCALE), int(18 * self.SCALE), int(18 * self.SCALE))
        else:
            switchColor = self.disactivatedColor
            ellipseRect = (self.rect.x + int(1 * self.SCALE), self.rect.y + int(1.5 * self.SCALE), int(18 * self.SCALE), int(18 * self.SCALE))
        pygame.draw.rect(surface, switchColor, self.rect, border_radius=(self.rect.height // 2))
        pygame.draw.ellipse(surface, self.circleColor, ellipseRect)
        
    def handleEvent(self, event):
        if self.rect.collidepoint((event.pos[0], event.pos[1])):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint((event.pos[0], event.pos[1])):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
            self.isActivated = not self.isActivated
                
class EntryBox:
    def __init__(self, scale, x, y, w, h, possibleCaracters, numCaraMax, accentColor, defaultTextContent):
        self.rect = pygame.Rect(x, y, w, h)
        self.scale = scale
        self.blinkerState = False
        self.blinkerLastBlink = time.time_ns()
        self.isWriting = False
        self.possibleCaracters = possibleCaracters
        self.typingText = ''
        self.numCaraMax = numCaraMax
        self.accentColor = accentColor
        self.defaultTextContent = defaultTextContent
        
    def drawBox(self, surface, boxColor, borderRadius, borderWidth):
        if self.isWriting:
            pygame.draw.rect(surface, self.accentColor, self.rect, border_radius=borderRadius)
        else:
            pygame.draw.rect(surface, boxColor, self.rect, border_radius=borderRadius)
        pygame.draw.rect(surface, boxColor, (self.rect.x + borderWidth, self.rect.y + borderWidth, self.rect.width - borderWidth * 2, self.rect.height - borderWidth * 2), border_radius=borderRadius)

    def drawLabel(self, surface, x, y, labelText, labelColor, labelSize):
        font = pygame.font.Font('fonts/Roboto-Medium.ttf', labelSize)
        labelSurface = font.render(labelText, True, labelColor)
        labelRect = labelSurface.get_rect(midleft=(x, y))
        surface.blit(labelSurface, labelRect)
        
    def drawText(self, surface, x, y, textColor, textSize, alreadySetText):
        font = pygame.font.Font('fonts/Roboto-Medium.ttf', textSize)
        if self.isWriting:
            textSurface = font.render(self.typingText.upper(), True, textColor)
        else:
            textSurface = font.render(alreadySetText.upper(), True, textColor)
        textRect = textSurface.get_rect(midleft=(x, y))
        surface.blit(textSurface, textRect)
        self.textPos = (x, y)
        self.textWidth = textSurface.get_width()
    
    def drawBlinker(self, surface, blinkerWidth, blinkerHeight, blinkerMSInterval):
        if self.isWriting:
            currentTime = time.time_ns()
            elapsedMS = (currentTime - self.blinkerLastBlink) / 1000000
            if elapsedMS > blinkerMSInterval:
                self.blinkerState = not self.blinkerState
                self.blinkerLastBlink = currentTime
            if self.blinkerState:
                blinkerRect = pygame.Rect(self.textPos[0] + self.textWidth + int(3 * self.scale), self.textPos[1] - int(8.5 * self.scale), blinkerWidth, blinkerHeight)
                pygame.draw.rect(surface, self.accentColor, blinkerRect)
            
    def drawDefaultText(self, surface, x, y, defaultTextColor, defaultTextSize):
        if len(self.typingText) <= 0:
            font = pygame.font.Font('fonts/Roboto-Medium.ttf', defaultTextSize)
            defaultTextSurface = font.render(self.defaultTextContent.upper(), True, defaultTextColor)
            defaultTextRect = defaultTextSurface.get_rect(midleft=(x, y))
            surface.blit(defaultTextSurface, defaultTextRect)
            
    def handleEvent(self, event):
        if (event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN) and self.rect.collidepoint((event.pos[0], event.pos[1])):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.isWriting = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.isWriting = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                self.isWriting = False
        if self.isWriting:
            if event.type == pygame.KEYDOWN:
                if event.key in self.possibleCaracters:
                    self.typingText += str(chr(event.key))
                elif event.key == pygame.K_BACKSPACE:
                    self.typingText = self.typingText[:-1]
            if len(self.typingText) > self.numCaraMax:
                self.typingText = self.typingText[:self.numCaraMax]
            elif len(self.typingText) == 6:
                self.definitveText = self.typingText
            elif len(self.typingText) < 6:
                self.definitveText = self.defaultTextContent
                
class DropdownBox:
    def __init__(self, scale, options, x, y, w, h, selectedOption):
        self.options = options
        self.scale = scale
        self.rect = pygame.Rect(x, y, w, h)
        self.isOpened = False
        self.selectedOption = selectedOption
        
    def drawBox(self, surface, boxColor, borderColor, borderRadius, borderWidth, optionTextColor, optionTextSize, arrowColor, arrowBackgroundColor, accentColor):
        if self.isOpened:
            pygame.draw.rect(surface, accentColor, (self.rect.x, self.rect.y, self.rect.w, self.rect.h + int((5 + len(self.options) * 16) * self.scale)), border_radius=borderRadius)
            pygame.draw.rect(surface, boxColor, (self.rect.x + borderWidth, self.rect.y + borderWidth, self.rect.w - borderWidth * 2, self.rect.h + int((5 + len(self.options) * 16) * self.scale) - borderWidth * 2), border_radius=borderRadius) 
            self.drawOptions(surface, optionTextColor, optionTextSize, arrowBackgroundColor, borderWidth, borderRadius)
        else:
            if borderWidth and borderWidth > 0:
                pygame.draw.rect(surface, borderColor, (self.rect.x, self.rect.y, self.rect.w, self.rect.h), width=borderWidth, border_radius=borderRadius)
            pygame.draw.rect(surface, boxColor, (self.rect.x + borderWidth, self.rect.y + borderWidth, self.rect.w - borderWidth * 2, self.rect.h - borderWidth * 2), border_radius=borderRadius)
            self.drawArrowBackground(surface, int(340 * self.scale), int(513 * self.scale), int(26 * self.scale), int(26 * self.scale), arrowBackgroundColor, 0, int(10 * self.scale), 0, int(10 * self.scale))
            self.drawArrow(surface, int(347 * self.scale), int(522 * self.scale), arrowColor)

    def drawArrow(self, surface, x, y, arrowColor):
        pygame.draw.polygon(surface, arrowColor, [(x, y), (x + int(11 * self.scale), y), (x + int(6 * self.scale), y + int(10 * self.scale))])
        
    def drawArrowBackground(self, surface, x, y, w, h, backgroundColor, topLeftBorderRadius, topRightBorderRadius, bottomLeftBorderRadius, bottomRightBorderRadius):
        pygame.draw.rect(surface, backgroundColor, (x, y, w, h), border_top_left_radius=topLeftBorderRadius, border_top_right_radius=topRightBorderRadius, border_bottom_left_radius=bottomLeftBorderRadius, border_bottom_right_radius=bottomRightBorderRadius)
        
    def drawText(self, surface, textColor, textSize):
        font = pygame.font.Font('fonts/Roboto-Medium.ttf', textSize)
        textSurface = font.render(self.selectedOption, True, textColor)
        textRect = textSurface.get_rect(midleft=(self.rect.x + int(10 * self.scale), self.rect.y + int((10 + 4) * self.scale)))
        surface.blit(textSurface, textRect)
        self.textWidth = textSurface.get_width()
        
    def drawOptions(self, surface, textColor, textSize, selectionColor, borderWidth, borderRadius):
        font = pygame.font.Font('fonts/Roboto-Medium.ttf', textSize)
        mousePos = pygame.mouse.get_pos()
        optionRects = []
        for i in range(len(self.options)):
            textSurface = font.render(self.options[i], True, textColor)
            textRect = textSurface.get_rect(midleft=(self.rect.x + int(10 * self.scale), self.rect.y + int(i * (24 * self.scale)) + int((10 + 6) * self.scale)))
            selectionBackground = textRect.inflate(int(120 * self.scale) - textRect.w - borderWidth * 2, int(6 * self.scale))
            selectionBackground.move_ip(selectionBackground.w // 2 - textRect.w // 2 - int(10 * self.scale) + borderWidth, - int(0.5 * self.scale))
            optionRects.append(selectionBackground.copy())
            if selectionBackground.collidepoint(mousePos):
                pygame.draw.rect(surface, selectionColor, selectionBackground, border_radius=borderRadius)
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            surface.blit(textSurface, textRect)
        self.optionRects = optionRects
        
    def handleEvent(self, event):
        if hasattr(event, "pos"):
            pos = event.pos
            if self.rect.collidepoint(pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(pos) and not self.isOpened:
                self.isOpened = True
                return
            if self.isOpened and event.type == pygame.MOUSEBUTTONDOWN:
                for i, optRect in enumerate(getattr(self, 'optionRects', [])):
                    if optRect.collidepoint(pos):
                        self.selectedOption = self.options[i]
                        readWriteUserSettings("pieceChoice", self.options[i])
                        self.isOpened = False
                        
def readWriteUserSettings(currentLineName, newLineState):
    with open("user_settings.json", "r", encoding="utf-8") as f:
        userSettings = json.load(f)

    userSettings[currentLineName] = newLineState

    with open("user_settings.json", "w", encoding="utf-8") as f:
        json.dump(userSettings, f, indent=4, ensure_ascii=False)