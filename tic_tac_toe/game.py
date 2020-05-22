"""This is a module for playing Tic-Tac-Toe."""
from tic_tac_toe.board import Board
from tic_tac_toe.btree import Tree


def main():
    """Play Tic-Tac-Toe."""
    board = Board([[" " for _ in range(3)] for _ in range(3)])
    print("Enter a pair of coordinates separated by space in range "
          "from 0 to 2 (e.g, 1 1).")
    while board.check_state() != 0:
        print(board)

        coords = input("> ").strip().split()
        try:
            x, y = (int(coord) for coord in coords)
            board.make_move(x, y)
        except ValueError:
            print("Enter a valid pair of coordinates.")
            continue
        if board.check_state() == -1:
            print(board)
            print("You won!")
            break

        tree = Tree(board)
        x, y = tree.find_best_move()
        board.make_move(x, y)
        if board.check_state() == 1:
            print(board)
            print("Computer won!")
            break
    if board.check_state() == 0:
        print(board)
        print("Draw!")


if __name__ == '__main__':
    main()
