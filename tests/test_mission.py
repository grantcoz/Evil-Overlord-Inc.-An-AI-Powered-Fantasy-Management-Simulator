from game.state import GameState
from game.actions import (buy_disguise, travel_to_castle, distract_guards,
                          enter_castle, steal_crown, escape_castle, successors)
from game.missions import initial_state, is_goal


def test_disguise_route():
    state = buy_disguise(initial_state)
    assert state.gold == 70
    for action in (travel_to_castle, enter_castle, steal_crown, escape_castle):
        state = action(state)
        assert state is not None
    assert is_goal(state)


def test_distraction_route():
    state = initial_state
    for action in (travel_to_castle, distract_guards, enter_castle, steal_crown, escape_castle):
        state = action(state)
        assert state is not None
    assert is_goal(state)
    assert state.gold == 100


def test_illegal_actions():
    assert enter_castle(initial_state) is None
    assert steal_crown(initial_state) is None
    assert escape_castle(initial_state) is None
    assert buy_disguise(GameState(gold=10)) is None
    assert enter_castle(GameState(location="castle_gate")) is None


def test_search_ready_states():
    assert len(list(successors(initial_state))) == 2
    assert isinstance(hash(initial_state), int)
