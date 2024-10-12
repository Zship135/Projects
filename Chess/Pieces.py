import pygame

class Piece:
    def __init__(self, type, color, x, y, image_path):
        self.type = type  
        self.color = color  
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path).convert_alpha() 
        self.image = pygame.transform.scale(self.image, (70, 70)) 

def CreatePiece(type, color, x, y, image_path):
    return Piece(type, color, x, y, image_path)

def LoadPieces():
    pieces = []
    pieces.append(CreatePiece("king", "black", 4, 8, "res/king-b.png"))
    pieces.append(CreatePiece("queen", "black", 5, 8, "res/queen-b.png"))
    pieces.append(CreatePiece("rook", "black", 1, 8, "res/rook-b.png"))
    pieces.append(CreatePiece("rook", "black", 8, 8, "res/rook-b.png"))
    pieces.append(CreatePiece("knight", "black", 2, 8, "res/knight-b.png"))
    pieces.append(CreatePiece("knight", "black", 7, 8, "res/knight-b.png"))
    pieces.append(CreatePiece("bishop", "black", 3, 8, "res/bishop-b.png"))
    pieces.append(CreatePiece("bishop", "black", 6, 8, "res/bishop-b.png"))
    pieces.append(CreatePiece("pawn", "black", 1, 7, "res/pawn-b.png"))
    pieces.append(CreatePiece("pawn", "black", 2, 7, "res/pawn-b.png"))
    pieces.append(CreatePiece("pawn", "black", 3, 7, "res/pawn-b.png"))
    pieces.append(CreatePiece("pawn", "black", 4, 7, "res/pawn-b.png"))
    pieces.append(CreatePiece("pawn", "black", 5, 7, "res/pawn-b.png"))
    pieces.append(CreatePiece("pawn", "black", 6, 7, "res/pawn-b.png"))
    pieces.append(CreatePiece("pawn", "black", 7, 7, "res/pawn-b.png"))
    pieces.append(CreatePiece("pawn", "black", 8, 7, "res/pawn-b.png"))

    pieces.append(CreatePiece("king", "white", 4, 1, "res/king-w.png"))
    pieces.append(CreatePiece("queen", "white", 5, 1, "res/queen-w.png"))
    pieces.append(CreatePiece("rook", "white", 1, 1, "res/rook-w.png"))
    pieces.append(CreatePiece("rook", "white", 8, 1, "res/rook-w.png"))
    pieces.append(CreatePiece("knight", "white", 2, 1, "res/knight-w.png"))
    pieces.append(CreatePiece("knight", "white", 7, 1, "res/knight-w.png"))
    pieces.append(CreatePiece("bishop", "white", 3, 1, "res/bishop-w.png"))
    pieces.append(CreatePiece("bishop", "white", 6, 1, "res/bishop-w.png"))
    pieces.append(CreatePiece("pawn", "white", 1, 2, "res/pawn-w.png"))
    pieces.append(CreatePiece("pawn", "white", 2, 2, "res/pawn-w.png"))
    pieces.append(CreatePiece("pawn", "white", 3, 2, "res/pawn-w.png"))
    pieces.append(CreatePiece("pawn", "white", 4, 2, "res/pawn-w.png"))
    pieces.append(CreatePiece("pawn", "white", 5, 2, "res/pawn-w.png"))
    pieces.append(CreatePiece("pawn", "white", 6, 2, "res/pawn-w.png"))
    pieces.append(CreatePiece("pawn", "white", 7, 2, "res/pawn-w.png"))
    pieces.append(CreatePiece("pawn", "white", 8, 2, "res/pawn-w.png"))

    

    return pieces


   