from constants import *

class Piece:
    def __init__(self, chessman : Chessman = Chessman.EMPTY, colour : Colour = Colour.EMPTY, pos : Pos = Pos()):
        self.chessman = chessman
        self.colour = colour

        self.pos = pos

    def __str__(self) -> str:
        if self.chessman == Chessman.EMPTY:
            return ' '

        if not UNICODE:
            if self.chessman == Chessman.PAWN:
                c =  'p'
            elif self.chessman == Chessman.BISHOP:
                c =  'b'
            elif self.chessman == Chessman.KNIGHT:
                c =  'n'
            elif self.chessman == Chessman.ROOK:
                c =  'r'
            elif self.chessman == Chessman.QUEEN:
                c =  'q'
            elif self.chessman == Chessman.KING:
                c =  'k'
            else:
                raise ValueError("Piece not an expected value!")

            if self.colour == Colour.WHITE:
                c = c.upper()

            return c

        if self.colour == Colour.WHITE:
            if self.chessman == Chessman.PAWN:
                return "♙"
            elif self.chessman == Chessman.BISHOP:
                return "♗"
            elif self.chessman == Chessman.KNIGHT:
                return "♘"
            elif self.chessman == Chessman.ROOK:
                return "♖"
            elif self.chessman == Chessman.QUEEN:
                return "♕"
            elif self.chessman == Chessman.KING:
                return "♔"
            else:
                raise ValueError("Piece not an expected value!")
        elif self.colour == Colour.BLACK:
            if self.chessman == Chessman.PAWN:
                return "♟︎"
            elif self.chessman == Chessman.BISHOP:
                return "♝"
            elif self.chessman == Chessman.KNIGHT:
                return "♞"
            elif self.chessman == Chessman.ROOK:
                return "♜"
            elif self.chessman == Chessman.QUEEN:
                return "♛"
            elif self.chessman == Chessman.KING:
                return "♚"
            else:
                raise ValueError("Piece not an expected value!")
        else:
            raise ValueError("Colour not an expected value!")

    def setPos(self, pos : Pos) -> None:
        self.pos = pos

    def getImagePath(self) -> str:
        if self.chessman == Chessman.EMPTY:
            return ""
        elif self.chessman == Chessman.PAWN:
            fp = "Pawn.png"
        elif self.chessman == Chessman.BISHOP:
            fp = "Bishop.png"
        elif self.chessman == Chessman.KNIGHT:
            fp = "Knight.png"
        elif self.chessman == Chessman.ROOK:
            fp = "Rook.png"
        elif self.chessman == Chessman.QUEEN:
            fp = "Queen.png"
        elif self.chessman == Chessman.KING:
            fp = "King.png"
        else:
            raise ValueError("Piece not an expected value!")

        if self.colour == Colour.BLACK:
            fp = "Black_" + fp
        elif self.colour == Colour.WHITE:
            fp = "White_" + fp
        else:
            raise ValueError("Colour not an expected value!")

        return fp