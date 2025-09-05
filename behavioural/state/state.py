""" Implementation State Design Pattern """

from __future__ import annotations
from abc import ABC, abstractmethod
import random



class Game:
    """ Implement Game class """
    def __init__(self):
        self.state = WelcomeScreenState(self)

    def change_state(self, state: State):
        """ change state method """
        self.state = state



class State(ABC):
    """ Abstract State class to manage change states """
    def __init__(self, game: Game):
        self.game = game
        print(f"Curently in {self} state")

    @abstractmethod
    def on_welcome_screen(self):
        """ Not Implemented """

    @abstractmethod
    def on_playing(self):
        """ Not Implemented """

    @abstractmethod
    def on_break(self):
        """ Not Implemented """

    @abstractmethod
    def on_end_game(self):
        """ Not Implemented """


class WelcomeScreenState(State):
    """
    Welcome Screen State
    Its the first step of the game
    """
    def on_welcome_screen(self):
        """ current state """
        print(f"Currently on welcome screen")

    def on_playing(self):
        """ available to go to play state """
        self.game.change_state(PlayingState(self.game))

    def on_break(self):
        """ denied to go to break state """
        print("From Welcome to break not allowed")

    def on_end_game(self):
        """ denied to to to end game state """
        print("From Welcome to end game not allowed")


class PlayingState(State):
    """
    Playing State
    Second Step of the game
    """
    def on_welcome_screen(self):
        """ denied to go to welcome screen state """
        print("From playing to welcome screen not allowed")

    def on_playing(self):
        """ current state """
        print("Currently Playing")

    def on_break(self):
        """ available to go to break state """
        self.game.change_state(BreakState(self.game))

    def on_end_game(self):
        """ available to go to endgame state """
        self.game.change_state(EndGameState(self.game))


class BreakState(State):
    """
    BreakState
    Third Step of the game
    """
    def on_welcome_screen(self):
        """ Denied to go to welcome screen state """
        print("From break to welcome not allowed")

    def on_playing(self):
        """ available to go to plying state """
        self.game.change_state(PlayingState(self.game))

    def on_break(self):
        """ current state """
        print("Currently on break")

    def on_end_game(self):
        """ Denied to go to Endgame state """
        print("From Break to EndGame not allwed")


class EndGameState(State):
    """
    EndGame State
    Last state of the game
    """
    def on_welcome_screen(self):
        """ Available to go to welcome screen state """
        self.game.change_state(PlayingState(self.game))

    def on_playing(self):
        """ Denied to go to playing state """
        print("From end game to playing not allowed")

    def on_break(self):
        """ Denied to go to break state """
        print("From endgame to break not allowed")

    def on_end_game(self):
        """ Current state """
        print("Currently in EndGame")


# Usage
if __name__ == "__main__":
    game = Game()

    for i in range(5):
        state = random.randrange(0, 4)
        print(state)
        if state == 0:
            print("Move to Welcome")
            game.state.on_welcome_screen()
        elif state == 1:
            print("Move to playing")
            game.state.on_playing()
        elif state == 2:
            print("Move to break")
            game.state.on_break()
        elif state == 3:
            print("Move to end game")
            game.state.on_end_game()
