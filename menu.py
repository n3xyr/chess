import pygame
from screeninfo import get_monitors
import webbrowser

def getMonitorResolution():
    for m in get_monitors():
        if m.is_primary:
            return m.width, m.height

SCREENWIDTH, SCREENHEIGHT = getMonitorResolution()
SCALE = float(SCREENHEIGHT * 0.8) / 1000
HEIGHT = int(1000 * SCALE)
WIDTH = int(800 * SCALE)
clock = pygame.time.Clock()

pygame.init()

def resizeWindow():
    global HEIGHT, WIDTH, background, BORDER_WIDTH, BORDER_RADIUS, BUTTON_NUMBER, BUTTON_INDIC
    global menuX, menuY, LEFT, TOP, menuRGBA, textBoxesRGBA
    global robotoMedium, robotoMediumUnderline
    global buttonStart, buttonTimeSetting, buttonIncrementSetting, buttonSettings
    global timeSettingTextEntry

    HEIGHT = int(1000 * SCALE)
    WIDTH = int(800 * SCALE)

    background = pygame.transform.scale(pygame.image.load('startEndScreens/background.png'), (WIDTH, HEIGHT))

    BORDER_WIDTH = max(1, WIDTH // 600)
    BORDER_RADIUS = int(0.0625 * WIDTH)
    BUTTON_NUMBER = 4
    BUTTON_INDIC = 1

    menuX = int(0.4375 * WIDTH)
    menuY = int(0.417 * HEIGHT)
    LEFT = (WIDTH - menuX) // 2
    TOP = (HEIGHT - menuY) // 2

    menuRGBA = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    textBoxesRGBA = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

    pygame.font.init()
    robotoMedium = pygame.font.Font('fonts/Roboto-Medium.ttf', int(18 * SCALE))
    robotoMediumUnderline = pygame.font.Font('fonts/Roboto-Medium.ttf', int(18 * SCALE))
    robotoMediumUnderline.set_underline(True)

    # Buttons
    def button_y(indic):
        return int(80 * SCALE + (menuY - int(0.076 * HEIGHT) * BUTTON_NUMBER) // (BUTTON_NUMBER + 1) * indic + int(0.076 * HEIGHT) * (indic - 1))
    def button_x():
        return (menuX - int(WIDTH * 0.375)) // 2
    def button_w():
        return int(WIDTH * 0.375)
    def button_h():
        return int(0.076 * HEIGHT)

    def centeredTextEntry_x():
        return int((1/3 * menuX))
    
    def centeredTextEntry_y(BUTTON_INDIC):
        return int((1/(BUTTON_NUMBER + 1) * menuY + int(0.076 * HEIGHT)) * BUTTON_INDIC - int(0.076 * HEIGHT))
    
    def centeredTextEntry_w():
        return int((1/3) * button_w())
    
    def centeredTextEntry_h():
        return int(3/5 * button_h())

    BUTTON_INDIC = 1
    buttonStart = Button(button_x(), button_y(BUTTON_INDIC), button_w(), button_h(), "Start Game", lambda: print("Start Game"))
    
    BUTTON_INDIC += 1
    buttonTimeSetting = Button(button_x(), button_y(BUTTON_INDIC), button_w(), button_h(), "10", lambda: print("Time Setting"))
    timeSettingTextEntry = textEntry(buttonTimeSetting, "10")

    BUTTON_INDIC += 1
    buttonIncrementSetting = Button(button_x(), button_y(BUTTON_INDIC), button_w(), button_h(), "5", lambda: print("Increment Setting"))
    
    BUTTON_INDIC += 1
    buttonSettings = Button(button_x(), button_y(BUTTON_INDIC), button_w(), button_h(), "Settings", lambda: print("Settings"))


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


class textEntry:
    def __init__(self, button, initial_text=""):
        self.rect = button.rect
        self.text = initial_text
        self.isEntrying = False
        self.font = pygame.font.Font('fonts/Roboto-Medium.ttf', int(22 * SCALE))
        self.button = button

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255, 0), self.rect)

        if self.isEntrying:
            text_surface = self.font.render(self.text, True, (128, 255, 128, 128))
            
        else:
            text_surface = self.font.render(self.text, True, (255, 255, 255, 128))

        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect.center)

    def testEntrying(self, pos):
        if self.rect.collidepoint(pos):
            self.isEntrying = True
        else:
            self.isEntrying = False

class Button:
    def __init__(self, x, y, w, h, text, callback):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback
        self.font = pygame.font.Font('fonts/Roboto-Medium.ttf', int(22 * SCALE))

    def draw(self, surface, BG_COLOR, BORDER_COLOR, TEXT_COLOR_1, TEXT_COLOR_2=None, LINE_COLOR=None, LABEL=None, UNIT=None):
        pygame.draw.rect(surface, BORDER_COLOR, self.rect, border_radius=int(0.036 * HEIGHT))
        pygame.draw.rect(surface, BG_COLOR, (self.rect.x + BORDER_WIDTH, self.rect.y + BORDER_WIDTH, self.rect.width - BORDER_WIDTH * 2, self.rect.height - BORDER_WIDTH * 2), border_radius=int(0.036 * HEIGHT - 2 * BORDER_WIDTH))
        if TEXT_COLOR_2 is not None:
            txt_surf = self.font.render(self.text, True, TEXT_COLOR_1)
            txt_rect = txt_surf.get_rect(center=self.rect.center)
            
            label_surf = robotoMedium.render(LABEL, True, TEXT_COLOR_2)
            label_rect = label_surf.get_rect(midleft=(self.rect.left + int(30 * SCALE), self.rect.centery))
            
            unit_surf = robotoMedium.render(UNIT, True, TEXT_COLOR_2)
            unit_rect = unit_surf.get_rect(midright=(self.rect.right - int(30 * SCALE), self.rect.centery))
            
            pygame.draw.line(surface, LINE_COLOR, (self.rect.left + int(85 * SCALE), self.rect.centery + int(19 * SCALE)), (self.rect.left + int(85 * SCALE), self.rect.centery - int(19 * SCALE)))
            pygame.draw.line(surface, LINE_COLOR, (self.rect.right - int(85 * SCALE), self.rect.centery + int(19 * SCALE)), (self.rect.right - int(85 * SCALE), self.rect.centery - int(19 * SCALE)))
            
            surface.blit(txt_surf, txt_rect)
            surface.blit(label_surf, label_rect)
            surface.blit(unit_surf, unit_rect)
        else:
            txt_surf = self.font.render(self.text, True, TEXT_COLOR_1)
            txt_rect = txt_surf.get_rect(center=self.rect.center)
            surface.blit(txt_surf, txt_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint((event.pos[0] - LEFT, event.pos[1] - TOP)):
            self.callback()

resizeWindow()

def drawButtons(surface):
        buttonStart.draw(surface, DARKGREEN, GREEN, GREEN)
        buttonTimeSetting.draw(surface, TEXTBOX_BG, BORDER, BUTTON_TEXT, TEXT_COLOR_2=BORDER, LINE_COLOR=TEXTBOX_LINE, LABEL="time", UNIT="min")
        buttonIncrementSetting.draw(surface, TEXTBOX_BG, BORDER, BUTTON_TEXT, TEXT_COLOR_2=BORDER, LINE_COLOR=TEXTBOX_LINE, LABEL="incr.", UNIT="sec")
        buttonSettings.draw(surface, BUTTON_BG, BORDER, BUTTON_TEXT)


def getPressedKeys(keys):
    pressed = []
    for k, v in keys.items():
        if v:
            pressed.append(k)
    return pressed


def main():
    global SCALE
    clock.tick(60)
    time_delta = clock.tick(60) / 1000
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Chess")
    running = True
    while running:
        screen.blit(background, (0, 0))
        pygame.draw.rect(menuRGBA, BORDER, (0, int(80 * SCALE), menuX, menuY), border_radius=BORDER_RADIUS)
        pygame.draw.rect(menuRGBA, PANEL_BG, (BORDER_WIDTH, int(81 * SCALE), menuX - BORDER_WIDTH * 2, menuY - BORDER_WIDTH * 2), border_radius=BORDER_RADIUS - 2 * BORDER_WIDTH)
        
        drawButtons(menuRGBA)
        timeSettingTextEntry.draw(textBoxesRGBA)
        
        github_text = robotoMediumUnderline.render("View on GitHub", True, LINK_COLOR)
        github_rect = github_text.get_rect(center=(WIDTH // 2, int(0.95 * HEIGHT)))
        githubLink = screen.blit(github_text, github_rect)
        screen.blit(menuRGBA, (LEFT, TOP))
        screen.blit(textBoxesRGBA, (LEFT, TOP))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            timeSettingTextEntry.testEntrying(pygame.mouse.get_pos())

            if timeSettingTextEntry.isEntrying:
                print("Entering text")
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    pressedKeys = getPressedKeys(keys)
                    for key in pressedKeys:
                        print(key)
                        # timeSettingTextEntry.text += key
                    
                    

            if event.type == pygame.VIDEORESIZE:
                newHeight = event.h
                newWidth = event.w
                if newWidth < 40 or newHeight < 50:
                    newWidth = 40
                    newHeight = 50
                elif newWidth > SCREENWIDTH or newHeight > SCREENHEIGHT:
                    newWidth = SCREENWIDTH
                    newHeight = SCREENHEIGHT
                if newWidth == WIDTH and newHeight != HEIGHT:
                    SCALE = newHeight / 1000
                else:
                    SCALE = newWidth / 1000
                resizeWindow()
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if githubLink.collidepoint(pos):
                    webbrowser.open(r"https://www.github.com/n3xyr/chess")
                buttonStart.handle_event(event)
                buttonTimeSetting.handle_event(event)
                buttonIncrementSetting.handle_event(event)
                buttonSettings.handle_event(event)
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()