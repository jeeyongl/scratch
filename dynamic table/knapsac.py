from dataclasses import dataclass
import numpy as np
from icecream import ic

@dataclass(frozen= True)
class Item:
    name: str
    weight: int
    value: float

items: list[Item] =     [Item("television", 50, 500),
                        Item("candlesticks", 2, 300),
                        Item("stereo", 35, 400),
                        Item("laptop", 3, 1000),
                        Item("food", 15, 50),
                        Item("clothing", 20, 800),
                        Item("jewelry", 1, 4000),
                        Item("books", 100, 300),
                        Item("printer", 18, 30),
                        Item("refrigerator", 200, 700),
                        Item("painting", 10, 1000)]

max_capacity = 50
table= np.zeros((len(items)+1, max_capacity +1), dtype= float)
ic(table.shape)

# one per item
for i , item in enumerate(items):
    for j in range(1, max_capacity + 1):
        previous = table[i,j]
        if j >= item.weight:
            table[i+1,j] = max(previous, table[i,j-item.weight] + item.value)
        else:
            table[i+1, j] = previous

# backtracking
solution = []
current_capacity = max_capacity

for i in range(len(items), 0, -1):
    if (current_capacity >= 0 
        and 
        table[i, current_capacity] != table[i-1, current_capacity]
        ):

        solution.append(items[i-1])
        current_capacity -= items[i-1].weight


ic ( sum(item.value for item in solution) ) 
ic ( sum(item.weight for item in solution) )
ic (solution)