#from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TypeVar


C= TypeVar('C', bound= 'Chromosome')

class Chromosome(ABC):
    def fitness(self) -> float:
        ...
    @classmethod
    def random_instance(self) -> C:
        # *Chromosome.random_instance()
        # @classmethod decorator should be placed before
        ...
    def mutate(self):
        ...
    def crossover(self, other: C) -> tuple[C,C]:
        ...
    
