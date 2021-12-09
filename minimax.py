import math
import time
from constants import *
from board import *
from action import *
 
def maxAlphaBeta(board : Board, alpha, beta, depth, aiColour : Colour, startTime : int, maxTime : int):
    '''
    Get maximum value of child nodes. Based on pseuodocode provided from class for alpha-beta pruning.
    :input board: Board instance
    :input alpha: alpha value int
    :input beta: beta value int
    :input depth: int remaning depth of children
    :return: optimal value and Action instance
    '''
    if time.time() - startTime > maxTime:
        raise Exception("Out of time")

    if depth <= 0 or board.isFinished():
        return board.gameScore(aiColour), Action()
    
    optimalVal = None
    optimalAct = None
    for act in board.getActions(aiColour):
        childVal, childAct = minAlphaBeta(board.childBoard(act), alpha, beta, depth-1, aiColour, startTime, maxTime)
        if optimalVal is None or childVal > optimalVal:
            optimalVal = childVal
            optimalAct = act

        if childVal >= beta:
            return childVal, childAct
        alpha = max(alpha, childVal)

    return optimalVal, optimalAct

def minAlphaBeta(board : Board, alpha, beta, depth, aiColour : Colour, startTime : int, maxTime : int):
    '''
    Get minimum value of child nodes. Based on pseuodocode provided from class for alpha-beta pruning.
    :input board: Board instance
    :input alpha: alpha value int
    :input beta: beta value int
    :input depth: int remaning depth of children
    :return: optimal value and Action instance
    '''
    if (time.time() - startTime) > maxTime:
        raise Exception("Out of time")

    if depth <= 0 or board.isFinished():
      return board.gameScore(aiColour), Action()
    
    optimalVal = None
    optimalAct = None
    for act in board.getActions(board.getOpponentColour(aiColour)):
        childVal, childAct = maxAlphaBeta(board.childBoard(act), alpha, beta, depth-1, aiColour, startTime, maxTime)
        if optimalVal is None or childVal < optimalVal:
            optimalVal = childVal
            optimalAct = act

        if childVal <= alpha:
            return childVal, childAct
        beta = min(beta, childVal)

    return optimalVal, optimalAct

def startMininmax(board : Board, aiColour : Colour, maxTime : int):
    '''
    Estimate optimal value and action for ai using varied depth.
    :input board: Board instance
    :return: optimal value and Action instance
    '''

    startTime = time.time()
    depth = 1
    while True:
        try:
            v, a = maxAlphaBeta(board, -math.inf, math.inf, depth, aiColour, startTime, maxTime)
            depth += 1
        except:
            break


    print(f"Took {time.time() - startTime}s and went to a depth of {depth}!")

    return v, a