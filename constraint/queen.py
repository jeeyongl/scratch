from constraint import *
from icecream import ic

class QueenConstraint(Constraint[int, int]):
    def __init__(self, columns: list(int)):
        super().__init__(columns)
        self.columns = columns

    def satisfied(self, assignment_to_be_tested):
        # dict[column, row]
        for c1, r1 in assignment_to_be_tested.items():


            
        return True
    

if __name__ == '__main__':
    columns = range(1,9) # variables
    rows = {i: list(range(1,9)) for i in columns} # domains

    csp = ConstraintSatisfactionProblem(columns, rows)
    csp.add_constraint(QueenConstraint(columns))
    ic(csp.backtracking_search())