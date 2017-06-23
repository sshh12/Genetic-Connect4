from connect4.agent import MiniMaxAgent, HumanAgent
from connect4.game import Connect4Game

from evolution.population import create_random_population, get_fitnesses, create_mating_pool, generate_new_population

def play_vs_ai():
    """Plays a basic game vs the ai"""
    a = HumanAgent()
    b = MiniMaxAgent()

    g = Connect4Game(a, b)
    g.play()

def train(generations=200, n=100):
    """
    Evolves population of MiniMaxAgent

    Parameters
    ----------
    generations : int
        The number of generations
    n : int
        The size of the population
    """
    population = create_random_population(n)

    for g in range(generations):

        fitnesses = get_fitnesses(population, method='reduce')

        for i, p in enumerate(population):
            print(fitnesses[i], p.dna)
        print()

        pool = create_mating_pool(population, fitnesses)

        population = generate_new_population(pool, n)


if __name__ == '__main__':
    train()
