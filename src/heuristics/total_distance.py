def total_distance_heuristic(current_state: list[int]) -> int:
    goal_state = sorted(current_state)
    return sum(abs(i - goal_state.index(p)) for i, p in enumerate(current_state))
