import pygame
import webbrowser

HEIGHT = 1000
WIDTH = 800

background = pygame.transform.scale(pygame.image.load('startEndScreens/background.png'), (WIDTH, HEIGHT))

PANEL_BG = (31, 31, 28, 192)

BORDER = pygame.Color("#5E5D5B")

DARKGREEN = pygame.Color("#02542D")
GREEN = pygame.Color("#14AE5C")

BUTTON_BG = (50, 50, 50)
BUTTON_TEXT = (150, 150, 150)

TEXTBOX_BG = pygame.Color("#211f1d")
TEXTBOX_TEXT = (94, 93, 91)
TEXTBOX_LINE = (94, 93, 91, 102)

LINK_COLOR = pygame.Color("#C6C6C6")

BORDER_WIDTH = WIDTH // 600
BORDER_RADIUS = int(0.0625 * WIDTH)
BUTTON_NUMBER = 4
BUTTON_INDIC = 1

menuX = int(0.4375 * WIDTH)
menuY = int(0.417 * HEIGHT)

LEFT = (WIDTH - menuX) // 2
TOP = (HEIGHT - menuY) // 2

menuRGBA = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

pygame.font.init()

robotoMedium = pygame.font.Font('fonts/Roboto-Medium.ttf', 18)
robotoMediumUnderline = pygame.font.Font('fonts/Roboto-Medium.ttf', 18)
robotoMediumUnderline.set_underline(True)

class Button:
    def __init__(self, x, y, w, h, text, callback):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback
        self.font = pygame.font.Font('fonts/Roboto-Medium.ttf', 22)

    def draw(self, surface, BG_COLOR, BORDER_COLOR, TEXT_COLOR_1, TEXT_COLOR_2=None, LINE_COLOR=None, LABEL=None, UNIT=None):
        pygame.draw.rect(surface, BORDER_COLOR, self.rect, border_radius=int(0.036 * HEIGHT))
        pygame.draw.rect(surface, BG_COLOR, (self.rect.x + BORDER_WIDTH, self.rect.y + BORDER_WIDTH, self.rect.width - BORDER_WIDTH * 2, self.rect.height - BORDER_WIDTH * 2), border_radius=int(0.038 * HEIGHT - 2 * BORDER_WIDTH))
        if TEXT_COLOR_2 is not None:
            txt_surf = self.font.render(self.text, True, TEXT_COLOR_1)
            txt_rect = txt_surf.get_rect(center=self.rect.center)
            label_surf = robotoMedium.render(LABEL, True, TEXT_COLOR_2)
            label_rect = label_surf.get_rect(midleft=(self.rect.left + 30, self.rect.centery))
            unit_surf = robotoMedium.render(UNIT, True, TEXT_COLOR_2)
            unit_rect = unit_surf.get_rect(midright=(self.rect.right - 30, self.rect.centery))
            pygame.draw.line(surface, LINE_COLOR, (self.rect.left + 85, self.rect.centery + 19), (self.rect.left + 85, self.rect.centery - 19))
            pygame.draw.line(surface, LINE_COLOR, (self.rect.right - 85, self.rect.centery + 19), (self.rect.right - 85, self.rect.centery - 19))
            surface.blit(txt_surf, txt_rect)
            surface.blit(label_surf, label_rect)
            surface.blit(unit_surf, unit_rect)
        else:
            txt_surf = self.font.render(self.text, True, TEXT_COLOR_1)
            txt_rect = txt_surf.get_rect(center=self.rect.center)
            surface.blit(txt_surf, txt_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.callback()

buttonStart = Button((menuX - WIDTH * 0.375) // 2, (80 + (menuY - 0.076 * HEIGHT * BUTTON_NUMBER) // (BUTTON_NUMBER + 1) * BUTTON_INDIC + 0.076 * HEIGHT * (BUTTON_INDIC - 1)), WIDTH * 0.375, 0.076 * HEIGHT, "Start Game", lambda: print("Start Game"))
BUTTON_INDIC += 1
buttonTimeSetting = Button((menuX - WIDTH * 0.375) // 2, (80 + (menuY - 0.076 * HEIGHT * BUTTON_NUMBER) // (BUTTON_NUMBER + 1) * BUTTON_INDIC + 0.076 * HEIGHT * (BUTTON_INDIC - 1)), WIDTH * 0.375, 0.076 * HEIGHT, "30", lambda: print("Time Setting"))
BUTTON_INDIC += 1
buttonIncrementSetting = Button((menuX - WIDTH * 0.375) // 2, (80 + (menuY - 0.076 * HEIGHT * BUTTON_NUMBER) // (BUTTON_NUMBER + 1) * BUTTON_INDIC + 0.076 * HEIGHT * (BUTTON_INDIC - 1)), WIDTH * 0.375, 0.076 * HEIGHT, "10", lambda: print("Increment Setting"))
BUTTON_INDIC += 1
buttonSettings = Button((menuX - WIDTH * 0.375) // 2, (80 + (menuY - 0.076 * HEIGHT * BUTTON_NUMBER) // (BUTTON_NUMBER + 1) * BUTTON_INDIC + 0.076 * HEIGHT * (BUTTON_INDIC - 1)), WIDTH * 0.375, 0.076 * HEIGHT, "Settings", lambda: print("Settings"))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")
    # Load your chess board and pieces here
    # For example:
    # board = load_board()
    
    running = True
    while running:
        screen.blit(background, (0, 0))
        pygame.draw.rect(menuRGBA, BORDER, (0, 80, menuX, menuY), border_radius=BORDER_RADIUS)
        pygame.draw.rect(menuRGBA, PANEL_BG, (BORDER_WIDTH, 81, menuX - BORDER_WIDTH * 2, menuY - BORDER_WIDTH * 2), border_radius=BORDER_RADIUS - 2 * BORDER_WIDTH)
        buttonStart.draw(menuRGBA, DARKGREEN, GREEN, GREEN)
        buttonTimeSetting.draw(menuRGBA, TEXTBOX_BG, BORDER, BUTTON_TEXT, TEXT_COLOR_2=BORDER, LINE_COLOR=TEXTBOX_LINE, LABEL="time", UNIT="min")
        buttonIncrementSetting.draw(menuRGBA, TEXTBOX_BG, BORDER, BUTTON_TEXT, TEXT_COLOR_2=BORDER, LINE_COLOR=TEXTBOX_LINE, LABEL="incr.", UNIT="sec")
        buttonSettings.draw(menuRGBA, BUTTON_BG, BORDER, BUTTON_TEXT)
        githubLink = screen.blit(robotoMediumUnderline.render("View on GitHub", True, LINK_COLOR), (int(WIDTH // 2 - 62 * (WIDTH // 800)), int(0.95 * HEIGHT)))
        screen.blit(menuRGBA, (LEFT, TOP))
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            if githubLink.collidepoint(pos):
                webbrowser.open(r"https://www.github.com/n3xyr/chess")
        
        # Update the display
        # display_board(screen, board)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()