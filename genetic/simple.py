from chromosome import Chromosome
from genetic import GeneticAlgorithm
from icecream import ic
from random import randrange, random

class SimpleChromosome(Chromosome):
    def __init__(self, x, y):
        self.x= x
        self.y= y

    def fitness(self):
        return -self.x**2 + 2*self.x - self.y # maximize

    @classmethod
    def random_instance(cls):
        return cls(randrange(10), randrange(10))

    def mutate(self):
        self.x = (self.x + 1) if random() > 0.5 else (self.x - 1)
        self.y = (self.y + 1) if random() > 0.5 else (self.y - 1)
            
    def crossover(self, other):
        if random() < 0.1:
            self.x, other.x = other.x, self.x
        if random() < 0.1:
            self.y, other.y = other.y, self.y
        return self, other

if __name__ == '__main__':
    population = [SimpleChromosome.random_instance() for _ in range(10)]
    ga= GeneticAlgorithm(population)
    ic(ga.run())