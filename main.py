from src.algos.ucs import ucs_solve
from src.ui import show_ui


def main():
    print("Welcome to Pancakes Problem!")

    while True:
        print("Press Enter to continue or Q to quit.")
        action = input().strip()
        if action.upper() == "Q":
            print("Goodbye!")
            return
        elif action == "":
            break
        else:
            print("Invalid input. Please press Enter or Q.")

    while True:
        print("Enter the number of pancakes: ")
        try:
            number = int(input())
            if number > 1:
                break
            else:
                print("Please enter a number greater than 1.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Choose input mode
    while True:
        print("Choose mode for pancakes generation (M for manual / R for random input):")
        mode = input().strip().upper()
        pancakes: Optional[list[int]] = None
        if mode == "M":
            pancakes = user_pancakes(number)
            break
        elif mode == "R":
            pancakes = random_pancakes(number)
            break
        else:
            print("Wrong mode! Please enter 'M' or 'R'.")
    print(pancakes)
    result, visited = ucs_solve(pancakes, sorted(pancakes))
    print(visited)
    show_ui(visited)


def user_pancakes(number: int) -> list[int]:
    pancakes: list[str] = []
    possible_pancakes: list[str] = [str(i) for i in random_pancakes(number)]

    for i in range(number):
        print("=========================================")
        while True:
            print("Possible pancakes:")
            print(possible_pancakes)
            print("Your pancakes:")
            print(pancakes)
            print("Enter one of the possible pancakes: ")
            choice = input().strip()

            if choice not in possible_pancakes:
                print("=========================================")
                print("Invalid input. Please enter a valid number.")
                continue
            else:
                pancakes.append(choice)
                index = possible_pancakes.index(choice)
                possible_pancakes[index] = 'X'
                break
    print("=========================================")
    print("Your final pancakes:")
    print(pancakes)
    return [int(i) for i in pancakes]

def random_pancakes(number: int) -> list[int]:
    return list(random(1, number + 1))


if __name__ == '__main__':
    main()
