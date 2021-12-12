import math
import time

import chess
 
class TimeoutException(Exception):
    pass

def maxAlphaBeta(board : chess.Board, player : chess.Color, alpha, beta, depth, startTime : int, maxTime : int):
    '''
    Get maximum value of child nodes. Based on pseuodocode provided from class for alpha-beta pruning.
    :input board: Board instance
    :input alpha: alpha value int
    :input beta: beta value int
    :input depth: int remaning depth of children
    :return: optimal value and Action instance
    '''
    if time.time() - startTime > maxTime:
        raise TimeoutException("Out of time")

    if depth <= 0:
        return heuristic(board), None

    if board.is_game_over():
        winner = board.outcome().winner

        if winner is None:
            return 0, None

        if winner == player:
            return 200, None
        
        return -200, None
    
    optimalVal = None
    optimalMove = None
    for move in board.legal_moves:
        childBoard = board.copy()
        childBoard.push(move)
        childVal, _ = minAlphaBeta(childBoard, player, alpha, beta, depth - 1, startTime, maxTime)
        if optimalVal is None or childVal > optimalVal:
            optimalVal = childVal
            optimalMove = move

        if childVal >= beta:
            return childVal, optimalMove
        alpha = max(alpha, childVal)

    return optimalVal, optimalMove

def minAlphaBeta(board : chess.Board, player : chess.Color, alpha, beta, depth, startTime : int, maxTime : int):
    '''
    Get minimum value of child nodes. Based on pseuodocode provided from class for alpha-beta pruning.
    :input board: Board instance
    :input alpha: alpha value int
    :input beta: beta value int
    :input depth: int remaning depth of children
    :return: optimal value and Action instance
    '''
    if (time.time() - startTime) > maxTime:
        raise TimeoutException("Out of time")

    if depth <= 0:
        return heuristic(board), None

    if board.is_game_over():
        winner = board.outcome().winner

        if winner == player:
            return -200, None
        
        return 200, None

    optimalVal = None
    optimalMove = None
    for move in board.legal_moves:
        childBoard = board.copy()
        childBoard.push(move)
        childVal, _ = maxAlphaBeta(childBoard, player, alpha, beta, depth - 1, startTime, maxTime)
        if optimalVal is None or childVal < optimalVal:
            optimalVal = childVal
            optimalMove = move

        if childVal <= alpha:
            return childVal, optimalMove
        beta = min(beta, childVal)

    return optimalVal, optimalMove

def startMininmax(board : chess.Board, player : chess.Color, maxTime : int):
    '''
    Estimate optimal value and action for ai using varied depth.
    :input board: Board instance
    :return: optimal value and Action instance
    '''

    startTime = time.time()
    depth = 1
    while True:
        try:
            v, m = maxAlphaBeta(board, player, -math.inf, math.inf, depth, startTime, maxTime)
            depth += 1
        except TimeoutException:
            break


    print(f"Searched to a depth of {depth} with score {v}!")

    return m

def heuristic(board : chess.Board):
    v = 0

    for _ in board.pieces(chess.QUEEN, board.turn):
        v += 9
    for _ in board.pieces(chess.QUEEN, not board.turn):
        v -= 9

    for _ in board.pieces(chess.ROOK, board.turn):
        v += 5
    for _ in board.pieces(chess.ROOK, not board.turn):
        v -= 5

    for _ in board.pieces(chess.BISHOP, board.turn):
        v += 3
    for _ in board.pieces(chess.BISHOP, not board.turn):
        v -= 3

    for _ in board.pieces(chess.KNIGHT, board.turn):
        v += 3
    for _ in board.pieces(chess.KNIGHT, not board.turn):
        v -= 3

    for _ in board.pieces(chess.PAWN, board.turn):
        v += 1
    for _ in board.pieces(chess.PAWN, not board.turn):
        v -= 1

    for _ in board.legal_moves:
        v += 0.1

    childBoard = board.copy()
    childBoard.push(chess.Move.null())

    for _ in childBoard.legal_moves:
        v -= 0.1

    if board.turn:
        return -v

    return v