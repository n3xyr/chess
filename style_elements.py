import pygame
from menu import SCALE, HEIGHT, BORDER_WIDTH

class Button:
    def __init__(self, x, y, w, h, text, callback, fontSize, borderRadius):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback
        self.font = pygame.font.Font('fonts/Roboto-Medium.ttf', int(fontSize * SCALE))
        self.borderRadius = borderRadius

    def draw(self, surface, BG_COLOR, BORDER_COLOR, TEXT_COLOR_1):
        pygame.draw.rect(surface, BORDER_COLOR, self.rect, border_radius=int(0.036 * HEIGHT))
        pygame.draw.rect(surface, BG_COLOR, (self.rect.x + BORDER_WIDTH, self.rect.y + BORDER_WIDTH, self.rect.width - BORDER_WIDTH * 2, self.rect.height - BORDER_WIDTH * 2), border_radius=int(self.borderRadius * SCALE))
        txt_surf = self.font.render(self.text, True, TEXT_COLOR_1)
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        surface.blit(txt_surf, txt_rect)

    def handle_event(self, event):
        if self.rect.collidepoint((event.pos[0], event.pos[1])):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint((event.pos[0], event.pos[1])):
            self.callback()

class Container:
    # border radius needs to be multiplied by scale beforehand, it's not done here
    def __init__(self, x, y, w, h, borderColor, boxColor, topLeftBorderRadius, topRightBorderRadius, bottomLeftBorderRadius, bottomRightBorderRadius):
        self.rect = pygame.Rect(x, y, w, h)
        self.borderColor = borderColor
        self.boxColor = boxColor
        self.topLeftBorderRadius = topLeftBorderRadius
        self.topRightBorderRadius = topRightBorderRadius
        self.bottomLeftBorderRadius = bottomLeftBorderRadius
        self.bottomRightBorderRadius = bottomRightBorderRadius
        
    def drawBox(self, surface):
        if self.topLeftBorderRadius == self.topRightBorderRadius == self.bottomLeftBorderRadius == self.bottomRightBorderRadius:
            pygame.draw.rect(surface, self.borderColor, self.rect, border_radius=self.topLeftBorderRadius)
            pygame.draw.rect(surface, self.boxColor, (self.rect.x + BORDER_WIDTH, self.rect.y + BORDER_WIDTH, self.rect.width - BORDER_WIDTH * 2, self.rect.height - BORDER_WIDTH * 2), border_radius=self.topLeftBorderRadius)
        else:
            pygame.draw.rect(surface, self.borderColor, self.rect, border_top_left_radius=self.topLeftBorderRadius, border_top_right_radius=self.topRightBorderRadius, border_bottom_left_radius=self.bottomLeftBorderRadius, border_bottom_right_radius=self.bottomRightBorderRadius)
            pygame.draw.rect(surface, self.boxColor, (self.rect.x + BORDER_WIDTH, self.rect.y + BORDER_WIDTH, self.rect.width - BORDER_WIDTH * 2, self.rect.height - BORDER_WIDTH * 2), border_top_left_radius=self.topLeftBorderRadius, border_top_right_radius=self.topRightBorderRadius, border_bottom_left_radius=self.bottomLeftBorderRadius, border_bottom_right_radius=self.bottomRightBorderRadius)
            
    def drawText(self, surface, x, y, fontSize, text, textColor):
        # x and y are from the text surface, not the whole game surface
        font = pygame.font.Font('fonts/Roboto-Medium.ttf', int(fontSize * SCALE))
        textSurface = font.render(text, True, textColor)
        textRect = textSurface.get_rect(center=(x, y))
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
    def __init__(self, x, y, activatedColor, disactivatedColor, circleColor, isActivated):
        self.rect = pygame.Rect(x, y, int(40 * SCALE), int(20 * SCALE))
        self.activatedColor = activatedColor
        self.disactivatedColor = disactivatedColor
        self.circleColor = circleColor
        self.isActivated = isActivated
        
    def draw(self, surface):
        if self.isActivated:
            switchColor = self.activatedColor
            ellipseRect = (self.rect.x + int(21 * SCALE), self.rect.y + int(1 * SCALE), int(18 * SCALE), int(18 * SCALE))
        else:
            switchColor = self.disactivatedColor
            ellipseRect = (self.rect.x + int(1 * SCALE), self.rect.y + int(1 * SCALE), int(18 * SCALE), int(18 * SCALE))
        pygame.draw.rect(surface, switchColor, self.rect, border_radius=(self.rect.height // 2))
        pygame.draw.ellipse(surface, self.circleColor, ellipseRect)
        
    def handleEvent(self, event):
        if self.rect.collidepoint((event.pos[0], event.pos[1])):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint((event.pos[0], event.pos[1])):
            if self.isActivated:
                self.isActivated = False
            else:
                self.isActivated = True
                
class EntryBox:
    def __init__(self, x, y, w, h, text, callback):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback
        self.font = pygame.font.Font('fonts/Roboto-Medium.ttf', int(22 * SCALE))

    def draw(self, surface, BG_COLOR, BORDER_COLOR, TEXT_COLOR_1, TEXT_COLOR_2, LINE_COLOR, LABEL, FONT_SIZE):
        font = pygame.font.Font('fonts/Roboto-Medium.ttf', int(FONT_SIZE * SCALE))
        pygame.draw.rect(surface, BORDER_COLOR, self.rect, border_radius=int(0.036 * HEIGHT))
        pygame.draw.rect(surface, BG_COLOR, (self.rect.x + BORDER_WIDTH, self.rect.y + BORDER_WIDTH, self.rect.width - BORDER_WIDTH * 2, self.rect.height - BORDER_WIDTH * 2), border_radius=int(0.036 * HEIGHT - 2 * BORDER_WIDTH))
        textSurface = self.font.render(self.text, True, TEXT_COLOR_1)
        textRect = textSurface.get_rect(centerx = self.rect.center[0] + (40 * SCALE), centery=self.rect.center[1])
        
        label_surf = font.render(LABEL, True, TEXT_COLOR_2)
        label_rect = label_surf.get_rect(midleft=(self.rect.left + int(25 * SCALE), self.rect.centery))

        for i in range(2):
            pygame.draw.line(surface, LINE_COLOR, (self.rect.left + int(90 * SCALE + i), self.rect.centery + int(19 * SCALE)), (self.rect.left + int(90 * SCALE + i), self.rect.centery - int(19 * SCALE)))
        
        surface.blit(textSurface, textRect)
        surface.blit(label_surf, label_rect)

    def set_text_entry(self, bool=True):
        self.text_entry = bool

    def handle_event(self, event):            
        if self.rect.collidepoint((event.pos[0], event.pos[1])):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.callback()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.text_entry = False

    def set_text(self, new_text):
        self.text = new_text
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))