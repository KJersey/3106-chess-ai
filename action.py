from constants import *

class Action:
    def __init__(self, actionType : ActionType = ActionType.NO_ACTION, moves : list = []):
        self.actionType = actionType
        self.moves = moves # List of single line movements in form [Movement movements...], ex. [UP, UP, UP, LEFT] or [DIAG_UP_LEFT, DIAG_UP_LEFT, DIAG_UP_LEFT]
        self.startPos = [0, 0]