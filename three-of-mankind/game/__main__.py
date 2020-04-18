import logging

import arcade
from .gamestate import GameState

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "something"

format_string = "%(asctime)s | %(filename)s#%(lineno)d | %(levelname)s | %(message)s"
logging.basicConfig(format=format_string, level=logging.DEBUG)


class Game(arcade.Window):
    """Main game object."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ingame = False
        self.gamestate = None

    def on_update(self, delta_time: float) -> None:
        """Send update event to the gamestate."""
        if not self.ingame:  # Temporarily automatically start the game if it isn't running
            self.start_game()
        if self.gamestate:
            self.gamestate.on_update(delta_time)

    def on_draw(self) -> None:
        """Send draw event to the gamestate."""
        if self.gamestate:
            self.gamestate.on_draw()

    def start_game(self) -> None:
        """Create gamestate and set to the ingame mode."""
        logging.info('New game started')
        self.ingame = True
        self.gamestate = GameState()


# Start game
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
arcade.run()
