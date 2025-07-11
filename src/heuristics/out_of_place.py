def out_ot_place_heuristic(current_state: list[int]) -> int:
    unplaced_pancakes = 0
    for pancake in range(len(current_state) - 1):
        if current_state[pancake] > current_state[pancake + 1]:
            unplaced_pancakes += 1

    return unplaced_pancakes