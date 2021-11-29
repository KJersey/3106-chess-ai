from board import *

def main():
    b = Board()
    b.movePiece(Pos("1a"), Pos("4d"))
    b.movePiece(Pos("2a"), Pos("1a"))
    print(b)

if __name__ == "__main__":
    main()