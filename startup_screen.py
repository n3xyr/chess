import pygame
import display_assistant
from display_board import adjustPromoSize, adjustWindowSize

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT = (235, 236, 208)
DARK = (115, 149, 82)
LIGHTSELECT = (202, 203, 179)
DARKSELECT = (99, 128, 70)
ULTRADARK = (38, 36, 33)
BACKGROUND = (48, 46, 43)
LIGHTGREY = (200, 200, 200)

def show_startup_screen(game, width, height, scale, tileSize, leftMargin, rightMargin, topMargin, bottomMargin):
    running = True
    titleFont = pygame.font.SysFont('Roboto', int(100 * scale))
    titleText = titleFont.render("CHESS", True, WHITE)
    titleRect = titleText.get_rect(center = (width // 2, height // 4))

    buttonFont = pygame.font.SysFont('Roboto', int(40 * scale))
    buttonText = buttonFont.render("Start Game", True, ULTRADARK)
    buttonRect = pygame.Rect(width // 2 - 150, height // 2, 300, 80)

    while running:
        game.fill(BACKGROUND)
        game.blit(titleText, titleRect)
        pygame.draw.rect(game, LIGHTGREY, buttonRect)
        game.blit(buttonText, buttonText.get_rect(center=buttonRect.center))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.VIDEORESIZE:
                adjustWindowSize(event.w, event.h)
                adjustPromoSize()
                display_assistant.displayAssistantConstructor(tileSize, topMargin, leftMargin, LIGHTSELECT, DARKSELECT)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if buttonRect.collidepoint(event.pos):
                    running = False