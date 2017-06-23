import random

def mutate_dna(a, b, mutate_thres=.4):
    """
    Creates a strand of dna based on the dna of 2 parents.

    Parameters
    ----------
    a, b : list of int
        The dna of each parent
    mutate_thres : float
        The chance of a mutation

    Returns
    -------
    list of int
        The new strand of dna
    """
    i = random.randrange(0, len(a))

    dna = a[:i] + b[i:]

    while random.random() < mutate_thres:

        m = random.randrange(1, len(a))
        dna[m] += random.randrange(-20, 20)

    return dna
