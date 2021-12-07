import math
from constants import *
from board import *
from action import *

def maxAlphaBeta(board : Board, alpha, beta, depth, aiColour : Colour):
    '''
    Get maximum value of child nodes. Based on pseuodocode provided from class for alpha-beta pruning.
    :input board: Board instance
    :input alpha: alpha value int
    :input beta: beta value int
    :input depth: int remaning depth of children
    :return: optimal value and Action instance
    '''
    if depth <= 0 or board.isFinished():
        return board.gameScore(aiColour), Action()
    
    optimalVal = None
    optimalAct = None
    for act in board.getActions(aiColour):
        childVal, childAct = minAlphaBeta(board.childBoard(act), alpha, beta, depth-1)
        if optimalVal is None or childVal > optimalVal:
            optimalVal = childVal
            optimalAct = childAct

        if childVal >= beta:
            return childVal, childAct
        alpha = max(alpha, childVal)

    return optimalVal, optimalAct

def minAlphaBeta(board : Board, alpha, beta, depth, aiColour : Colour):
    '''
    Get minimum value of child nodes. Based on pseuodocode provided from class for alpha-beta pruning.
    :input board: Board instance
    :input alpha: alpha value int
    :input beta: beta value int
    :input depth: int remaning depth of children
    :return: optimal value and Action instance
    '''
    if depth <= 0 or board.isFinished():
      return board.gameScore(aiColour), Action()
    
    optimalVal = None
    optimalAct = None
    for act in board.getActions(board.getOpponentColour(aiColour)):
        childVal, childAct = maxAlphaBeta(board.childBoard(act), alpha, beta, depth-1)
        if optimalVal is None or childVal < optimalVal:
            optimalVal = childVal
            optimalAct = childAct

        if childVal <= alpha:
            return childVal, childAct
        beta = min(beta, childVal)

    return optimalVal, optimalAct

def startMininmax(board : Board, aiColour : Colour):
    '''
    Estimate optimal value and action for ai using fixed depth.
    :input board: Board instance
    :return: optimal value and Action instance
    '''
    value, action = maxAlphaBeta(board, -math.inf, math.inf, DEPTH, aiColour)