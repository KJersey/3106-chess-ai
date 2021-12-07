from board import *
from minimax import *

def main():
    b = Board()
    # TODO: implement game logic

def playerMove(b : Board):
  flag = True
  while flag:
    action = getPlayerAction(b)
    try:
      b.performAction(action)
      flag = False
    except ValueError as e:
      print(e)

def getPlayerAction(b : Board, playerColour : Colour):
    playerColourStr = "black" if playerColour == Colour.BLACK else "white"
    srcPieceStr = input("Enter piece to move: ")
    srcPiece = b.getPiece(srcPieceStr)
    if srcPiece.colour != playerColour:
        raise ValueError(f"Piece located at {srcPiece} is not valid. Please choose a piece of colour {playerColourStr}.")
    destStr = input(f"Enter where to move {srcPiece}: ")
    action = Action(ActionType.MOVE, srcPiece, Pos(destStr))
    # TODO: adjust ActionType and chessman in returned action
    return action

def getAiAction(b : Board, aiColour : Colour):
    value, action = startMininmax(b, aiColour)
    b.performAction(action)

if __name__ == "__main__":
    main()