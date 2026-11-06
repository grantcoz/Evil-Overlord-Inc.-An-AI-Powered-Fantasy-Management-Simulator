from game.state import GameState

initial_state = GameState()

def is_goal(state: Gamestate) -> bool:
    return state.crown_stolen and state.escaped