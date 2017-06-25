# Genetic Connect4

Using evolution to evolve a minimax connect4 AI.

## Dependencies
* [NumPy](http://www.numpy.org/)

## What
As a twist to the connect4 algorithms I've written earlier, this project uses
the basic principles of genetics and evolution to create the best minimax
heuristic for playing connect4 given predefined features. First a generation
of agents (Connect4 bots) with random DNA is created. A function
that calculates the fitness (how well each agent performs) is then used to
determine the probability that an agent will produce an offspring. Then a
second generation is created from the original agents along with some mutation.
The process repeats with each iteration improving the general performance
of the population.

## Usage

#### Install
1. ```git clone https://github.com/sshh12/Genetic-Connect4.git```
2. ```pip install numpy```

#### Running
1. ```python main.py```
