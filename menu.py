import pygame

HEIGHT = 1000
WIDTH = 800

background = pygame.transform.scale(pygame.image.load('C:\\Users\\unkno\\Downloads\\test\\imagechessmenu.png'), (WIDTH, HEIGHT))

PANEL_BG = (30, 30, 30, 169)

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
DARKGREEN = (0, 150, 0)
BORDER_COLOR = (100, 100, 100)
BORDER_WIDTH = WIDTH // 400
BORDER_RADIUS = int(0.0625 * WIDTH)
BUTTON_NUMBER = 4
BUTTON_INDIC = 1

menuX = int(0.4375 * WIDTH)
menuY = int(0.417 * HEIGHT)

LEFT = (WIDTH - menuX) // 2
TOP = (HEIGHT - menuY) // 2

menuRGBA = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

pygame.font.init()

class Button:
    def __init__(self, x, y, w, h, text, callback):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback
        self.font = pygame.font.SysFont(None, 40)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        color = DARKGREEN if self.rect.collidepoint(mouse_pos) else GREEN
        pygame.draw.rect(surface, BORDER_COLOR, self.rect, border_radius=int(0.036 * HEIGHT))
        pygame.draw.rect(surface, color, (self.rect.x + BORDER_WIDTH, self.rect.y + BORDER_WIDTH, self.rect.width - BORDER_WIDTH * 2, self.rect.height - BORDER_WIDTH * 2), border_radius=int(0.036 * HEIGHT - 2 * BORDER_WIDTH))
        txt_surf = self.font.render(self.text, True, WHITE)
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        surface.blit(txt_surf, txt_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.callback()

buttonStart = Button((menuX - WIDTH * 0.375) // 2, (menuY - 0.076 * HEIGHT * BUTTON_NUMBER) // (BUTTON_NUMBER + 1) * BUTTON_INDIC + 0.076 * HEIGHT * (BUTTON_INDIC - 1), WIDTH * 0.375, 0.076 * HEIGHT, "Start Game", lambda: print("Start Game"))
BUTTON_INDIC += 1
buttonTimeSeting = Button((menuX - WIDTH * 0.375) // 2, (menuY - 0.076 * HEIGHT * BUTTON_NUMBER) // (BUTTON_NUMBER + 1) * BUTTON_INDIC + 0.076 * HEIGHT * (BUTTON_INDIC - 1), WIDTH * 0.375, 0.076 * HEIGHT, "Time Setting", lambda: print("Time Setting"))
BUTTON_INDIC += 1
buttonIncrementSeting = Button((menuX - WIDTH * 0.375) // 2, (menuY - 0.076 * HEIGHT * BUTTON_NUMBER) // (BUTTON_NUMBER + 1) * BUTTON_INDIC + 0.076 * HEIGHT * (BUTTON_INDIC - 1), WIDTH * 0.375, 0.076 * HEIGHT, "Increment Setting", lambda: print("Increment Setting"))
BUTTON_INDIC += 1
buttonSetings = Button((menuX - WIDTH * 0.375) // 2, (menuY - 0.076 * HEIGHT * BUTTON_NUMBER) // (BUTTON_NUMBER + 1) * BUTTON_INDIC + 0.076 * HEIGHT * (BUTTON_INDIC - 1), WIDTH * 0.375, 0.076 * HEIGHT, "Settings", lambda: print("Settings"))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess Display Board")
    # Load your chess board and pieces here
    # For example:
    # board = load_board()
    
    running = True
    while running:
        screen.blit(background, (0, 0))
        pygame.draw.rect(menuRGBA, BORDER_COLOR, (0, 0, menuX, menuY), border_radius=BORDER_RADIUS)
        pygame.draw.rect(menuRGBA, PANEL_BG, (BORDER_WIDTH, BORDER_WIDTH, menuX - BORDER_WIDTH * 2, menuY - BORDER_WIDTH * 2), border_radius=BORDER_RADIUS - 2 * BORDER_WIDTH)
        buttonStart.draw(menuRGBA)
        buttonTimeSeting.draw(menuRGBA)
        buttonIncrementSeting.draw(menuRGBA)
        buttonSetings.draw(menuRGBA)
        screen.blit(menuRGBA, (LEFT, TOP))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update the display
        # display_board(screen, board)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()