from src.pancakes_fuctions import is_solved, make_move


def ucs_solve(start_state: list[int], goal_state: list[int]):
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

        possible_moves: list[tuple[int, list[int], list[int]]] = get_all_possible_moves(current_state)
        for ps in possible_moves:
            if not is_visited(ps, visited):
                frontier = add_to_frontier(frontier, ps)

    return None


def add_to_frontier(frontier: list[tuple[int, list[int], list[int]]], state: tuple[int, list[int], list[int]]):
    new_frontier = []
    index = len(frontier)
    for i in range(len(frontier)):
        if state[0] < frontier[i][0]:
            index = i
            break

    new_frontier = frontier[:index] + [state] + frontier[index:]
    return new_frontier

def pop_frontier(frontier: list[tuple[int, list[int], list[int]]]) -> tuple[int, list[int], list[int]]:
    return frontier.pop(0)

def is_visited(state: tuple[int, list[int], list[int]], visited: list[list[int]]) -> bool:
    return state[1] in visited

def get_all_possible_moves(state: tuple[int, list[int], list[int]]) -> list[tuple[int, list[int], list[int]]]:
    possible_moves: list[tuple[int, list[int], list[int]]] = []
    s = state[1]
    for k in range(2, len(state[1]) + 1):
        ns = make_move(s, k)
        new_state: tuple[int, list[int], list[int]] = (state[0] + k, ns, state[2] + [k])
        possible_moves.append(new_state)

    return possible_moves
