from constants import *

class Action:
    def __init__(self, actionType : ActionType = ActionType.NO_ACTION, moves : list = []):
        self.actionType = actionType
        self.moves = moves