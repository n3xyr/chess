import board
import piecesImages
import time
import datetime
import pygame
import sys

# Initialize Pygame
pygame.init()

# Define window size
WIDTH, HEIGHT = 800, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# Define colors
WHITE = (255, 255, 255)
LIGHT = (235, 236, 208)
DARK = (73, 95, 52)
ULTRADARK = (38, 36, 33)
BACKGROUND = (48, 46, 43)

# Define tiles size
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

def draw_board(win):
    """Draw board"""
    win.fill(BACKGROUND)
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 1:
                pygame.draw.rect(win, DARK, (col * SQUARE_SIZE, 100 + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(win, LIGHT, (col * SQUARE_SIZE, 100 + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)  # 60 FPS cap

        if len(moveList) == 0:
            timer = time.time()
            lastTime = timer
        else:
            if timer - lastTime >= 1:
                lastTime = timer

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_board(WIN)
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
