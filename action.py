from piece import *

class Action:
    def __init__(self, actionType : ActionType = ActionType.NO_ACTION, piece : Piece = Piece(), pos : Pos = Pos(), chessman : Chessman = Chessman.EMPTY):
        self.actionType = actionType
        self.piece = piece
        self.pos = pos
        self.chessman = chessman

    def __str__(self) -> str:
        s = ""

        if self.actionType == ActionType.NO_ACTION:
            s += "No Action "
        elif self.actionType == ActionType.MOVE:
            s += "Move "
        elif self.actionType == ActionType.CASTLE:
            s += "Castle "
        elif self.actionType == ActionType.PROMOTION:
            s += "Promotion to: "
            if self.chessman == Chessman.ROOK:
                s += "Rook "
            elif self.chessman == Chessman.KNIGHT:
                s += "Knight "
            elif self.chessman == Chessman.BISHOP:
                s += "Bishop "
            else:
                raise ValueError(f"Cannot promote to {self.chessman}")

        s += f"from piece at {self.piece.pos} to {self.pos}."

        return s