from __future__ import annotations
from typing import Generic, TypeVar
from copy import deepcopy

# variable, domain
V = TypeVar('V')
D = TypeVar('D')

class Constraint(Generic[V,D]):
    def __init__(self, variables_to_be_restricted: list[V]):
        self.variables_to_be_restricted = variables_to_be_restricted
        pass
    def satisfied(self, assignment_to_be_tested: dict[V,D]) -> bool:
        return True


class ConstraintSatisfactionProblem(Generic[V,D]):
    def __init__(self, variables: list[V], domains: dict[V, list[D]]):
        self.variables = variables
        self.domains = domains
        self.constraints : dict[V, list[Constraint]] = {}

    def add_constraint(self, constraint: Constraint[V,D]):
        # check V & D
        for v in constraint.variables_to_be_restricted:
            if v in self.variables:
                self.constraints.setdefault(v, []).append(constraint)
            else:
                raise LookupError(f'cannot set restriction on variable, {v}.')

    # maximum number of backtracking : len(V)*len(D)
    def backtracking_search(self, assignment: dict[V,D] = {}) -> dict[V,D]|None:
        # all assigned
        if len(self.variables) == len(assignment):
            return assignment
        # find unassigend variables
        unassigned_variables = [v for v in self.variables if v not in assignment]
        checking_variable = unassigned_variables[0]

        for domain_value in self.domains[checking_variable]:
            # assign one more variable here
            copied_assignment = deepcopy(assignment)
            copied_assignment[checking_variable] = domain_value

            # check constraints for checking_variable
            if all(constraint.satisfied(copied_assignment) for constraint in self.constraints[checking_variable]):
                # if ok, then recursive call, otherwise next possible domain
                result = self.backtracking_search(copied_assignment)
                if result is not None: 
                    return result # recursive return of found assignment

        return None
