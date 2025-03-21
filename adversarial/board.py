from __future__ import annotations
from typing import NewType, TypeVar, Generic
from abc import ABC, abstractmethod

Move = NewType('Move', int)
P = TypeVar('P', bound= 'Piece')
B = TypeVar('B', bound= 'Board')

class Piece(ABC, Generic[P]):
    @property
    @abstractmethod
    def opposite(self) -> P:
        ...

class Board(ABC, Generic[P, B]):
    @abstractmethod
    def turn(self) -> P:
        ...

    @abstractmethod
    def move(self, location: Move) -> B:
        ...

    @abstractmethod
    def legal_moves(self) -> list[Move]:
        ...

    @abstractmethod
    def is_win(self) -> bool:
        ...

    def is_draw(self) -> bool:
        return not self.is_win() and len(self.legal_moves()) == 0 
    
    @abstractmethod
    def evaluate(self, player: P) -> float:
        ...

    