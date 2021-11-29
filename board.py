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
        return board[:-1] # Remove trailing newline

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

    def getPiece(self, rank : int, file : int) -> Piece:
        if rank < 0 or rank >= self.width:
            raise ValueError("rank out of range: Please give a value between {0}-{self.width}. Value given: {rank}")

        if file < 0 or file >= self.width:
            raise ValueError("file out of range: Please give a value between {0}-{self.height}. Value given: {file}")

        return self.pieces[rank][file]

    def movePiece(self, srcRank : int, srcFile : int, destRank : int, destFile : int) -> None:
        if srcRank < 0 or srcRank >= self.width:
            raise ValueError("srcRank out of range: Please give a value between {0}-{self.width}. Value given: {srcRank}")

        if srcFile < 0 or srcFile >= self.height:
            raise ValueError("srcFile out of range: Please give a value between {0}-{self.height}. Value given: {srcFile}")

        if destRank < 0 or destRank >= self.width:
            raise ValueError("destRank out of range: Please give a value between {0}-{self.width}. Value given: {destRank}")

        if destFile < 0 or destFile >= self.height:
            raise ValueError("destFile out of range: Please give a value between {0}-{self.height}. Value given: {destFile}")

        p = self.pieces[srcRank][srcFile]
        self.pieces[srcRank][srcFile] = Piece()
        self.pieces[destRank][destFile] = p

    # TODO: Fill these in
    def isFinished(self):
        # If no actions left (either white or black has won)
        return False

    def gameScore(self):
        # Heuristic value if game not done, or final game value if game is done
        return False

    def getActions(self, playerColour):
        # Return all possible actions from player
        actions = []
        return actions

    def childBoard(self, action):
        # Initialize and return new board with same state, but affected by input action
        return self