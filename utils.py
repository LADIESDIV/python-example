"""Add beer in file."""

import json
from pathlib import Path


def add_beer(response):
    """Add beer in file.

    Args:
        response (json): add beer in file.
    """
    filename = "addBeer.json"
    with Path(filename).open("w") as f:
        json.dump(response.json(), f)
    Path(filename).unlink()


def drink_beer(response):
    """Add beer drink in file.

    Args:
        response (json): add beer drink in file.
    """
    filename = "drinkBeer.json"
    with Path(filename).open("w") as f:
        json.dump(response.json(), f)
    Path(filename).unlink()
