"""Legal crown-heist actions; invalid actions return None."""
from dataclasses import replace
from game.state import GameState


def buy_disguise(state: GameState) -> GameState | None:
    if state.location != "headquarters" or state.gold < 30 or "disguise" in state.inventory:
        return None
    return replace(state, gold=state.gold - 30, inventory=state.inventory + ("disguise",))


def travel_to_castle(state: GameState) -> GameState | None:
    if state.location != "headquarters" or state.escaped:
        return None
    return replace(state, location="castle_gate")


def distract_guards(state: GameState) -> GameState | None:
    if state.location != "castle_gate" or state.guards_distracted:
        return None
    return replace(state, guards_distracted=True)


def enter_castle(state: GameState) -> GameState | None:
    if state.location != "castle_gate":
        return None
    if "disguise" not in state.inventory and not state.guards_distracted:
        return None
    return replace(state, location="treasury")


def steal_crown(state: GameState) -> GameState | None:
    if state.location != "treasury" or state.crown_stolen:
        return None
    return replace(state, crown_stolen=True)


def escape_castle(state: GameState) -> GameState | None:
    if state.location != "treasury" or not state.crown_stolen:
        return None
    return replace(state, location="headquarters", escaped=True)


ACTIONS = {
    "buy_disguise": buy_disguise,
    "travel_to_castle": travel_to_castle,
    "distract_guards": distract_guards,
    "enter_castle": enter_castle,
    "steal_crown": steal_crown,
    "escape_castle": escape_castle,
}


def successors(state: GameState):
    """Yield (action name, next state) for all legal actions."""
    for name, action in ACTIONS.items():
        next_state = action(state)
        if next_state is not None:
            yield name, next_state
