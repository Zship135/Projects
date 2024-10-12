import pygame
from Pieces import LoadPieces


# INIT #
pygame.init()

# BOARD #
BOARD_WIDTH = 8
BOARD_HEIGHT = 8
TILE_WIDTH = 70
TILE_HEIGHT = 70

# COLORS #
black = (0, 0, 0)
white = (255, 255, 255)
background_color = (234,212,252)
light_tile = (186, 202, 68)
dark_tile = (118, 150, 86)

# SCREEEN INIT #
screen = pygame.display.set_mode([800, 700])
pygame.display.set_caption('Chess')
screen.fill(background_color)
running = True

# FUNCTIONS #
def DrawBoard():

    for i in range(1, BOARD_WIDTH + 1):
        for j in range(1, BOARD_HEIGHT + 1):
            if (i + j) % 2 != 0:
                tile_color = dark_tile
            else:
                tile_color = light_tile
            pygame.draw.rect(screen, tile_color, pygame.Rect(TILE_WIDTH * i, TILE_HEIGHT * j, TILE_WIDTH, TILE_HEIGHT))
def DrawPieces():
    for piece in LoadPieces():
        screen.blit(piece.image, (piece.x * TILE_WIDTH, piece.y * TILE_HEIGHT))

DrawBoard()
DrawPieces()

pygame.display.flip()

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            print(mouse_x, mouse_y)

            for piece in LoadPieces():
                if (piece.x * TILE_WIDTH <= mouse_x <= (piece.x + 1) * TILE_WIDTH and
                        piece.y * TILE_HEIGHT <= mouse_y <= (piece.y + 1) * TILE_HEIGHT):
                    selected_piece = piece
                    print(selected_piece.type)
                    break

        

        


