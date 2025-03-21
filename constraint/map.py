from icecream import ic
from constraint import Constraint, ConstraintSatisfactionProblem

class MapConstraint(Constraint[str, str]):
    def __init__(self, variable1, variable2):
        super().__init__([variable1, variable2])
        self.variable1 = variable1
        self.variable2 = variable2

    def satisfied(self, assignment_to_be_tested):
        # assignment is a form of {variable: domain}
        if (self.variable1 not in assignment_to_be_tested 
            or 
            self.variable2 not in assignment_to_be_tested):
            return True
        return assignment_to_be_tested[self.variable1] != assignment_to_be_tested[self.variable2]
            
if __name__ == '__main__':
    variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    domains = {v: ['a', 'b', 'c', 'd'] for v in variables}
    problem = ConstraintSatisfactionProblem(variables, domains)
    problem.add_constraint(MapConstraint('A', 'B'))
    problem.add_constraint(MapConstraint('B', 'C'))
    problem.add_constraint(MapConstraint('C', 'D'))
    problem.add_constraint(MapConstraint('D', 'E'))
    problem.add_constraint(MapConstraint('E', 'F'))
    problem.add_constraint(MapConstraint('F', 'G'))
    problem.add_constraint(MapConstraint('G', 'H'))
    problem.add_constraint(MapConstraint('H', 'I'))
    problem.add_constraint(MapConstraint('I', 'J'))
    problem.add_constraint(MapConstraint('J', 'K'))
    problem.add_constraint(MapConstraint('K', 'L'))
    problem.add_constraint(MapConstraint('L', 'M'))
    problem.add_constraint(MapConstraint('M', 'N'))
    problem.add_constraint(MapConstraint('N', 'O'))
    problem.add_constraint(MapConstraint('O', 'P'))
    problem.add_constraint(MapConstraint('P', 'Q'))
    problem.add_constraint(MapConstraint('Q', 'R'))
    problem.add_constraint(MapConstraint('R', 'S'))
    problem.add_constraint(MapConstraint('S', 'T'))
    problem.add_constraint(MapConstraint('T', 'U'))
    problem.add_constraint(MapConstraint('U', 'V'))
    problem.add_constraint(MapConstraint('V', 'W'))
    problem.add_constraint(MapConstraint('W', 'X'))
    problem.add_constraint(MapConstraint('X', 'Y'))
    problem.add_constraint(MapConstraint('Y', 'Z'))
    ic(problem.backtracking_search())