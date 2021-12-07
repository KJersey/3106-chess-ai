from board import *
from minimax import *

def main():
    b = Board()
    aiColour = Colour.BLACK
    playerColour = Colour.WHITE
    winner = False
    while not winner:
        if (b.currentPlayer == playerColour):
            print(f"\nPlayer ({getColourString(playerColour)}) turn:\n"+str(b))
            playerMove(b, playerColour)
        winner = b.isFinished()
        if winner:
            break

        if (b.currentPlayer == aiColour):
            print(f"\nAI ({getColourString(aiColour)}) turn:\n"+str(b))
            aiMove(b, aiColour)
        winner = b.isFinished()
        if winner:
            break
    print(f"The winner is {getColourString(winner)}!")

def playerMove(b : Board, playerColour : Colour):
  flag = True
  while flag:
    try:
        action = getPlayerAction(b, playerColour)
        print(action)
        status = b.performAction(action)
        if status:
            flag = False
        else:
            print("Could not perform action. Please try a different one.")
    except ValueError as e:
        print(e)

def getPlayerAction(b : Board, playerColour : Colour):
    playerColourStr = getColourString(playerColour)
    srcPieceStr = input("Enter piece to move: ")
    srcPiece = b.getPiece(srcPieceStr)
    if srcPiece.colour != playerColour:
        raise ValueError(f"Piece located at {srcPiece} is not valid. Please choose a piece of colour {playerColourStr}.")
    destStr = input(f"Enter where to move piece at {srcPieceStr}: ")
    action = Action(ActionType.MOVE, srcPiece, Pos(destStr))
    # TODO: adjust ActionType and chessman in returned action
    return action

def aiMove(b : Board, aiColour : Colour):
    print("The AI is thinking...")
    action = getAiAction(b, aiColour)
    b.performAction(action, skipValidity=True)

def getAiAction(b : Board, aiColour : Colour):
    value, action = startMininmax(b, aiColour)
    print(action)
    print("Action value:", value)
    return action

def getColourString(colour : Colour):
    if colour == Colour.BLACK:
        return "black"
    elif colour == Colour.WHITE:
        return "white"
    return "none"

if __name__ == "__main__":
    main()