import board
import piecesImages
import time
import datetime
import pygame
import sys

# Initialize Pygame
pygame.init()
bp = pygame.transform.scale(pygame.image.load("piecesImages/bp.png"), (100, 100))
bb = pygame.transform.scale(pygame.image.load("piecesImages/bb.png"), (100, 100))
bk = pygame.transform.scale(pygame.image.load("piecesImages/bk.png"), (100, 100))
bn = pygame.transform.scale(pygame.image.load("piecesImages/bn.png"), (100, 100))
bq = pygame.transform.scale(pygame.image.load("piecesImages/bq.png"), (100, 100))
br = pygame.transform.scale(pygame.image.load("piecesImages/br.png"), (100, 100))
wp = pygame.transform.scale(pygame.image.load("piecesImages/wp.png"), (100, 100))
wb = pygame.transform.scale(pygame.image.load("piecesImages/wb.png"), (100, 100))
wk = pygame.transform.scale(pygame.image.load("piecesImages/wk.png"), (100, 100))
wn = pygame.transform.scale(pygame.image.load("piecesImages/wn.png"), (100, 100))
wq = pygame.transform.scale(pygame.image.load("piecesImages/wq.png"), (100, 100))
wr = pygame.transform.scale(pygame.image.load("piecesImages/wr.png"), (100, 100))

# Define window size
HEIGHTMARGIN = 100
WIDTH, HEIGHT = 800, 800 + 2 * HEIGHTMARGIN
GAME = pygame.display.set_mode((WIDTH, HEIGHT))
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

def draw_board(game):
    """Draw board"""
    game.fill(BACKGROUND)
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 1:
                pygame.draw.rect(game, DARK, (col * SQUARE_SIZE, HEIGHTMARGIN + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(game, LIGHT, (col * SQUARE_SIZE, HEIGHTMARGIN + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            if row == 0:        # black pieces first rank
                if col == 0 or col == 7:
                    game.blit(br, (col * SQUARE_SIZE, HEIGHTMARGIN + row * SQUARE_SIZE))    # black rook
                if col == 1 or col == 6:
                    game.blit(bn, (col * SQUARE_SIZE, HEIGHTMARGIN + row * SQUARE_SIZE))    # black knight
                if col == 2 or col == 5:
                    game.blit(bb, (col * SQUARE_SIZE, HEIGHTMARGIN + row * SQUARE_SIZE))    # black bishop
                if col == 3:
                    game.blit(bk, (col * SQUARE_SIZE, HEIGHTMARGIN + row * SQUARE_SIZE))    # black king
                if col == 4:
                    game.blit(bq, (col * SQUARE_SIZE, HEIGHTMARGIN + row * SQUARE_SIZE))    # black queen
            
            if row == 1:        # black pieces second row
                game.blit(bp, (col * SQUARE_SIZE, HEIGHTMARGIN + row * SQUARE_SIZE))        # black pawn

            if row == 7:        # white pieces first row
                if col == 0 or col == 7:
                    game.blit(wr, (col * SQUARE_SIZE, HEIGHTMARGIN + row * SQUARE_SIZE))    # white rook
                if col == 1 or col == 6:
                    game.blit(wn, (col * SQUARE_SIZE, HEIGHTMARGIN + row * SQUARE_SIZE))    # white knight
                if col == 2 or col == 5:
                    game.blit(wb, (col * SQUARE_SIZE, HEIGHTMARGIN + row * SQUARE_SIZE))    # white bishop
                if col == 3:
                    game.blit(wk, (col * SQUARE_SIZE, HEIGHTMARGIN + row * SQUARE_SIZE))    # white king
                if col == 4:
                    game.blit(wq, (col * SQUARE_SIZE, HEIGHTMARGIN + row * SQUARE_SIZE))    # white queen
            
            if row == 6:        # white pieces second row
                game.blit(wp, (col * SQUARE_SIZE, HEIGHTMARGIN + row * SQUARE_SIZE))        # white pawn


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

        draw_board(GAME)
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
