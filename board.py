from typing import List
import numpy as np
from piece import *

class Board:
    def __init__(self, width : int = 8, height : int = 8):

        if width <= 0 or width > 26:
            raise ValueError(f"width out of range: Please enter a value between 0-26, Value given: {width}")

        if height <= 0 or height > 9:
            raise ValueError(f"width out of range: Please enter a value between 0-9, Value given: {height}")

        self.width = width
        self.height = height
        self.flipped = False

        if self.width == 8 and self.height == 8:
            self.setupBoard()
        else:
            self.clearBoard()

    def __str__(self) -> str:
        board = ""

        pieces = self.pieces
        if self.flipped:
            pieces = np.flip(pieces)

        for rank in range(self.height):
            row = (str(self.height - rank) if self.flipped else str(rank + 1)) + "│" + ANSIColours.fgBrightBlack
            for file in range(self.width):
                row += ANSIColours.bgBlack if (rank + file) % 2 else ANSIColours.bgWhite # ANSI Background colours
                row += str(pieces[rank][file]) + ' '
                
            row += ANSIColours.reset + "\n" # Reset background colour
            board += row


        board += "─┼"
        for i in range(self.width):
            board += '──'

        board += '\n │'

        for file in range(self.width):
            board += chr(96 + (self.width - file if self.flipped else file + 1)) + ' '

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

        for i in range(8):
            for j in range(8):
                self.pieces[i][j].setPos(Pos(i + 1, j + 1))

    def getPiece(self, rank : int, file : int) -> Piece:
        if rank < 0 or rank >= self.width:
            raise ValueError(f"rank out of range: Please give a value between {0}-{self.width}. Value given: {rank}")

        if file < 0 or file >= self.width:
            raise ValueError(f"file out of range: Please give a value between {0}-{self.height}. Value given: {file}")

        return self.pieces[rank][file]

    def movePiece(self, srcPos : Pos, destPos : Pos) -> bool:
        if srcPos.rank < 0 or srcPos.rank >= self.width:
            raise ValueError(f"srcPos Rank out of range: Please give a value between {0}-{self.width}. Value given: {srcPos.rank}")

        if srcPos.file < 0 or srcPos.file >= self.height:
            raise ValueError(f"srcPos File out of range: Please give a value between {0}-{self.height}. Value given: {srcPos.file}")

        if destPos.rank < 0 or destPos.rank >= self.width:
            raise ValueError(f"destPos Rank out of range: Please give a value between {0}-{self.width}. Value given: {destPos.rank}")

        if destPos.file < 0 or destPos.file >= self.height:
            raise ValueError(f"destPos File out of range: Please give a value between {0}-{self.height}. Value given: {destPos.file}")

        # TODO: Implement actual legality checking. Currently just moves piece

        piece = self.pieces[srcPos.rank][srcPos.file]

        if piece.chessman == Chessman.EMPTY:
            return False

        self.pieces[srcPos.rank][srcPos.file] = Piece(Chessman.EMPTY, Colour.EMPTY, Pos(srcPos.rank + 1, srcPos.file + 1))
        self.pieces[destPos.rank][destPos.file] = piece
        piece.setPos(destPos)

        return True

    def flipBoard(self) -> None:
        self.flipped = not self.flipped

    # TODO: Fill these in
    def isFinished(self):
        # If no actions left (either white or black has won)
        return False

    def getPieces(self, playerColour : Colour) -> List[Piece]:

        pieces = []

        for rank in self.pieces:
            for piece in rank:
                if piece.colour == playerColour:
                    pieces.append(piece)

        return pieces

    def gameScore(self):
        # Heuristic value if game not done, or final game value if game is done
        return False

    def getActions(self, playerColour : Colour):
        # Return all possible actions from player
        actions = []
        return actions

    def childBoard(self, action):
        # Initialize and return new board with same state, but affected by input action
        return self