def total_distance_heuristic(current_state: list[int], goal_state: list[int]) -> int:
    return sum(abs(i - goal_state.index(p)) for i, p in enumerate(current_state))
