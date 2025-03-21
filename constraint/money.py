from icecream import ic
from constraint import Constraint, ConstraintSatisfactionProblem

class MoneyConstraint(Constraint):
    def __init__(self, variables_letters: list[str]):
        super().__init__(variables_letters)
        self.variables_letters = variables_letters

    def satisfied(self, assignment_to_be_tested):
        # assignment is a form of {variable: domain}

        # checking duplicates
        if len(set(assignment_to_be_tested.values())) < len(assignment_to_be_tested):
            return False
        
        # all letters assigned
        if len(assignment_to_be_tested) == len(self.variables_letters):
            s: int = assignment_to_be_tested['S']
            e: int = assignment_to_be_tested['E']
            n: int = assignment_to_be_tested['N']
            d: int = assignment_to_be_tested['D']
            m: int = assignment_to_be_tested['M']
            o: int = assignment_to_be_tested['O']
            r: int = assignment_to_be_tested['R']
            y: int = assignment_to_be_tested['Y']

            send = s * 1000 + e * 100 + n * 10 + d
            more = m * 1000 + o * 100 + r * 10 + e
            money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
            return (send + more) == money
        
        return True # intermediates should pass the test

if __name__ == '__main__':
    variable_letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
    domain_digits = {l: list(range(0, 10)) for l in variable_letters}
    domain_digits['M'] = [1]

    csp = ConstraintSatisfactionProblem(variable_letters, domain_digits)
    #ic(variable_letters, domain_digits)
    csp.add_constraint(MoneyConstraint(variable_letters)) # should consider all letters.

    ic(solution := csp.backtracking_search())
