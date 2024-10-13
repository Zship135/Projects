import pygame
from Pieces import CreatePiece

# INIT #
pygame.init()

# BOARD #
BOARD_WIDTH = 8
BOARD_HEIGHT = 8
TILE_WIDTH = 70
TILE_HEIGHT = 70

pressing = False
selected_piece = None
offset_x, offset_y = 0, 0  # To track the offset when dragging

pieces = []
valid_moves = []

# COLORS #
background_color = (234, 212, 252)
light_tile = (186, 202, 68)
dark_tile = (118, 150, 86)
valid_move = (255, 255, 255, 128)

# SCREEN INIT #
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

def CreatePieces():
    pieces.append(CreatePiece("rook", "white", 1, 1, "res/rook-w.png"))
    pieces.append(CreatePiece("rook", "white", 8, 1, "res/rook-w.png"))
    pieces.append(CreatePiece("rook", "black", 1, 8, "res/rook-b.png"))
    pieces.append(CreatePiece("rook", "black", 8, 8, "res/rook-b.png"))

def DrawPieces():
    screen.fill(background_color)  # Clear the screen before drawing
    DrawBoard()  # Redraw the board
    for piece in pieces:
        screen.blit(piece.image, (piece.x * TILE_WIDTH, piece.y * TILE_HEIGHT))
    pygame.display.flip()  # Update the display

def CheckRookMoves(piece):
    
    if piece.type == "rook":

        stop = False
        # check right #
        for i in range(piece.x + 1, BOARD_WIDTH + 1):
            if i <= 8 and stop == False:
                valid_moves.append((i, piece.y))
            for j in pieces:
                if (j.x, j.y) == (i, piece.y):
                    valid_moves.remove((i, piece.y))
                    stop = True

        stop = False
        # check down #
        for i in range(piece.y + 1, BOARD_HEIGHT + 1):
            if i <= 8 and stop == False:
                valid_moves.append((piece.x, i))
            for j in pieces:
                if (j.x, j.y) == (piece.x, i):
                    valid_moves.remove((piece.x, i))
                    stop = True

        stop = False
        # check left #
        for i in range(piece.x - 1,  8 - BOARD_WIDTH, -1):
            if i <= piece.x and stop == False:
                valid_moves.append((i, piece.y))
            for j in pieces:
                if (j.x, j.y) == (i, piece.y):
                    valid_moves.remove((i, piece.y))
                    stop = True
            

        stop = False
        # check up #
        for i in range(piece.y - 1, 8 - BOARD_HEIGHT, -1):
            if i <= piece.y and stop == False:
                valid_moves.append((piece.x, i))
            for j in pieces:
                if (j.x, j.y) == (piece.x, i):
                    valid_moves.remove((piece.x, i))
                    stop = True
        
    

def CheckValidMoves(piece):
    CheckRookMoves(piece)
    
            
            



# INITIAL DRAWING
DrawBoard()
CreatePieces()
DrawPieces()
pygame.display.flip()

# MAIN LOOP
while running:
    # allow to close window #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and selected_piece:
            mouse_x, mouse_y = event.pos
            mouse_x = mouse_x // TILE_WIDTH
            mouse_y = mouse_y // TILE_HEIGHT
            for moves in valid_moves:
                if (mouse_x, mouse_y) == moves:
                    selected_piece.x = mouse_x
                    selected_piece.y = mouse_y
                    selected_piece = None
                    valid_moves = []
                    DrawBoard()
                    DrawPieces()

            valid_moves = []
            DrawPieces()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            mouse_x = mouse_x // TILE_WIDTH
            mouse_y = mouse_y // TILE_HEIGHT
            valid_moves = []
            DrawPieces()
            
            for piece in pieces:
                if piece.x == mouse_x and piece.y == mouse_y:
                    selected_piece = piece
                    break
                else:
                    selected_piece = None
                    valid_moves = []
                    DrawBoard()
                    DrawPieces()
                    pygame.display.flip()

            if selected_piece is not None:
                CheckValidMoves(selected_piece)
                for (x,y) in valid_moves:
                    pygame.draw.rect(screen, valid_move, pygame.Rect(TILE_WIDTH * x, TILE_HEIGHT * y, TILE_WIDTH, TILE_HEIGHT))
                    pygame.display.flip()

            pressing = True

        if event.type == pygame.MOUSEBUTTONUP:
            pressing = False

pygame.quit()

        



        


