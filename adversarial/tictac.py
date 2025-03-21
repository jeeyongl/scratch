from __future__ import annotations
from board import Board, Move, Piece
from dataclasses import dataclass
from enum import Enum

class TTTPiece(Piece, Enum):
    X : str = "X"
    O : str = "O"
    E : str = " "

    @property
    def opposite(self) -> TTTPiece:
        match self:
            case TTTPiece.X: return TTTPiece.O
            case TTTPiece.O: return TTTPiece.X
            case TTTPiece.E: return TTTPiece.E
    def __str__(self) -> str:
        return self.value

piece = TTTPiece.X
   