from connect4.tools import *
import numpy as np

class Connect4Game(object):
    """
    Connect4 game

    This class will create a game between two agents.
    """
    def __init__(self, pA, pB, size=(6, 7)):
        """
        Creates the game

        Parameters
        ----------
        pA, pB : MiniMaxAgent or HumanAgent
            The 2 players/agents
        size : tuple of int
            The size of the board
        """
        self.playerA = pA
        self.playerB = pB

        self.width, self.height = size

        self.playerA.set_id(1)
        self.playerB.set_id(2)

        self.board = np.zeros(size, dtype=np.uint8)

    def _get_scores(self, id_):

        return [most_vertical(self.board, id_),
                most_horizontal(self.board, id_),
                most_inc_diagonal(self.board, id_),
                most_dec_diagonal(self.board, id_)]

    def _get_player(self, id_):

        if id_ == 1:
            return self.playerA
        elif id_ == 2:
            return self.playerB

    def _play_move(self, id_, col):

        if self.board[0, col] == 0:

            if self.board[-1, col] == 0:

                self.board[-1, col] = id_

            else:

                self.board[np.argmax(self.board > 0, axis=0)[col] - 1, col] = id_


    def get_winner(self):
        """
        Gets the winner of the game

        Returns
        -------
        int
            1 for player A, 2 for player B, 0 for no winner/tie
        """
        if 4 in self._get_scores(1):
            return 1
        elif 4 in self._get_scores(2):
            return 2
        else:
            return 0

    def play(self):
        """
        Plays the game to completion

        This will loop through each round until an agent has won or
        a tie has occured.

        Note
        ----
        Always starts will player A
        """
        turn = 1

        while not self.get_winner():

            if self.board[0, :].min() != 0:
                break

            player = self._get_player(turn)

            move = player.get_move(self.board)

            self._play_move(turn, move)

            turn ^= 3
