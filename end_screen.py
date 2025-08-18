import pygame
from display_board import WIDTH, HEIGHT, SCALE, TILESIZE

WINDOWDARKTRANSPARENCY = (38, 37, 34, 102)
ENDBOXOUTLINE = (60, 58, 56, 255)
ENDBOXBACKGROUND = (31, 31, 28, 90)
TITLETEXT = (217, 217, 217, 255)
WINCONDITIONTEXTCOLOR = (144, 142, 140, 255)
CROSSCOLOR = WINCONDITIONTEXTCOLOR
GREENBUTTONBACKGROUND = (2, 84, 45, 255)
GREENBUTTONOUTLINE = (20, 174, 92, 255)
GREENBUTTONTEXT = GREENBUTTONOUTLINE
NORMALBUTTONOUTLINE = (94, 93, 91, 255)
NORMALBUTTONBACKGROUND = (48, 46, 43, 255)
NORMALBUTTONTEXT = NORMALBUTTONOUTLINE

class Button:
    def __init__(self, x, y, w, h, text, callback, FONT_SIZE):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback
        self.font = pygame.font.Font('fonts/Roboto-Medium.ttf', int(FONT_SIZE * SCALE))
        self.BORDER_WIDTH = max(1, WIDTH // 600)
        menuX = int(WIDTH // 2 - int(TILESIZE * 1.5))
        menuY = int(HEIGHT // 2 - int(TILESIZE * 1.85))
        self.LEFT = (WIDTH - menuX) // 2
        self.TOP = (HEIGHT - menuY) // 2

    def draw(self, surface, BG_COLOR, BORDER_COLOR, TEXT_COLOR_1):
        pygame.draw.rect(surface, BORDER_COLOR, self.rect, border_radius=int(20 * SCALE))
        pygame.draw.rect(surface, BG_COLOR, (self.rect.x + self.BORDER_WIDTH, self.rect.y + self.BORDER_WIDTH, self.rect.width - self.BORDER_WIDTH * 2, self.rect.height - self.BORDER_WIDTH * 2), border_radius=int(20 * SCALE - 2 * self.BORDER_WIDTH))
        txt_surf = self.font.render(self.text, True, TEXT_COLOR_1)
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        surface.blit(txt_surf, txt_rect)

    def handle_event(self, event):
        if self.rect.collidepoint((event.pos[0] - self.LEFT, event.pos[1] - self.TOP)):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint((event.pos[0] - self.LEFT, event.pos[1] - self.TOP)):
            self.callback()

def drawEndScreen(surface, winner, winCondition, scale, tileSize):
    width, height = surface.get_size()
    BORDER_WIDTH = max(1, width // 600)
    ENDBOX_BORDER_RADIUS = int(25 * scale)
    menuX = int(width // 2 - int(tileSize * 1.5))
    menuY = int(height // 2 - int(tileSize * 1.85))
    
    pygame.font.init()
    headerFont = pygame.font.Font('fonts/Roboto-Medium.ttf', int(30 * scale))
    winConditionFont = pygame.font.Font('fonts/Roboto-Medium.ttf', int(15 * scale))
    
    overlay = pygame.Surface((width, height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    surface.blit(overlay, (0, 0))
    
    pygame.draw.rect(surface, ENDBOXOUTLINE, (menuX, menuY, 3 * tileSize, 3.7 * tileSize), border_radius=ENDBOX_BORDER_RADIUS)
    pygame.draw.rect(surface, ENDBOXBACKGROUND, (menuX + BORDER_WIDTH, menuY + BORDER_WIDTH, 3 * tileSize - BORDER_WIDTH * 2, 3.7 * tileSize - BORDER_WIDTH * 2), border_radius=ENDBOX_BORDER_RADIUS - 2 * BORDER_WIDTH)
    pygame.draw.rect(surface, ENDBOXOUTLINE, (menuX, menuY, 3 * tileSize, 0.9 * tileSize), border_radius=0, border_top_left_radius=ENDBOX_BORDER_RADIUS, border_top_right_radius=ENDBOX_BORDER_RADIUS, border_bottom_left_radius=0, border_bottom_right_radius=0)

    headerString = 'Draw'
    if winner == 'white':
        headerString = 'White wins!'
    elif winner == 'black':
        headerString = 'Black wins!'
        
    headerText = headerFont.render(headerString, True, TITLETEXT)
    headerRect = headerText.get_rect(center=(menuX + 1.5 * tileSize, menuY + 0.38 * tileSize))
    surface.blit(headerText, headerRect)
    winConditionTxt = winConditionFont.render(winCondition, True, WINCONDITIONTEXTCOLOR)
    winConditionRect = winConditionTxt.get_rect(center=(menuX + 1.5 * tileSize, menuY + 0.67 * tileSize))
    surface.blit(winConditionTxt, winConditionRect)
    
    closingCross = pygame.Rect(int(683 * SCALE), int(332 * SCALE), int(20 * SCALE), int(20 * SCALE))
    pygame.draw.rect(surface, ENDBOXOUTLINE, closingCross)
    pygame.draw.aaline(surface, CROSSCOLOR, (int(688 * SCALE), int(332 * SCALE)), (int(708 * SCALE), int(352 * SCALE)))
    pygame.draw.aaline(surface, CROSSCOLOR, (int(708 * SCALE), int(332 * SCALE)), (int(688 * SCALE), int(352 * SCALE)))
    
    buttonHeightIdx = 0
    mainMenuButton = Button(menuX + int(0.2 * tileSize), menuY + int(scale * 105) + int(86 * scale * buttonHeightIdx), int(260 * scale), int(75 * scale), "Main Menu", lambda: print('main menu'), 22)
    buttonHeightIdx += 1
    viewGameButton = Button(menuX + int(0.2 * tileSize), menuY + int(scale * 105) + int(86 * scale * buttonHeightIdx), int(260 * scale), int(75 * scale), "View Game", lambda: print('view game'), 22)
    buttonHeightIdx += 1
    revengeButton = Button(menuX + int(0.2 * tileSize), menuY + int(scale * 105) + int(86 * scale * buttonHeightIdx), int(260 * scale), int(75 * scale), "Revenge", lambda: print('revenge'), 22)
    
    mainMenuButton.draw(surface, GREENBUTTONBACKGROUND, GREENBUTTONOUTLINE, GREENBUTTONTEXT)
    viewGameButton.draw(surface, NORMALBUTTONBACKGROUND, NORMALBUTTONOUTLINE, NORMALBUTTONTEXT)
    revengeButton.draw(surface, NORMALBUTTONBACKGROUND, NORMALBUTTONOUTLINE, NORMALBUTTONTEXT)
    
    return {'main': mainMenuButton, 'view': viewGameButton, 'revenge': revengeButton}