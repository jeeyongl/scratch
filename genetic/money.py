from genetic import GeneticAlgorithm
from chromosome import Chromosome

class MoneyChromosome(Chromosome):
    
    
    
    pass





if __main__ == '__main__':
    population = [MoneyChromosome.random_instance() for _ in range(10)]
    ga= GeneticAlgorithm(population)
    ic(ga.run())