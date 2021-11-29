import enum

DEPTH = 4

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

class ActionType(enum.Enum):
    NO_ACTION = enum.auto()