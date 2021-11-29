import math
from constants import *
from board import *
from action import *

def maxAlphaBeta(board, alpha, beta, depth):
    '''
    Get maximum value of child nodes. Based on pseuodocode provided from class for alpha-beta pruning.
    :input board: Board instance
    :input alpha: alpha value int
    :input beta: beta value int
    :input depth: int remaning depth of children
    :return: optimal value and Action instance
    '''
    if depth <= 0 or board.isFinished():
        return board.gameScore(), Action()
    
    optimalVal = None
    optimalAct = None
    for act in board.getActions(Colour.WHITE):
        childVal, childAct = minAlphaBeta(board.childBoard(act), alpha, beta, depth-1)
        if optimalVal is None or childVal > optimalVal:
            optimalVal = childVal
            optimalAct = childAct

        if childVal >= beta:
            return childVal, childAct
        alpha = max(alpha, childVal) # TODO: check if changing value here will change value in parent

    return optimalVal, optimalAct

def minAlphaBeta(board, alpha, beta, depth):
    '''
    Get minimum value of child nodes. Based on pseuodocode provided from class for alpha-beta pruning.
    :input board: Board instance
    :input alpha: alpha value int
    :input beta: beta value int
    :input depth: int remaning depth of children
    :return: optimal value and Action instance
    '''
    if depth <= 0 or board.isFinished():
      return board.gameScore(), Action()
    
    optimalVal = None
    optimalAct = None
    for act in board.getActions(Colour.BLACK):
        childVal, childAct = maxAlphaBeta(board.childBoard(act), alpha, beta, depth-1)
        if optimalVal is None or childVal < optimalVal:
            optimalVal = childVal
            optimalAct = childAct

        if childVal <= alpha:
            return childVal, childAct
        beta = min(beta, childVal) # TODO: check if changing value here will change value in parent

    return optimalVal, optimalAct

def startMininmax(board):
    '''
    Estimate optimal value and action for ai using fixed depth.
    :input board: Board instance
    :return: optimal value and Action instance
    '''
    value, action = maxAlphaBeta(board, -math.inf, math.inf, DEPTH)