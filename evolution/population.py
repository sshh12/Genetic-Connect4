from connect4.agent import MiniMaxAgent
from connect4.game import Connect4Game

from evolution.genetics import mutate_dna

from itertools import combinations
import random

def create_random_population(n):
    """Generates population of random agents with size n"""
    return [ MiniMaxAgent() for _ in range(n) ]

def get_fitnesses(population, method='combo'):
    """
    Calculates the fitnesses of the population.

    Combo will put every agent against every other agent and tally wins. Reduce
    will loop through the population and discard those that lose while keeping the
    winners in the pool until only one winner remains.

    Parameters
    ----------
    population : list of MiniMaxAgent
        The current population
    method : str
        The method of evaluation

    Returns
    -------
    list of int
        The fitness values for each member of the population
    """
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
    """
    Generate a mating pool

    This will create a new population proportional to the fitnesses
    of the original population. The pool will the be used as the basis
    for generating the next generation.

    Parameters
    ----------
    population : list of MiniMaxAgent
        The current population
    fitnesses : list of int
        The fitness values for each member of the population
    norm : bool
        True will apply basic normilization to the fitness values before
        creating the pool

    Returns
    -------
    list of MiniMaxAgent
        The mating pool with the frequency of each agent proportional to
        its fitness
    """
    if norm:
        mx = max(fitnesses)
        fitnesses = [ int((f / mx) * 10.0) for f in fitnesses ]

    pool = []

    for i, fitness in enumerate(fitnesses):

        for _ in range(fitness):

            pool.append(population[i])

    return pool

def generate_new_population(pool, n):
    """
    Creates the next population

    This will randomly choose agents from the population to mate and add
    their offspring to the next population. The offsprings dna is based on
    the dna of the parents selected with some additional genetic mutation.

    Parameters
    ----------
    pool : list of MiniMaxAgent
        The mating pool
    n : int
        The size of the next population
    """
    new_pop = []

    while len(new_pop) < n:

        a, b = random.choice(pool), random.choice(pool)

        if a != b:
            new_pop.append(MiniMaxAgent(dna=mutate_dna(a.dna, b.dna)))

    return new_pop
