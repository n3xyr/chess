import pygame
from screeninfo import get_monitors
import webbrowser
import display_board
import time

def getMonitorResolution():
    for m in get_monitors():
        if m.is_primary:
            return m.width, m.height

NUMBER_KEYS_WITH_NUMPAD = [
    pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
    pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,
    pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4,
    pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9
]

MAGNITUDE_DIC = {
    1: 'sec',
    60: 'min',
    3600: 'h'
}

pygame.display.set_caption("Chess")
SCREENWIDTH, SCREENHEIGHT = getMonitorResolution()
SCALE = float(SCREENHEIGHT * 0.8) / 1000
HEIGHT = int(1000 * SCALE)
WIDTH = int(800 * SCALE)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
timeMagnitude = 60
incrementMagnitude = 1

pygame.init()

def resizeWindow():
    global HEIGHT, WIDTH, background, BORDER_WIDTH, BORDER_RADIUS, BUTTON_NUMBER, BUTTON_INDIC
    global menuX, menuY, LEFT, TOP, menuRGBA
    global robotoMedium, robotoMediumUnderline
    global buttonStart, buttonTimeSetting, buttonIncrementSetting, buttonSettings
    global buttonTimeMagnitude, buttonIncrementMagnitude
    global timeMagnitude, incrementMagnitude
    global MAGNITUDE_DIC

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

    pygame.font.init()
    robotoMedium = pygame.font.Font('fonts/Roboto-Medium.ttf', int(25 * SCALE))
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
    
    BUTTON_INDIC = 1
    buttonStart = Button(button_x(), button_y(BUTTON_INDIC), button_w(), button_h(), "Start Game", lambda: display_board.main(timeMagnitude * int(buttonTimeSetting.text), incrementMagnitude * int(buttonIncrementSetting.text)), 22)
    
    BUTTON_INDIC += 1
    buttonTimeSetting = entryButton(button_x(), button_y(BUTTON_INDIC), WIDTH * 0.26, button_h(), "10", lambda: getTypedTextTime())
    UNIT = MAGNITUDE_DIC[timeMagnitude]
    buttonTimeMagnitude = Button(button_x() + (226 * SCALE), button_y(BUTTON_INDIC), button_h(), button_h(), UNIT, lambda: timeIncreaseMagnitude(), 23)
    buttonTimeSetting.set_text_entry(False)

    BUTTON_INDIC += 1
    buttonIncrementSetting = entryButton(button_x(), button_y(BUTTON_INDIC), WIDTH * 0.26, button_h(), "5", lambda: getTypedTextIncrement())
    UNIT = MAGNITUDE_DIC[incrementMagnitude]
    buttonIncrementMagnitude = Button(button_x() + (226 * SCALE), button_y(BUTTON_INDIC), button_h(), button_h(), UNIT, lambda: incrementIncreaseMagnitude(), 23)
    buttonIncrementSetting.set_text_entry(False)

    BUTTON_INDIC += 1
    buttonSettings = Button(button_x(), button_y(BUTTON_INDIC), button_w(), button_h(), "Settings", lambda: print("Settings"), 22)


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


class Button:
    def __init__(self, x, y, w, h, text, callback, FONT_SIZE):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback
        self.font = pygame.font.Font('fonts/Roboto-Medium.ttf', int(FONT_SIZE * SCALE))

    def draw(self, surface, BG_COLOR, BORDER_COLOR, TEXT_COLOR_1):
        pygame.draw.rect(surface, BORDER_COLOR, self.rect, border_radius=int(0.036 * HEIGHT))
        pygame.draw.rect(surface, BG_COLOR, (self.rect.x + BORDER_WIDTH, self.rect.y + BORDER_WIDTH, self.rect.width - BORDER_WIDTH * 2, self.rect.height - BORDER_WIDTH * 2), border_radius=int(0.036 * HEIGHT - 2 * BORDER_WIDTH))
        txt_surf = self.font.render(self.text, True, TEXT_COLOR_1)
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        surface.blit(txt_surf, txt_rect)

    def handle_event(self, event):
        if self.rect.collidepoint((event.pos[0] - LEFT, event.pos[1] - TOP)):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint((event.pos[0] - LEFT, event.pos[1] - TOP)):
            self.callback()


class entryButton:
    def __init__(self, x, y, w, h, text, callback):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback
        self.font = pygame.font.Font('fonts/Roboto-Medium.ttf', int(22 * SCALE))

    def draw(self, surface, BG_COLOR, BORDER_COLOR, TEXT_COLOR_1, TEXT_COLOR_2, LINE_COLOR, LABEL, FONT_SIZE):
        font = pygame.font.Font('fonts/Roboto-Medium.ttf', int(FONT_SIZE * SCALE))
        pygame.draw.rect(surface, BORDER_COLOR, self.rect, border_radius=int(0.036 * HEIGHT))
        pygame.draw.rect(surface, BG_COLOR, (self.rect.x + BORDER_WIDTH, self.rect.y + BORDER_WIDTH, self.rect.width - BORDER_WIDTH * 2, self.rect.height - BORDER_WIDTH * 2), border_radius=int(0.036 * HEIGHT - 2 * BORDER_WIDTH))
        txt_surf = self.font.render(self.text, True, TEXT_COLOR_1)
        txt_rect = txt_surf.get_rect(centerx = self.rect.center[0] + (40 * SCALE), centery=self.rect.center[1])
        
        label_surf = font.render(LABEL, True, TEXT_COLOR_2)
        label_rect = label_surf.get_rect(midleft=(self.rect.left + int(25 * SCALE), self.rect.centery))

        for i in range(2):
            pygame.draw.line(surface, LINE_COLOR, (self.rect.left + int(90 * SCALE + i), self.rect.centery + int(19 * SCALE)), (self.rect.left + int(90 * SCALE + i), self.rect.centery - int(19 * SCALE)))
        
        surface.blit(txt_surf, txt_rect)
        surface.blit(label_surf, label_rect)

    def set_text_entry(self, bool=True):
        self.text_entry = bool

    def handle_event(self, event):            
        if self.rect.collidepoint((event.pos[0] - LEFT, event.pos[1] - TOP)):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.callback()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.text_entry = False

    def set_text(self, new_text):
        self.text = new_text
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))

resizeWindow()

def drawButtons(surface):
    buttonStart.draw(surface, DARKGREEN, GREEN, GREEN)
    
    buttonTimeSetting.draw(surface, TEXTBOX_BG, BORDER, BUTTON_TEXT, BORDER, TEXTBOX_LINE, "time", 22)
    buttonTimeMagnitude.draw(surface, BUTTON_BG, BUTTON_BG, BUTTON_TEXT)

    buttonIncrementSetting.draw(surface, TEXTBOX_BG, BORDER, BUTTON_TEXT, BORDER, TEXTBOX_LINE, "incr.", 22)
    buttonIncrementMagnitude.draw(surface, BUTTON_BG, BUTTON_BG, BUTTON_TEXT)

    buttonSettings.draw(surface, BUTTON_BG, BORDER, BUTTON_TEXT)


def getTypedTextTime():
    buttonTimeSetting.set_text_entry()


def getTypedTextIncrement():
    buttonIncrementSetting.set_text_entry()


def timeIncreaseMagnitude(): 
    global timeMagnitude
    if timeMagnitude == 3600:
        timeMagnitude = 1
    elif timeMagnitude == 60:
        timeMagnitude = 3600
    else:
        timeMagnitude = 60


def incrementIncreaseMagnitude():
    global incrementMagnitude
    if incrementMagnitude == 3600:
        incrementMagnitude = 1
    elif incrementMagnitude == 60:
        incrementMagnitude = 3600
    else:
        incrementMagnitude = 60


def drawCursor(textBox):
    center = textBox.rect.center
    textWidth = textBox.font.size(textBox.text)[0]
    textLength = len(textBox.text)
    if textLength:
        cursorLeft = int(textBox.rect.left + 145 * SCALE + textWidth / 2 + 0.2 * textWidth / textLength)
    else:
        cursorLeft = int(textBox.rect.left + 145 * SCALE)
        
    cursorTop = int(center[1] - 2 / 4 * int(22 * SCALE))
    cursorWidth = int(0.003 * WIDTH)
    cursorHeight = int(0.024 * HEIGHT)
    
    pygame.draw.rect(menuRGBA, BUTTON_TEXT, ((cursorLeft, cursorTop), (cursorWidth, cursorHeight)))


def setMagnitudes():
    UNIT = MAGNITUDE_DIC[timeMagnitude]
    buttonTimeMagnitude.text = UNIT
    
    UNIT = MAGNITUDE_DIC[incrementMagnitude]
    buttonIncrementMagnitude.text = UNIT
    
def blinkCursor():
    return (time.time() % 1.4) < 0.7

def main():
    global SCALE, screen
    clock.tick(60)
    running = True

    while running:
        screen.blit(background, (0, 0))
        pygame.draw.rect(menuRGBA, BORDER, (0, int(80 * SCALE), menuX, menuY), border_radius=BORDER_RADIUS)
        pygame.draw.rect(menuRGBA, PANEL_BG, (BORDER_WIDTH, int(81 * SCALE), menuX - BORDER_WIDTH * 2, menuY - BORDER_WIDTH * 2), border_radius=BORDER_RADIUS - 2 * BORDER_WIDTH)
        setMagnitudes()
        drawButtons(menuRGBA)
        
        github_text = robotoMediumUnderline.render("View on GitHub", True, LINK_COLOR)
        github_rect = github_text.get_rect(center=(WIDTH // 2, int(0.95 * HEIGHT)))
        githubLink = screen.blit(github_text, github_rect)
        if blinkCursor():
            if buttonTimeSetting.text_entry:
                drawCursor(buttonTimeSetting)
            if buttonIncrementSetting.text_entry:
                drawCursor(buttonIncrementSetting)

        screen.blit(menuRGBA, (LEFT, TOP))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if buttonTimeSetting.text_entry:
                inputText = buttonTimeSetting.text

                if event.type == pygame.KEYDOWN:
                    if event.key in NUMBER_KEYS_WITH_NUMPAD:
                        inputText += str(NUMBER_KEYS_WITH_NUMPAD.index(event.key) % 10)
                    if event.key == pygame.K_BACKSPACE:
                        inputText = inputText[:-1]
                    if event.key == pygame.K_RETURN:
                        buttonTimeSetting.set_text_entry(False)
                if len(inputText) <= 6:
                    buttonTimeSetting.set_text(inputText)
            elif len(buttonTimeSetting.text) == 0:
                buttonTimeSetting.set_text('10')

            if buttonIncrementSetting.text_entry:
                inputText = buttonIncrementSetting.text

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    buttonIncrementSetting.set_text_entry(False)

                if event.type == pygame.KEYDOWN:
                    if event.key in NUMBER_KEYS_WITH_NUMPAD:
                        inputText += str(NUMBER_KEYS_WITH_NUMPAD.index(event.key) % 10)
                    if event.key == pygame.K_BACKSPACE:
                        inputText = inputText[:-1]
                    if event.key == pygame.K_RETURN:
                        buttonIncrementSetting.set_text_entry(False)
                if len(inputText) <= 6:
                    buttonIncrementSetting.set_text(inputText)
            elif len(buttonIncrementSetting.text) == 0:
                buttonIncrementSetting.set_text('5')

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

            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                buttonStart.handle_event(event)
                    
                buttonTimeSetting.handle_event(event)
                buttonTimeMagnitude.handle_event(event)
                
                buttonIncrementSetting.handle_event(event)
                buttonIncrementMagnitude.handle_event(event)

                buttonSettings.handle_event(event)
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()