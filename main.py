from board import *

def main():
    b = Board()
    b.movePiece(Pos("2a"), Pos("4a"))
    print(b)
    print()
    b.flipBoard()
    b.movePiece(Pos("2b"), Pos("4b"))
    print(b)

if __name__ == "__main__":
    main()