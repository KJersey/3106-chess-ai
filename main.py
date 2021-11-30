from board import *

def main():
    b = Board()
    a = Action(ActionType.MOVE, b.getPiece("a2"), Pos("a4"))
    b.movePiece(a)
    print(b)

if __name__ == "__main__":
    main()