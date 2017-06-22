import random

def mutate_dna(a, b, mutate_thres=.4):

    i = random.randrange(0, len(a))

    dna = a[:i] + b[i:]

    while random.random() < mutate_thres:

        m = random.randrange(1, len(a))
        dna[m] += random.randrange(-20, 20)

    return dna
