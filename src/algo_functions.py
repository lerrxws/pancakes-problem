from src.heuristics.gap import gap_heuristic
from src.heuristics.out_of_place import out_ot_place_heuristic
from src.heuristics.total_distance import total_distance_heuristic
from src.pancakes_fuctions import make_move


def add_to_frontier(frontier: list[tuple[int, list[int], list[int]]], state: tuple[int, list[int], list[int]]):
    index = len(frontier)
    for i in range(len(frontier)):
        if state[0] < frontier[i][0]:
            index = i
            break

    return frontier[:index] + [state] + frontier[index:]

def pop_frontier(frontier: list[tuple[int, list[int], list[int]]]) -> tuple[int, list[int], list[int]]:
    return frontier.pop(0)

def is_visited(state: tuple[int, list[int], list[int]], visited: list[list[int]]) -> bool:
    return state[1] in visited

def add_visited(state: tuple[int, list[int], list[int]], visited: list[list[int]]) -> list[list[int]]:
    visited.append(state[1])
    return visited

def get_all_possible_moves(state: tuple[int, list[int], list[int]], use_g: bool = True) -> list[tuple[int, list[int], list[int]]]:
    possible_moves: list[tuple[int, list[int], list[int]]] = []
    s = state[1]
    for k in range(2, len(state[1]) + 1):
        g = k if use_g else 0
        ns = make_move(s, k)
        new_state: tuple[int, list[int], list[int]] = (state[0] + g, ns, state[2] + [k])
        possible_moves.append(new_state)

    return possible_moves

def get_heuristic_cost(state: list[int], heuristic: str) -> int:
    if heuristic == "gap":
        return gap_heuristic(state)
    elif heuristic == "out_of_place":
        return out_ot_place_heuristic(state)
    elif heuristic == "distance":
        return total_distance_heuristic(state)
    else:
        raise ValueError("Invalid heuristic")

def add_heuristic_cost(possible_moves: list[tuple[int, list[int], list[int]]], heuristic: str) -> list[tuple[int, list[int], list[int]]]:
    update_pm: list[tuple[int, list[int], list[int]]] = []
    for pm in possible_moves:
        heuristic_cost = get_heuristic_cost(pm[1], heuristic)
        update_pm.append((pm[0] + heuristic_cost, pm[1], pm[2] + [pm[0] + heuristic_cost]))

    return update_pm