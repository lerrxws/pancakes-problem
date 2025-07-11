def make_move(pancakes: list[int], k: int) -> list[int]:
    new_stack = pancakes[:]  # make a shallow copy
    for i in range(k // 2):
        temp = new_stack[i]
        new_stack[i] = new_stack[k - i - 1]
        new_stack[k - i - 1] = temp
    return new_stack

def is_move_possible(pancakes: list[int], k: int) -> bool:
    if k < 2 or len(pancakes) < k:
        return False

    return True

def is_solved(pancakes: list[int], goal_state: list[int]) -> bool:
    return pancakes == goal_state

def count_unplaced_pancakes(pancakes: list[int]) -> int:
    unplaced_pancakes = 0
    for pancake in range(len(pancakes) - 1):
        if pancakes[pancake] > pancakes[pancake + 1]:
            unplaced_pancakes += 1

    return unplaced_pancakes


#
# pancakes = [1, 2, 3, 4, 5]
# # result = make_move(pancakes, 4)
# # result = is_move_possible(pancakes, k = 4)
# result = make_move(pancakes, 5)
# print(result)