import enum

class Colour(enum.Enum):
    WHITE = 0
    BLACK = 1

class Chessman(enum.Enum):
    EMPTY   = enum.auto()
    PAWN    = enum.auto()
    ROOK    = enum.auto()
    KNIGHT  = enum.auto()
    BISHOP  = enum.auto()
    KING    = enum.auto()
    QUEEN   = enum.auto()

class Piece:
    def __init__(self, chessman : Chessman = Chessman.EMPTY, colour : Colour = Colour.WHITE):
        self.chessman = chessman
        self.colour = colour

    def __str__(self) -> str:
        if self.chessman == Chessman.EMPTY:
            return " "
        elif self.chessman == Chessman.PAWN:
            c = "P"
        elif self.chessman == Chessman.BISHOP:
            c = "B"
        elif self.chessman == Chessman.KNIGHT:
            c = "N"
        elif self.chessman == Chessman.ROOK:
            c = "R"
        elif self.chessman == Chessman.QUEEN:
            c = "Q"
        elif self.chessman == Chessman.KING:
            c = "K"
        else:
            raise ValueError("Piece not an expected value!")

        if self.colour == Colour.WHITE:
            return c.upper()
        elif self.colour == Colour.BLACK:
            return c.lower()
        else:
            raise ValueError("Colour not an expected value!")

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