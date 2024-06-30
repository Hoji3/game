def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")

def get_input(board):
    while True:
        step = input("Ваш ход: ")
        if not step.isdigit():
            print('Некорректный ввод')
            continue
        step = int(step)
        if step not in board:
            print('Неправильный ход')
            continue
        return step - 1


def check_win(board):
    combinations = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )
    for a, b, c in combinations:
        if board[a] == board[b] == board[c]:
            return True
    return False


def print_field(board):
    for i in range(3):
        print(*board[i*3:i*3+3], sep=' | ')
        if i != 2:
            print('-' * 9)


def main():
    count = 0
    board = list(range(1, 10))
    while True:
        symbol = '\033[31mx\033[0m' if count % 2 == 0 else '\033[34mo\033[0m'

        print_field(board)
        get_input(board)
        step = get_input(board)
        board[step] = symbol

        if check_win(board):
            print(f'Победил {symbol}')
            print_field(board)
            break

        count += 1
        if count == 9:
            print('Ничья')
            print_field(board)
            break
greet()
main()
