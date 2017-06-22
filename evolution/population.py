from connect4.agent import MiniMaxAgent
from connect4.game import Connect4Game

from evolution.genetics import mutate_dna

from itertools import combinations
import random

def create_random_population(n):

    return [ MiniMaxAgent() for _ in range(n) ]

def get_fitnesses(population, method='combo'):

    fitnesses = [0 for _ in population]

    if method == 'combo':

        for a, b in combinations(population, 2):

            g = Connect4Game(a, b)
            g.play()

            w = g.get_winner()

            if w == 1:
                fitnesses[population.index(a)] += 1
            elif w == 2:
                fitnesses[population.index(b)] += 1

    elif method == 'reduce':

        indices = list(range(len(population)))

        while len(indices) > 1:

            a_index = random.choice(indices)
            b_index = random.choice(indices)

            if a_index != b_index:

                g = Connect4Game(population[a_index], population[b_index])
                g.play()

                w = g.get_winner()

                if w == 1:
                    fitnesses[a_index] += 1
                    indices.remove(b_index)
                elif w == 2:
                    fitnesses[b_index] += 1
                    indices.remove(a_index)

    return fitnesses

def create_mating_pool(population, fitnesses, norm=True):

    if norm:
        mx = max(fitnesses)
        fitnesses = [ int((f / mx) * 10.0) for f in fitnesses ]

    pool = []

    for i, fitness in enumerate(fitnesses):

        for _ in range(fitness):

            pool.append(population[i])

    return pool

def generate_new_population(pool, n):

    new_pop = []

    while len(new_pop) < n:

        a = random.choice(pool)
        b = random.choice(pool)

        if a != b:
            new_pop.append(MiniMaxAgent(dna=mutate_dna(a.dna, b.dna)))

    return new_pop
