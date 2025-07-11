from typing import Optional
from src.algo_functions import add_to_frontier, pop_frontier, get_all_possible_moves, is_visited, add_visited
from src.pancakes_fuctions import is_solved


def ucs_solve(start_state: list[int], goal_state: list[int]) -> Optional[tuple[int, list[int], list[int]]]:
    frontier: list[tuple[int, list[int], list[int]]] = []
    visited: list[list[int]] = []

    current_state: tuple[int, list[int], list[int]] = (0, start_state, [])
    frontier = add_to_frontier(frontier, current_state)
    while frontier:
        current_state: tuple[int, list[int], list[int]] = pop_frontier(frontier)

        if is_solved(current_state[1], goal_state):
            return current_state

        if is_visited(current_state, visited):
            continue
        add_visited(current_state, visited)

        possible_moves: list[tuple[int, list[int], list[int]]] = get_all_possible_moves(current_state)
        for ps in possible_moves:
            if not is_visited(ps, visited):
                frontier = add_to_frontier(frontier, ps)

    return None
