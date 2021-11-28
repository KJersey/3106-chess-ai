from piece import *

class Board:
    def __init__(self, width : int = 8, height : int = 8):
        self.width = width
        self.height = height

        if self.width == 8 and self.height == 8:
            self.setupBoard()
        else:
            self.clearBoard()
        

    def __str__(self) -> str:
        board = ""
        for i in range(self.height):
            row = ""
            for j in range(self.width):
                row += str(self.pieces[i][j])
            row += '\n'
            board += row
        return board

    def clearBoard(self) -> None:
        self.pieces = []
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                row.append(Piece())
            self.pieces.append(row)

    def setupBoard(self) -> None:
        if not self.width == 8 or not self.height == 8:
            raise ValueError(f"Can only setup with an 8x8 board. Current board is: {self.width}x{self.height}")

        self.pieces = [
            [Piece(Chessman.ROOK, Colour.BLACK), Piece(Chessman.KNIGHT, Colour.BLACK), Piece(Chessman.BISHOP, Colour.BLACK), Piece(Chessman.QUEEN, Colour.BLACK), Piece(Chessman.KING, Colour.BLACK), Piece(Chessman.BISHOP, Colour.BLACK), Piece(Chessman.KNIGHT, Colour.BLACK), Piece(Chessman.ROOK, Colour.BLACK)],
            [Piece(Chessman.PAWN, Colour.BLACK), Piece(Chessman.PAWN,   Colour.BLACK), Piece(Chessman.PAWN,   Colour.BLACK), Piece(Chessman.PAWN,  Colour.BLACK), Piece(Chessman.PAWN, Colour.BLACK), Piece(Chessman.PAWN,   Colour.BLACK), Piece(Chessman.PAWN,   Colour.BLACK), Piece(Chessman.PAWN, Colour.BLACK)],
            [Piece(Chessman.EMPTY),              Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),               Piece(Chessman.EMPTY),              Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY)],
            [Piece(Chessman.EMPTY),              Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),               Piece(Chessman.EMPTY),              Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY)],
            [Piece(Chessman.EMPTY),              Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),               Piece(Chessman.EMPTY),              Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY)],
            [Piece(Chessman.EMPTY),              Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),               Piece(Chessman.EMPTY),              Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY)],
            [Piece(Chessman.PAWN, Colour.WHITE), Piece(Chessman.PAWN,   Colour.WHITE), Piece(Chessman.PAWN,   Colour.WHITE), Piece(Chessman.PAWN,  Colour.WHITE), Piece(Chessman.PAWN, Colour.WHITE), Piece(Chessman.PAWN,   Colour.WHITE), Piece(Chessman.PAWN,   Colour.WHITE), Piece(Chessman.PAWN, Colour.WHITE)],
            [Piece(Chessman.ROOK, Colour.WHITE), Piece(Chessman.KNIGHT, Colour.WHITE), Piece(Chessman.BISHOP, Colour.WHITE), Piece(Chessman.QUEEN, Colour.WHITE), Piece(Chessman.KING, Colour.WHITE), Piece(Chessman.BISHOP, Colour.WHITE), Piece(Chessman.KNIGHT, Colour.WHITE), Piece(Chessman.ROOK, Colour.WHITE)]
        ]


    def getPiece(self, row : int, col : int) -> Piece:
        return self.pieces[row][col]