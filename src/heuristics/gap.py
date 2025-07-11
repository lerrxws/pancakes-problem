def gap_heuristic(current_state: list[int]) -> int:
    gap = 0
    for i in range(len(current_state) - 1):
        if abs(current_state[i] - current_state[i + 1]) >= 2:
            gap += 1

    return gap
