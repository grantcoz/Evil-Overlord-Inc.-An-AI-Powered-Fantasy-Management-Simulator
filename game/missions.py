"""First mission: A Crown for a Clown."""
from game.state import GameState

initial_state = GameState()


def is_goal(state: GameState) -> bool:
    return state.crown_stolen and state.escaped and state.location == "headquarters"
