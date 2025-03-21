from icecream import ic
from constraint import Constraint, ConstraintSatisfactionProblem

class QueenConstraint(Constraint[int, int]):
    def __init__(self, columns: list[int]): # need all 8 columns for checking the violation
        super().__init__(columns)
        self.columns = columns

    def satisfied(self, assignment_to_be_tested):
        # checking {8 X column: row}
        for c1, r1 in assignment_to_be_tested.items():
            for c2 in range(c1 + 1, len(self.columns) + 1):
                if c2 in assignment_to_be_tested:
                    r2 = assignment_to_be_tested[c2] 
                    if r1 == r2:
                        return False
                    if abs(c1 - c2) == abs(r1 - r2):
                        return False
        return True

if __name__ == '__main__':
    columns = range(1,9) # variables
    rows = {i: list(range(1,9)) for i in columns} # domains

    csp = ConstraintSatisfactionProblem(columns, rows)
    csp.add_constraint(QueenConstraint(columns)) # should consider all columns.
    ic(solution := csp.backtracking_search())
