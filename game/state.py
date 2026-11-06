from dataclasses import dataclass

@dataclass(frozen=True)
class GameState:
    gold: int = 100
    location: str = "headquarters"
    inventory: tuple[str, ...] = ()
    guards_distracted: bool = False
    crown_stolen: bool = False
    escaped: bool = False