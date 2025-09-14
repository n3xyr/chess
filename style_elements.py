import pygame
import globals

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
            self.isActivated = not self.isActivated
                
class EntryBox:
    pass