"""Compose a transparent character sprite over a location background."""
from pathlib import Path
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def render_scene(
    character="archibald",
    location="wizard_tower",
    expression="neutral",
    x_position=0.01,
):
    background_path = PROJECT_ROOT / "assets" / "backgrounds" / f"{location}.png"
    sprite_path = PROJECT_ROOT / "assets" / "characters" / character / f"{expression}.png"

    background = Image.open(background_path).convert("RGBA")
    sprite = Image.open(sprite_path).convert("RGBA")

    target_height = int(background.height * 0.94)
    ratio = target_height / sprite.height

    sprite = sprite.resize(
        (round(sprite.width * ratio), target_height),
        Image.Resampling.LANCZOS,
    )

    x = int(background.width * x_position)
    y = background.height - sprite.height

    background.alpha_composite(sprite, (x, y))

    return background.convert("RGB")
