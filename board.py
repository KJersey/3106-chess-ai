from typing import List
import numpy as np

from piece import *
from action import *

class Board:
    def __init__(self, width : int = 8, height : int = 8, playerColour : Colour = Colour.BLACK):

        if width <= 0 or width > 26:
            raise ValueError(f"width out of range: Please enter a value between 0-26, Value given: {width}")

        if height <= 0 or height > 9:
            raise ValueError(f"width out of range: Please enter a value between 0-9, Value given: {height}")

        self.width = width
        self.height = height
        self.playerColour = playerColour
        self.flipped = False

        self.lastMoved = None # Used for en passant

        if self.width == 8 and self.height == 8:
            self.setupBoard()
        else:
            self.clearBoard()

    def __str__(self) -> str:
        s = ""

        pieces = self.pieces
        if self.flipped:
            pieces = np.flip(pieces)

        board = ""

        for rank in range(self.height):
            row = (str(self.height - rank) if self.flipped else str(rank + 1)) + "│" + ANSIColours.fgBrightBlack
            for file in range(self.width):
                row += ANSIColours.bgWhite if (rank + file) % 2 else ANSIColours.bgBlack # ANSI Background colours
                row += str(pieces[rank][file]) + ' '
                
            row += ANSIColours.reset + "\n" # Reset background colour
            board = row + board

        s += board

        s += "─┼"
        for _ in range(self.width):
            s += '──'

        s += '\n │'

        for file in range(self.width):
            s += chr(96 + (self.width - file if self.flipped else file + 1)) + ' '

        return s
    
    def getPlayerColour(self):
        return self.playerColour

    def getAiColour(self):
        if self.playerColour == Colour.WHITE:
            return Colour.BLACK
        else:
            return Colour.WHITE

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
            [Piece(Chessman.ROOK,   Colour.WHITE), Piece(Chessman.KNIGHT, Colour.WHITE), Piece(Chessman.BISHOP, Colour.WHITE), Piece(Chessman.QUEEN,  Colour.WHITE), Piece(Chessman.KING,   Colour.WHITE), Piece(Chessman.BISHOP, Colour.WHITE), Piece(Chessman.KNIGHT, Colour.WHITE), Piece(Chessman.ROOK, Colour.WHITE)],
            [Piece(Chessman.PAWN,   Colour.WHITE), Piece(Chessman.PAWN,   Colour.WHITE), Piece(Chessman.PAWN,   Colour.WHITE), Piece(Chessman.PAWN,   Colour.WHITE), Piece(Chessman.PAWN,   Colour.WHITE), Piece(Chessman.PAWN,   Colour.WHITE), Piece(Chessman.PAWN,   Colour.WHITE), Piece(Chessman.PAWN, Colour.WHITE)],
            [Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY)]             ,
            [Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY)]             ,
            [Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY)]             ,
            [Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY),                Piece(Chessman.EMPTY)]             ,
            [Piece(Chessman.PAWN,   Colour.BLACK), Piece(Chessman.PAWN,   Colour.BLACK), Piece(Chessman.PAWN,   Colour.BLACK), Piece(Chessman.PAWN,   Colour.BLACK), Piece(Chessman.PAWN,   Colour.BLACK), Piece(Chessman.PAWN,   Colour.BLACK), Piece(Chessman.PAWN,   Colour.BLACK), Piece(Chessman.PAWN, Colour.BLACK)],
            [Piece(Chessman.ROOK,   Colour.BLACK), Piece(Chessman.KNIGHT, Colour.BLACK), Piece(Chessman.BISHOP, Colour.BLACK), Piece(Chessman.QUEEN,  Colour.BLACK), Piece(Chessman.KING,   Colour.BLACK), Piece(Chessman.BISHOP, Colour.BLACK), Piece(Chessman.KNIGHT, Colour.BLACK), Piece(Chessman.ROOK, Colour.BLACK)]
        ]

        for rank in range(self.height):
            for file in range(self.width):
                self.pieces[rank][file].pos = Pos(rank + 1, file + 1)

    def getPiece(self, *args) -> Piece:
        if len(args) == 0:
            raise ValueError(f"Invalid number of args, given {args}")

        elif len(args) == 1:
            if not len(args[0]) == 2:
                raise ValueError(f"Invalid value for position, expected a number and letter, given {args[0]}")

            file = ord(args[0][0]) - 97
            rank = int(args[0][1]) - 1

            return self.pieces[rank][file]

        elif len(args) == 2:
            rank, file = args
            rank -= 1

            if isinstance(file, str):
                file = ord(file) - 97
            elif isinstance(file, int):
                file  -= 1
            else:
                pass

            return self.pieces[rank][file]
        else:
            pass

    def performAction(self, action: Action) -> bool:
        srcPos = action.piece.pos
        destPos = action.pos

        if destPos.rank < 0 or destPos.rank >= self.width:
            raise ValueError(f"destPos Rank out of range: Please give a value between {0}-{self.width}. Value given: {destPos.rank}")

        if destPos.file < 0 or destPos.file >= self.height:
            raise ValueError(f"destPos File out of range: Please give a value between {0}-{self.height}. Value given: {destPos.file}")

        if action.actionType == ActionType.MOVE:
            # TODO: Implement actual legality checking. Currently just moves piece

            piece = self.pieces[srcPos.rank][srcPos.file]

            if piece.chessman == Chessman.EMPTY:
                return False

            self.pieces[srcPos.rank][srcPos.file] = Piece(Chessman.EMPTY, Colour.EMPTY, Pos(srcPos.rank + 1, srcPos.file + 1))
            self.pieces[destPos.rank][destPos.file] = piece
            piece.pos = destPos
            piece.moved = True

            self.lastMoved = piece

        return True

    def flipBoard(self) -> None:
        self.flipped = not self.flipped

    # TODO: Fill these in
    def isFinished(self):
        # If no actions left (either white or black has won)
        return False if len(self.getPieces(self.playerColour)) == 0 or len(self.getPieces(self.getAiColour)) == 0 else True

    def getPieces(self, playerColour : Colour) -> List[Piece]:
        pieces = []

        for rank in self.pieces:
            for piece in rank:
                if piece.colour == playerColour:
                    pieces.append(piece)

        return pieces

    def isValidAction(self, piece, act):
        # Meant to validate player move
        # Validate action (if specific piece can act in specified way)
        # Also call isValidMove
        return piece.isValidAction(act) and self.isValidMove(self, act)

    def isValidMove(self, act):
        # Validate move (check if piece collides with another piece of same colour or if piece moves off board)
        return True

    def gameScore(self):
        # Heuristic value if game not done, or final game value if game is done
        return False

    def getActions(self, playerColour : Colour):
        # Return all possible actions from player
        actions = []
        for p in self.getPieces(playerColour):
            for act in p.getActions():
                if self.isValidMove(act):
                    actions.append(act)
        return actions

    def childBoard(self, action):
        # Initialize and return new board with same state, but affected by input action
        return self