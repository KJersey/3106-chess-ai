from typing import List
import numpy as np

from piece import *
from action import *

class Board:
    def __init__(self, fen : str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", prevFens : list = []):

        fields = fen.split(' ')
        rows = fields[0].split('/')

        self.pieces = []

        rank = 8
        for r in rows:
            row = []
            file = 1
            for c in r:
                if c == 'p':
                    row.append(Piece(Chessman.PAWN, Colour.BLACK, Pos(rank, file)))
                elif c == 'P':
                    row.append(Piece(Chessman.PAWN, Colour.WHITE, Pos(rank, file)))
                elif c == 'r':
                    row.append(Piece(Chessman.ROOK, Colour.BLACK, Pos(rank, file)))
                elif c == 'R':
                    row.append(Piece(Chessman.ROOK, Colour.WHITE, Pos(rank, file)))
                elif c == 'n':
                    row.append(Piece(Chessman.KNIGHT, Colour.BLACK, Pos(rank, file)))
                elif c == 'N':
                    row.append(Piece(Chessman.KNIGHT, Colour.WHITE, Pos(rank, file)))
                elif c == 'b':
                    row.append(Piece(Chessman.BISHOP, Colour.BLACK, Pos(rank, file)))
                elif c == 'B':
                    row.append(Piece(Chessman.BISHOP, Colour.WHITE, Pos(rank, file)))
                elif c == 'q':
                    row.append(Piece(Chessman.QUEEN, Colour.BLACK, Pos(rank, file)))
                elif c == 'Q':
                    row.append(Piece(Chessman.QUEEN, Colour.WHITE, Pos(rank, file)))
                elif c == 'k':
                    row.append(Piece(Chessman.KING, Colour.BLACK, Pos(rank, file)))
                elif c == 'K':
                    row.append(Piece(Chessman.KING, Colour.WHITE, Pos(rank, file)))
                else:
                    for _ in range(int(c)):
                        row.append(Piece(Chessman.EMPTY, Colour.EMPTY, Pos(rank, file)))
                        file += 1
                    file -= 1
                
                file += 1
            self.pieces.insert(0, row)
            rank -= 1

        self.currentPlayer = Colour.WHITE if fields[1] == 'w' else Colour.BLACK
        self.castleRights = CastleRights('K' in fields[2], 'Q' in fields[2], 'k' in fields[2], 'q' in fields[2])
        self.enPassantTarget = None if fields[3] == '-' else Pos(fields[3])
        self.halfMove = int(fields[4])
        self.fullTurn = int(fields[5])
        self.prevFens = prevFens

    def __str__(self) -> str:
        s = ""

        pieces = self.pieces
        if self.currentPlayer == Colour.BLACK:
            pieces = np.flip(pieces)

        board = ""

        for rank in range(8):
            row = (str(8 - rank) if self.currentPlayer == Colour.BLACK else str(rank + 1)) + "│" + ANSIColours.fgBrightBlack
            for file in range(8):
                row += ANSIColours.bgWhite if (rank + file) % 2 else ANSIColours.bgBlack # ANSI Background colours
                row += str(pieces[rank][file]) + ' '
                
            row += ANSIColours.reset + "\n" # Reset background colour
            board = row + board

        s += board

        s += "─┼"
        for _ in range(8):
            s += '──'

        s += '\n │'

        for file in range(8):
            s += chr(96 + (8 - file if self.currentPlayer == Colour.BLACK else file + 1)) + ' '

        return s

    def clearBoard(self) -> None:
        self.pieces = []
        for _ in range(8):
            row = []
            for _ in range(8):
                row.append(Piece())
            self.pieces.append(row)

    def run(self, whiteMove, blackMove) -> None:
        while True:
            print(self)
            if (self.currentPlayer == Colour.WHITE):
                whiteMove(self, Colour.WHITE)
            else:
                blackMove(self, Colour.BLACK)

            print(self.genFen())

            if self.isFinished():
                break


    def genFen(self) -> str:
        fen = ""

        for i in range(7, -1, -1):
            counter = 0
            for piece in self.pieces[i]:
                if piece.chessman == Chessman.EMPTY:
                    counter += 1
                elif counter > 0:
                    fen += str(counter)
                    counter = 0
                    fen += piece.getASCII()
                else:
                    fen += piece.getASCII()

            if counter > 0:
                fen += str(counter)
            fen += '/'

        fen = fen[:-1] + ' '

        fen += 'w ' if self.currentPlayer == Colour.WHITE else 'b '

        cr = ''

        if self.castleRights.K:
            cr += 'K'
        if self.castleRights.Q:
            cr += 'Q'
        if self.castleRights.k:
            cr += 'k'
        if self.castleRights.q:
            cr += 'q'
        if cr == '':
            cr = '-'

        fen += cr + ' '

        if not self.enPassantTarget is None:
            fen += str(self.enPassantTarget) + ' '
        else:
            fen += '- '

        fen += str(self.halfMove) + ' ' + str(self.fullTurn)

        return fen

    def getOpponentColour(self, playerColour : Colour):
        return Colour.BLACK if playerColour == Colour.WHITE else Colour.WHITE

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

    def getPieces(self, playerColour : Colour) -> List[Piece]:
        pieces = []
        for rank in self.pieces:
            for piece in rank:
                if piece.colour == playerColour:
                    pieces.append(piece)
        return pieces

    def performAction(self, action : Action, skipValidity : bool = False) -> bool:
        srcPos = action.piece.pos
        destPos = action.pos

        if destPos.rank < 0 or destPos.rank >= 8:
            raise ValueError(f"destPos Rank out of range: Please give a value between {0}-{8}. Value given: {destPos.rank}")
        elif destPos.file < 0 or destPos.file >= 8:
            raise ValueError(f"destPos File out of range: Please give a value between {0}-{8}. Value given: {destPos.file}")

        piece = self.pieces[srcPos.rank][srcPos.file]
        if not skipValidity:
            if not self.isValidAction(piece, action):
                return False

        capture = False

        if action.actionType == ActionType.MOVE:
            # TODO: Currently just moves piece (add pawn promotion)
            if piece.chessman == Chessman.EMPTY:
                return False

            self.pieces[srcPos.rank][srcPos.file] = Piece(Chessman.EMPTY, Colour.EMPTY, Pos(srcPos.rank + 1, srcPos.file + 1))

            if not self.pieces[destPos.rank][destPos.file].chessman == Chessman.EMPTY:
                capture = True

            self.pieces[destPos.rank][destPos.file] = piece
            piece.pos = destPos

            if piece.chessman == Chessman.PAWN and abs(destPos.rank - srcPos.rank) == 2:
                self.enPassantTarget = Pos(destPos.rank + (0 if self.currentPlayer == Colour.WHITE else 2), destPos.file + 1)
            else:
                self.enPassantTarget = None

                if piece.chessman == Chessman.KING:
                    if piece.colour == Colour.WHITE:
                        self.castleRights.K = False
                        self.castleRights.Q = False
                    else:
                        self.castleRights.k = False
                        self.castleRights.q = False
                    self.enPassantTarget = None
                elif piece.chessman == Chessman.ROOK:
                    if srcPos.rank == 0 and srcPos.file == 0 and piece.colour == Colour.WHITE:
                        self.castleRights.Q = False
                    elif srcPos.rank == 0 and srcPos.file == 7 and piece.colour == Colour.WHITE:
                        self.castleRights.K = False
                    elif srcPos.rank == 7 and srcPos.file == 0 and piece.colour == Colour.BLACK:
                        self.castleRights.q = False
                    elif srcPos.rank == 7 and srcPos.file == 7 and piece.colour == Colour.BLACK:
                        self.castleRights.k = False
                    

            

        self.currentPlayer = Colour.BLACK if self.currentPlayer == Colour.WHITE else Colour.WHITE

        if piece.chessman == Chessman.PAWN or capture:
            self.halfMove = 0
        else:
            self.halfMove += 1

        if self.currentPlayer == Colour.WHITE:
            self.fullTurn += 1

        self.prevFens.append(self.genFen())

        return True

    def getPieceActions(self, piece):
        actions = []
        directionsNonDiag = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        directionsDiag = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
        srcRank = piece.pos.rank + 1
        srcFile = piece.pos.file + 1

        if piece.chessman == Chessman.PAWN:
            advanceDirection = 1 if piece.colour == Colour.WHITE else -1
            actions.append(Action(ActionType.MOVE, piece, Pos(srcRank + advanceDirection*1, srcFile)))
            if piece.pos.rank == 1 or piece.pos.rank == 6:
                actions.append(Action(ActionType.MOVE, piece, Pos(srcRank + advanceDirection*2, srcFile)))
        if piece.chessman == Chessman.ROOK or piece.chessman == Chessman.BISHOP or piece.chessman == Chessman.QUEEN:
            # TODO: only add actions for Chessman.ROOK when the king castles
            directions = []
            if piece.chessman != Chessman.BISHOP:
                directions += directionsNonDiag
            if piece.chessman != Chessman.ROOK:
                directions += directionsDiag
            for dir in directions:
                for i in range(1, 8): # horizontally or vertically up to 8
                    action = Action(ActionType.MOVE, piece, Pos(srcRank + i*dir[0], srcFile + i*dir[1]))
                    if not self.noCollisions(action):
                        break
                    actions.append(action)

        if piece.chessman == Chessman.KNIGHT:
                actions.append(Action(ActionType.MOVE, piece, Pos(srcRank + 2, srcFile + 1)))
                actions.append(Action(ActionType.MOVE, piece, Pos(srcRank + 1, srcFile + 2)))
                actions.append(Action(ActionType.MOVE, piece, Pos(srcRank + 2, srcFile - 1)))
                actions.append(Action(ActionType.MOVE, piece, Pos(srcRank + 1, srcFile - 2)))
                actions.append(Action(ActionType.MOVE, piece, Pos(srcRank - 2, srcFile + 1)))
                actions.append(Action(ActionType.MOVE, piece, Pos(srcRank - 1, srcFile + 2)))
                actions.append(Action(ActionType.MOVE, piece, Pos(srcRank - 2, srcFile - 1)))
                actions.append(Action(ActionType.MOVE, piece, Pos(srcRank - 1, srcFile - 2)))
        if piece.chessman == Chessman.KING:
            directions = directionsNonDiag + directionsDiag
            for dir in directions:
                actions.append(Action(ActionType.MOVE, piece, Pos(srcRank + dir[0], srcFile + dir[1])))

        return actions

    def isValidPieceAction(self, piece, action):
        for move in self.getPieceActions(piece):
            # Check if input action matches an available action
            if action.actionType == move.actionType and action.piece == piece and action.pos == move.pos:
                return True
        return False

    def isValidAction(self, piece, act):
        return self.isValidPieceAction(piece, act) and self.noCollisions(act)

    def noCollisions(self, act):
        # Validate move, check if piece collides with another piece of same colour anywhere, if another piece in between path
        destPos = act.pos
        if destPos.rank < 0 or destPos.rank >= 8 or destPos.file < 0 or destPos.file >= 8:
            return False
        
        # Check if destPos contains piece of same colour
        destPiece = self.pieces[destPos.rank][destPos.file]
        if destPiece.colour == act.piece.colour:
            return False
        
        if act.piece.chessman == Chessman.KNIGHT:
            # Will hop over all pieces inside of path
            return True

        # Pawns cannot capture forwards
        if act.piece.chessman == Chessman.PAWN and not self.pieces[destPos.rank][destPos.file].chessman == Chessman.EMPTY:
            return False

        rank = act.piece.pos.rank
        file = act.piece.pos.file
        changeRank = 0
        changeFile = 0
        if destPos.rank < act.piece.pos.rank: # Up
            changeRank = -1
        elif destPos.rank > act.piece.pos.rank: # Down
            changeRank = 1
        if destPos.file < act.piece.pos.file: # Left
            changeFile = -1
        elif destPos.file > act.piece.pos.file: # Right
            changeFile = 1

        # Calc Steps
        steps = max(abs(act.piece.pos.rank-destPos.rank), abs(act.piece.pos.file-destPos.file))

        # For each step, check if a piece is in the way
        for i in range(steps-1):
            rank += changeRank
            file += changeFile
            
            if self.pieces[rank][file].chessman != Chessman.EMPTY:
                return False

        return True

    def gameScore(self, playerColour : Colour):
        # Heuristic value if game not done, or final game value if game is done
        # TODO: account for doubled, blocked, isolated pawns (-0.5 each for AI side, +0.5 each for player side)
        pieceDiff = {}
        for row in self.pieces:
            for piece in row:
                if piece.chessman not in pieceDiff:
                    pieceDiff[piece.chessman] = 0
                
                if piece.colour == playerColour:
                    pieceDiff[piece.chessman] += 1
                else:
                    pieceDiff[piece.chessman] -= 1
        
        value = 0
        for chessman in pieceDiff:
            value += ChessmanValue[chessman] * pieceDiff[chessman]

        doubled = 0
        # TODO: Calc doubled

        blocked = 0
        # TODO: Calc blocked

        isolated = 0
        # TODO: Calc isolated

        value -= 0.5 * (doubled + blocked + isolated)

        # Compare number of legal actions
        mobility = len(self.getActions(playerColour)) - len(self.getActions(self.getOpponentColour(playerColour)))

        value += 0.1 * mobility

        return value

    def getActions(self, playerColour : Colour):
        # Return all possible actions from player
        actions = []
        for p in self.getPieces(playerColour):
            for act in self.getPieceActions(p):
                if self.noCollisions(act):
                    actions.append(act)
        return actions

    def childBoard(self, action):
        # Initialize new board starting from same state
        childBoard = Board(self.genFen(), self.prevFens) 
        # Apply action on childBoard
        try:
            childBoard.performAction(action, skipValidity=True)
            return childBoard
        except Exception as e:
            raise e

    def isFinished(self):
        # If no actions left, return winner
        if len(self.getActions(Colour.WHITE)) == 0:
            return Colour.BLACK
        elif len(self.getActions(Colour.BLACK)) == 0:
            return Colour.WHITE
        return False