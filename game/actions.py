from dataclasses import replace
from game.state import GameState

def buy_disguise(state: GameState) -> GameState | None:
    if state.gold < 30:
        return None

    if "disguise" in state.inventory:
        return None
    
    return replace(state, 
                   gold=state.gold - 30, 
                   inventory=state.inventory + ("disguise",)
    )