import chess

from minimax import *

def main():
    b = chess.Board()

    whiteMove = playerMove
    blackMove = aiMove

    while True:
        print(b.transform(chess.flip_vertical).transform(chess.flip_horizontal))
        whiteMove(b, chess.Color)
        print()

        if b.is_game_over():
            break

        print(b)
        blackMove(b, chess.Color)
        print()
        if b.is_game_over():
            break

    winner = b.outcome().winner
    if winner is None:
        print("Stalemate!")
    elif winner:
        print("White Won!")
    else:
        print("Black Won!")

def playerMove(board, _ : chess.Color):
    moved = False

    while not moved:
        try:
            board.push_san(input())
            moved = True
        except Exception:
            print("Illegal Move")

def aiMove(board, player : chess.Color):
    move = startMininmax(board, player, 10)
    board.push(move)
    print(move)

if __name__ == "__main__":
    main()