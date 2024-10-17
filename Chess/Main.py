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
    pieces.append(CreatePiece("rook", "white", 1, 1, "res/rook-b.png"))
    pieces.append(CreatePiece("rook", "white", 8, 1, "res/rook-b.png"))
    pieces.append(CreatePiece("rook", "black", 1, 8, "res/rook-w.png"))
    pieces.append(CreatePiece("rook", "black", 8, 8, "res/rook-w.png"))
    pieces.append(CreatePiece("knight", "white", 2, 1, "res/knight-b.png"))
    pieces.append(CreatePiece("knight", "white", 7, 1, "res/knight-b.png"))
    pieces.append(CreatePiece("knight", "black", 2, 8, "res/knight-w.png"))
    pieces.append(CreatePiece("knight", "black", 7, 8, "res/knight-w.png"))
    pieces.append(CreatePiece("bishop", "white", 3, 1, "res/bishop-b.png"))
    pieces.append(CreatePiece("bishop", "white", 6, 1, "res/bishop-b.png"))
    pieces.append(CreatePiece("bishop", "black", 3, 8, "res/bishop-w.png"))
    pieces.append(CreatePiece("bishop", "black", 6, 8, "res/bishop-w.png"))
    pieces.append(CreatePiece("queen", "white", 4, 1, "res/queen-b.png"))
    pieces.append(CreatePiece("queen", "black", 4, 8, "res/queen-w.png"))
    pieces.append(CreatePiece("king", "white", 5, 1, "res/king-b.png"))
    pieces.append(CreatePiece("king", "black", 5, 8, "res/king-w.png"))
    pieces.append(CreatePiece("pawn", "white", 1, 2, "res/pawn-b.png"))
    pieces.append(CreatePiece("pawn", "white", 2, 2, "res/pawn-b.png"))
    pieces.append(CreatePiece("pawn", "white", 3, 2, "res/pawn-b.png"))
    pieces.append(CreatePiece("pawn", "white", 4, 2, "res/pawn-b.png"))
    pieces.append(CreatePiece("pawn", "white", 5, 2, "res/pawn-b.png"))
    pieces.append(CreatePiece("pawn", "white", 6, 2, "res/pawn-b.png"))
    pieces.append(CreatePiece("pawn", "white", 7, 2, "res/pawn-b.png"))
    pieces.append(CreatePiece("pawn", "white", 8, 2, "res/pawn-b.png"))
    pieces.append(CreatePiece("pawn", "black", 1, 7, "res/pawn-w.png"))
    pieces.append(CreatePiece("pawn", "black", 2, 7, "res/pawn-w.png"))
    pieces.append(CreatePiece("pawn", "black", 3, 7, "res/pawn-w.png"))
    pieces.append(CreatePiece("pawn", "black", 4, 7, "res/pawn-w.png"))
    pieces.append(CreatePiece("pawn", "black", 5, 7, "res/pawn-w.png"))
    pieces.append(CreatePiece("pawn", "black", 6, 7, "res/pawn-w.png"))
    pieces.append(CreatePiece("pawn", "black", 7, 7, "res/pawn-w.png"))
    pieces.append(CreatePiece("pawn", "black", 8, 7, "res/pawn-w.png"))

def DrawPieces():
    screen.fill(background_color)  # Clear the screen before drawing
    DrawBoard()  # Redraw the board
    for piece in pieces:
        screen.blit(piece.image, (piece.x * TILE_WIDTH, piece.y * TILE_HEIGHT))
    pygame.display.flip()  # Update the display

def CheckRookMoves(piece):
    if piece.type == "rook":
        valid_rook_moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # Straight line directions
        for move in valid_rook_moves:
            dx, dy = move
            x, y = piece.x, piece.y

            
            while True:
                x += dx
                y += dy

                if not (1 <= x <= 8 and 1 <= y <= 8):
                    break

                occupied_by_friendly = False
                occupied_by_enemy = False
                for other_piece in pieces:
                    if other_piece.x == x and other_piece.y == y:
                        if other_piece.color == piece.color:
                            occupied_by_friendly = True
                        else:
                            occupied_by_enemy = True
                        break  

                if occupied_by_friendly:
                    break

                if occupied_by_enemy:
                    valid_moves.append((x, y))
                    break

                valid_moves.append((x, y))
        
def CheckBishopMoves(piece):
    if piece.type == "bishop":
        valid_bishop_moves = [(1, 1), (-1, -1), (1, -1), (-1, 1)]  # Diagonal directions
        for move in valid_bishop_moves:
            dx, dy = move
            x, y = piece.x, piece.y

            
            while True:
                x += dx
                y += dy

                if not (1 <= x <= 8 and 1 <= y <= 8):
                    break

                occupied_by_friendly = False
                occupied_by_enemy = False
                for other_piece in pieces:
                    if other_piece.x == x and other_piece.y == y:
                        if other_piece.color == piece.color:
                            occupied_by_friendly = True
                        else:
                            occupied_by_enemy = True
                        break  

                if occupied_by_friendly:
                    break

                if occupied_by_enemy:
                    valid_moves.append((x, y))
                    break

                valid_moves.append((x, y))
    
def CheckKnightMoves(piece):
    if piece.type == "knight":
        valid_knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        for move in valid_knight_moves:
            dx, dy = move
            x, y = piece.x + dx, piece.y + dy

            if not (1 <= x <= 8 and 1 <= y <= 8):
                continue  # Skip invalid moves but continue the loop, don't break

            occupied_by_friendly = False
            for other_piece in pieces:
                if other_piece.x == x and other_piece.y == y:
                    if other_piece.color == piece.color:
                        occupied_by_friendly = True
                    break  

            if not occupied_by_friendly:
                valid_moves.append((x, y))  # Add the valid move

def CheckQueenMoves(piece):
    if piece.type == "queen":
        # Queen's movement is a combination of rook and bishop
        valid_queen_moves = [(0, 1), (1, 0), (-1, 0), (0, -1),  # Rook-like moves
                             (1, 1), (1, -1), (-1, 1), (-1, -1)]  # Bishop-like moves
        for move in valid_queen_moves:
            dx, dy = move
            x, y = piece.x, piece.y

            while True:
                x += dx
                y += dy

                if not (1 <= x <= 8 and 1 <= y <= 8):
                    break  # Stop if move goes out of bounds

                occupied_by_friendly = False
                occupied_by_enemy = False

                # Check if the position is occupied by another piece
                for other_piece in pieces:
                    if other_piece.x == x and other_piece.y == y:
                        if other_piece.color == piece.color:
                            occupied_by_friendly = True
                        else:
                            occupied_by_enemy = True
                        break  # Stop checking pieces after a collision

                if occupied_by_friendly:
                    break  # Can't move further in this direction

                valid_moves.append((x, y))  # Valid move if no friendly piece in the way

                if occupied_by_enemy:
                    break  # Can capture enemy but can't move further beyond

def CheckKingMoves(piece):
    if piece.type == "king":
        # King moves one square in any direction
        valid_king_moves = [(0, 1), (1, 0), (-1, 0), (0, -1),  # Horizontal/vertical moves
                            (1, 1), (1, -1), (-1, 1), (-1, -1)]  # Diagonal moves
        for move in valid_king_moves:
            dx, dy = move
            x, y = piece.x + dx, piece.y + dy

            # Ensure the move is within bounds
            if not (1 <= x <= 8 and 1 <= y <= 8):
                continue  # Skip if the move is out of bounds

            occupied_by_friendly = False
            for other_piece in pieces:
                if other_piece.x == x and other_piece.y == y:
                    if other_piece.color == piece.color:
                        occupied_by_friendly = True  # Cannot move onto a square occupied by a friendly piece
                    break  # Stop checking once a piece is found on this square

            if not occupied_by_friendly:
                valid_moves.append((x, y))  # Add valid move if not occupied by a friendly piece

def CheckPawnMoves(piece):
    if piece.type == "pawn":
        direction = 1 if piece.color == "white" else -1  # White pawns move up, black pawns move down
        
        # Move forward one square
        if is_empty(piece.x, piece.y + direction):
            valid_moves.append((piece.x, piece.y + direction))
        
            # Move forward two squares on the first move
            if (piece.color == "white" and piece.y == 2) or (piece.color == "black" and piece.y == 7):
                if is_empty(piece.x, piece.y + 2 * direction):
                    valid_moves.append((piece.x, piece.y + 2 * direction))

        # Capture diagonally
        for dx in [-1, 1]:
            new_x = piece.x + dx
            new_y = piece.y + direction
            if 1 <= new_x <= 8 and 1 <= new_y <= 8:
                for other_piece in pieces:
                    if other_piece.x == new_x and other_piece.y == new_y and other_piece.color != piece.color:
                        valid_moves.append((new_x, new_y))
                        break

def is_empty(x, y):
    for piece in pieces:
        if piece.x == x and piece.y == y:
            return False
    return True

def CheckTake(piece):
    for other_piece in pieces:
        if piece.x == other_piece.x and piece.y == other_piece.y and other_piece.color != piece.color:
            pieces.remove(other_piece)
            DrawBoard()
            DrawPieces()


def CheckValidMoves(piece):
    valid_moves.clear()  # Clear the previous moves
    if piece.type == "rook":
        CheckRookMoves(piece)
    if piece.type == "bishop":
        CheckBishopMoves(piece)
    if piece.type == "knight":
        CheckKnightMoves(piece)
    if piece.type == "queen":
        CheckQueenMoves(piece)
    if piece.type == "king":
        CheckKingMoves(piece)
    if piece.type == "pawn":
        CheckPawnMoves(piece)

# INITIAL DRAWING
DrawBoard()
CreatePieces()
DrawPieces()
pygame.display.flip()

# MAIN LOOP
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            mouse_x = mouse_x // TILE_WIDTH
            mouse_y = mouse_y // TILE_HEIGHT

            for move in valid_moves:
                if mouse_x == move[0] and mouse_y == move[1]:
                    selected_piece.x = mouse_x
                    selected_piece.y = mouse_y
                    CheckTake(selected_piece)
                    DrawBoard()
                    DrawPieces()
                    pygame.display.flip()
            
            for piece in pieces:
                if mouse_x == piece.x and mouse_y == piece.y:
                    selected_piece = piece
                    print(selected_piece.type)
                    CheckValidMoves(piece)
                    DrawBoard()
                    DrawPieces()
                    for (x,y) in valid_moves:
                        print(x,y)
                        pygame.draw.rect(screen, valid_move, pygame.Rect(TILE_WIDTH * x, TILE_HEIGHT * y, TILE_WIDTH, TILE_HEIGHT))
                        pygame.display.flip() 
                    break
                else:
                    selected_piece = None
                    valid_moves = []
                    DrawBoard()
                    DrawPieces()
                    print(selected_piece)

            

        if event.type == pygame.MOUSEBUTTONUP:
            pressing = False

pygame.quit()
