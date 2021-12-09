from board import *
from minimax import *

def main():
    b = Board()
    b.run(aiMove, playerMove)

def playerMove(b : Board, playerColour : Colour):
  while True:
    try:
        action = getPlayerAction(b, playerColour)
        print(action)
        status = b.performAction(action)
        if status:
            break
        else:
            print("Could not perform action. Please try a different one.")
    except ValueError as e:
        print(e)

def getPlayerAction(b : Board, playerColour : Colour):
    playerColourStr = getColourString(playerColour)
    srcPieceStr = input("Enter piece to move: ")
    srcPiece = b.getPiece(srcPieceStr)
    if srcPiece.colour != playerColour:
        raise ValueError(f"Piece located at {srcPieceStr} is not valid. Please choose a piece of colour {playerColourStr}.")
    destStr = input(f"Enter where to move piece at {srcPieceStr}: ")
    action = Action(ActionType.MOVE, srcPiece, Pos(destStr))
    # TODO: adjust ActionType and chessman in returned action
    return action

def aiMove(b : Board, aiColour : Colour):
    print("The AI is thinking...")
    action = getAiAction(b, aiColour)
    b.performAction(action, skipValidity=True)

def getAiAction(b : Board, aiColour : Colour):
    value, action = startMininmax(b, aiColour, 10)
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
    try:
        main()
    except KeyboardInterrupt:
        print("Game exited by user!")