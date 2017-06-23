from connect4.tools import *

import numpy as np
import random

class BaseAgent(object):
    """
    Base Agent Class
    """
    def __init__(self):
        pass

    def set_id(self, id_):
        self.id_ = id_

    def get_move(self, board):
        pass

class HumanAgent(BaseAgent):
    """
    Agent that gets its move from user input
    """
    def get_move(self, board):

        print(board)

        return int(input(' Col > '))

class MiniMaxAgent(BaseAgent):
    """
    Agent that uses minimax and heuristic based on dna
    """
    def __init__(self, dna=None):
        """
        Creates a new Agent

        Note
        ----
        If dna is not provided it is randomly generated.
        """
        if not dna:
            self.dna = [ random.randrange(2, 8) ]
            self.dna.extend([ random.randrange(-20, 300) for _ in range(14) ])
        else:
            self.dna = dna

        self.depth = self.dna[0]

    def _next_row(self, board, col):

        if board[-1, col] == 0:
            return board.shape[0] - 1
        else:
            return np.argmax(board > 0, axis=0)[col] - 1

    def get_move(self, board):

        best, _ = max(self._get_moves(board), key=lambda v:v[1])
        return best

    def _get_moves(self, board):

        for col in range(board.shape[1]):

            if board[0, col] == 0:

                row = self._next_row(board, col)

                board[row, col] = self.id_

                score = self._alphabeta(board, 0, MIN, MAX, False)

                board[row, col] = 0

                yield col, score

    def _get_points(self, board, id_):

        return [most_vertical(board, id_),
                most_horizontal(board, id_),
                most_inc_diagonal(board, id_),
                most_dec_diagonal(board, id_)]

    def _eval_board(self, board, depth=0):

        points = self._get_points(board, self.id_)
        enemy_points = self._get_points(board, self.id_ ^ 3)

        if 4 in enemy_points:
            return MIN + depth * 20
        elif 4 in points:
            return MAX - depth * 20

        score = (sum(points) * self.dna[1] +
                points.count(3) * self.dna[2] +
                points.count(2) * self.dna[3] +
                points[0] * self.dna[4] +
                points[1] * self.dna[5] +
                points[2] * self.dna[6] +
                points[3] * self.dna[7])

        enemy_score = (sum(enemy_points) * self.dna[8] +
                enemy_points.count(3) * self.dna[9] +
                enemy_points.count(2) * self.dna[10] +
                enemy_points[0] * self.dna[11] +
                enemy_points[1] * self.dna[12] +
                enemy_points[2] * self.dna[13] +
                enemy_points[3] * self.dna[14])

        return score - enemy_score

    def __repr__(self):
        return str(self.dna)

    def _alphabeta(self, board, depth, alpha, beta, maximize):

        if depth == self.depth:

            return self._eval_board(board, depth)

        elif maximize:

            v = MIN
            for col in range(board.shape[1]):

                if board[0, col] == 0:

                    row = self._next_row(board, col)

                    board[row, col] = self.id_

                    v = max(v, self._alphabeta(board, depth + 1, alpha, beta, False))

                    board[row, col] = 0

                    alpha = max(alpha, v)

                    if beta <= alpha:
                        break

        else:

            v = MAX
            for col in range(board.shape[1]):

                if board[0, col] == 0:

                    row = self._next_row(board, col)

                    board[row, col] = self.id_ ^ 3

                    v = min(v, self._alphabeta(board, depth + 1, alpha, beta, True))

                    board[row, col] = 0

                    beta = min(alpha, v)

                    if beta <= alpha:
                        break

        return v
