import pygame
import subprocess

WINDOWDARKTRANSPARENCY = (0, 0, 0, 128)
ENDBOXOUTLINE = (60, 58, 56, 255)
ENDBOXOUTLINETRANSPARENT = (60, 58, 56, 240)
ENDBOXBACKGROUND = (31, 31, 28, 240)
TITLETEXT = (217, 217, 217, 255)
WINCONDITIONTEXTCOLOR = (144, 142, 140, 255)
CROSSCOLOR = WINCONDITIONTEXTCOLOR
GREENBUTTONBACKGROUND = (2, 84, 45, 255)
GREENBUTTONOUTLINE = (20, 174, 92, 255)
GREENBUTTONTEXT = GREENBUTTONOUTLINE
NORMALBUTTONOUTLINE = (94, 93, 91, 255)
NORMALBUTTONBACKGROUND = (48, 46, 43, 255)
NORMALBUTTONTEXT = NORMALBUTTONOUTLINE
REPLAY = False

showEndScreen = True
viewingGame = False

class Button:
    def __init__(self, x, y, w, h, text, callback, FONT_SIZE, SCALE, WIDTH, borderRadius):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback
        self.font = pygame.font.Font('fonts/Roboto-Medium.ttf', int(FONT_SIZE * SCALE))
        self.BORDER_WIDTH = max(1, WIDTH // 600)
        self.SCALE = SCALE
        self.borderRadius = borderRadius

    def draw(self, surface, BG_COLOR, BORDER_COLOR, TEXT_COLOR_1):
        pygame.draw.rect(surface, BORDER_COLOR, self.rect, border_radius=int(self.borderRadius * self.SCALE))
        pygame.draw.rect(surface, BG_COLOR, (self.rect.x + self.BORDER_WIDTH, self.rect.y + self.BORDER_WIDTH, self.rect.width - self.BORDER_WIDTH * 2, self.rect.height - self.BORDER_WIDTH * 2), border_radius=int(self.borderRadius * self.SCALE - 2 * self.BORDER_WIDTH))
        txt_surf = self.font.render(self.text, True, TEXT_COLOR_1)
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        surface.blit(txt_surf, txt_rect)

    def handle_event(self, event):
        if self.rect.collidepoint((event.pos[0], event.pos[1])):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)           
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint((event.pos[0], event.pos[1])):
            self.callback()

class EndScreen:
    def __init__(self, winner, winCondition, width, height, tileSize):
        self.winner = winner
        self.winCondition = winCondition
        self.menuX = int(width // 2 - int(tileSize * 1.5))
        self.menuY = int(height // 2 - int(tileSize * 1.85))
    
    def defineButtons(self, scale, tileSize, width, height):
        self.closingCrossButton = Button(int(688 * scale), int(332 * scale), int(20 * scale), int(20 * scale), '', lambda: viewGameAction(scale), 0, scale, height, 0)

        buttonHeightIdx = 0
        self.mainMenuButton = Button(self.menuX + int(0.2 * tileSize), self.menuY + int(scale * 105) + int(86 * scale * buttonHeightIdx), int(260 * scale), int(75 * scale), "Main Menu", lambda: mainMenuAction(), 22, scale, height, 20)
        buttonHeightIdx += 1
        self.viewGameButton = Button(self.menuX + int(0.2 * tileSize), self.menuY + int(scale * 105) + int(86 * scale * buttonHeightIdx), int(260 * scale), int(75 * scale), "View Game", lambda: viewGameAction(scale), 22, scale, height, 20)
        buttonHeightIdx += 1
        self.revengeButton = Button(self.menuX + int(0.2 * tileSize), self.menuY + int(scale * 105) + int(86 * scale * buttonHeightIdx), int(260 * scale), int(75 * scale), "Revenge", lambda: revengeAction(), 22, scale, height, 20)

    def handleEvents(self, event):
        self.closingCrossButton.handle_event(event)
        self.mainMenuButton.handle_event(event)
        self.viewGameButton.handle_event(event)
        self.revengeButton.handle_event(event)

    def draw(self, surface, scale, tileSize):
        width, height = surface.get_size()
        BORDER_WIDTH = max(1, width // 600)
        ENDBOX_BORDER_RADIUS = int(25 * scale)
        
        pygame.font.init()
        headerFont = pygame.font.Font('fonts/Roboto-Medium.ttf', int(30 * scale))
        winConditionFont = pygame.font.Font('fonts/Roboto-Medium.ttf', int(15 * scale))
        
        overlay = pygame.Surface((width, height), pygame.SRCALPHA)
        overlay.fill(WINDOWDARKTRANSPARENCY)
        
        pygame.draw.rect(overlay, ENDBOXOUTLINETRANSPARENT, (self.menuX, self.menuY, 3 * tileSize, 3.7 * tileSize), border_radius=ENDBOX_BORDER_RADIUS)
        pygame.draw.rect(overlay, ENDBOXBACKGROUND, (self.menuX + BORDER_WIDTH, self.menuY + BORDER_WIDTH, 3 * tileSize - BORDER_WIDTH * 2, 3.7 * tileSize - BORDER_WIDTH * 2), border_radius=ENDBOX_BORDER_RADIUS - 2 * BORDER_WIDTH)
        surface.blit(overlay, (0, 0))
        pygame.draw.rect(surface, ENDBOXOUTLINE, (self.menuX, self.menuY, 3 * tileSize, 0.9 * tileSize), border_radius=0, border_top_left_radius=ENDBOX_BORDER_RADIUS, border_top_right_radius=ENDBOX_BORDER_RADIUS, border_bottom_left_radius=0, border_bottom_right_radius=0)

        headerString = 'Draw'
        if self.winner == 'white':
            headerString = 'White wins!'
        elif self.winner == 'black':
            headerString = 'Black wins!'
            
        headerText = headerFont.render(headerString, True, TITLETEXT)
        headerRect = headerText.get_rect(center=(self.menuX + 1.5 * tileSize, self.menuY + 0.38 * tileSize))
        surface.blit(headerText, headerRect)
        winConditionTxt = winConditionFont.render(self.winCondition, True, WINCONDITIONTEXTCOLOR)
        winConditionRect = winConditionTxt.get_rect(center=(self.menuX + 1.5 * tileSize, self.menuY + 0.67 * tileSize))
        surface.blit(winConditionTxt, winConditionRect)
        
        closingCross = pygame.Rect(int(683 * scale), int(332 * scale), int(20 * scale), int(20 * scale))
        self.closingCrossButton.draw(surface, ENDBOXOUTLINE, ENDBOXOUTLINE, ENDBOXOUTLINE)

        pygame.draw.rect(surface, ENDBOXOUTLINE, closingCross)
        pygame.draw.aaline(surface, CROSSCOLOR, (int(688 * scale), int(332 * scale)), (int(708 * scale), int(352 * scale)))
        pygame.draw.aaline(surface, CROSSCOLOR, (int(708 * scale), int(332 * scale)), (int(688 * scale), int(352 * scale)))
        
        self.mainMenuButton.draw(surface, GREENBUTTONBACKGROUND, GREENBUTTONOUTLINE, GREENBUTTONTEXT)
        self.viewGameButton.draw(surface, NORMALBUTTONBACKGROUND, NORMALBUTTONOUTLINE, NORMALBUTTONTEXT)
        self.revengeButton.draw(surface, NORMALBUTTONBACKGROUND, NORMALBUTTONOUTLINE, NORMALBUTTONTEXT)

def mainMenuAction():
    pygame.quit()
    subprocess.run(["python", "menu.py"])

def viewGameAction(scale):
    global showEndScreen, viewingGame, inGameMainMenuButton
    showEndScreen = False
    viewingGame = True
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    inGameMainMenuButton = Button(int(825 * scale), int(905 * scale), int(300 * scale), int(75 * scale), "Main Menu", lambda: mainMenuAction(), 22, scale, 0, 20)

def revengeAction():
    global REPLAY
    REPLAY = True