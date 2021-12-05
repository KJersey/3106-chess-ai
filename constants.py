import enum

DEPTH = 4

# Enables UNICODE Chess Characters
UNICODE = True  

# Enables ANSI Coloured Background
ANSI = True     

class Colour(enum.Enum):
    EMPTY = enum.auto()
    WHITE = enum.auto()
    BLACK = enum.auto()

class Chessman(enum.Enum):
    EMPTY   = enum.auto()
    PAWN    = enum.auto()
    ROOK    = enum.auto()
    KNIGHT  = enum.auto()
    BISHOP  = enum.auto()
    KING    = enum.auto()
    QUEEN   = enum.auto()

ChessmanValue = {
    Chessman.EMPTY: 0,
    Chessman.PAWN: 1,
    Chessman.KNIGHT: 3,
    Chessman.BISHOP: 3,
    Chessman.ROOK: 5,
    Chessman.QUEEN: 9,
    Chessman.KING: 200
}

class ANSIColours:
    if ANSI:
        reset = "\033[0m"

        # Black
        fgBlack = "\033[30m"
        fgBrightBlack = "\033[30;1m"
        bgBlack = "\033[40m"
        bgBrightBlack = "\033[40;1m"

        # Red
        fgRed = "\033[31m"
        fgBrightRed = "\033[31;1m"
        bgRed = "\033[41m"
        bgBrightRed = "\033[41;1m"

        # Green
        fgGreen = "\033[32m"
        fgBrightGreen = "\033[32;1m"
        bgGreen = "\033[42m"
        bgBrightGreen = "\033[42;1m"

        # Yellow
        fgYellow = "\033[33m"
        fgBrightYellow = "\033[33;1m"
        bgYellow = "\033[43m"
        bgBrightYellow = "\033[43;1m"

        # Blue
        fgBlue = "\033[34m"
        fgBrightBlue = "\033[34;1m"
        bgBlue = "\033[44m"
        bgBrightBlue = "\033[44;1m"

        # Magenta
        fgMagenta = "\033[35m"
        fgBrightMagenta = "\033[35;1m"
        bgMagenta = "\033[45m"
        bgBrightMagenta = "\033[45;1m"

        # Cyan
        fgCyan = "\033[36m"
        fgBrightCyan = "\033[36;1m"
        bgCyan = "\033[46m"
        bgBrightCyan = "\033[46;1m"

        # White
        fgWhite = "\033[37m"
        fgBrightWhite = "\033[37;1m"
        bgWhite = "\033[47m"
        bgBrightWhite = "\033[47;1m"

    else:
        reset = ""

        # Black
        fgBlack = ""
        fgBrightBlack = ""
        bgBlack = ""
        bgBrightBlack = ""

        # Red
        fgRed = ""
        fgBrightRed = ""
        bgRed = ""
        bgBrightRed = ""

        # Green
        fgGreen = ""
        fgBrightGreen = ""
        bgGreen = ""
        bgBrightGreen = ""

        # Yellow
        fgYellow = ""
        fgBrightYellow = ""
        bgYellow = ""
        bgBrightYellow = ""

        # Blue
        fgBlue = ""
        fgBrightBlue = ""
        bgBlue = ""
        bgBrightBlue = ""

        # Magenta
        fgMagenta = ""
        fgBrightMagenta = ""
        bgMagenta = ""
        bgBrightMagenta = ""

        # Cyan
        fgCyan = ""
        fgBrightCyan = ""
        bgCyan = ""
        bgBrightCyan = ""

        # White
        fgWhite = ""
        fgBrightWhite = ""
        bgWhite = ""
        bgBrightWhite = ""

class CastleRights:
    def __init__(self, K : bool = True, Q : bool = True, k : bool = True, q : bool = True):
        self.K = K
        self.Q = Q
        self.k = k
        self.q = q

class Pos():
    def __init__(self, *args):
        if len(args) == 0:
            self.rank = -1
            self.file = -1

        elif len(args) == 1:
            if not len(args[0]) == 2:
                raise ValueError(f"Invalid value for position, expected a number and letter, given {args[0]}")

            self.file = ord(args[0][0]) - 97
            self.rank = int(args[0][1]) - 1

        elif len(args) == 2:
            rank, file = args
            self.rank = rank - 1

            if isinstance(file, str):
                self.file = ord(file) - 97
            elif isinstance(file, int):
                self.file = file - 1
            else:
                pass
        else:
            pass

    def __str__(self) -> str:
        return chr(self.file + 97) + str(self.rank + 1)

    def __repr__(self) -> str:
        return self.__str__()

class ActionType(enum.Enum):
    NO_ACTION   = enum.auto()
    MOVE        = enum.auto()
    CASTLE      = enum.auto()
    PROMOTION   = enum.auto()