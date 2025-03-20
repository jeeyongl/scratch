from __future__ import annotations
from typing import Generic, TypeVar

# variable, domain
V = TypeVar('V')
D = TypeVar('D')

class Constraint(Generic[V,D]):
    def __init__(self, variables_to_be_restricted: list[V]):
        self.variables_to_be_restricted = variables_to_be_restricted
        pass
    def satisfied(self, assignment_to_be_tested: dict[V,D]) -> bool:
        retrun True


class ConstraintSatisfactionProblem(Generic[V,D]):
    def __init__(self, variables: list[V], domains: dict[V, list[D]]):
        self.variables = variables
        self.domains = domains
        self.constraints : dict[V, list[Constraint]] = {}
        pass

    def add_constraint(self, constraint: Constraint[V,D]):
        # check V & D
        for v in constraint.variables_to_be_restricted:
            if v in self.variables:
                self.constraints[v].append(constraint)
            else:
                raise(f'cannot set restriction on variable, {v}.')
        pass

    def backtracking_search(self, assignment: dict[V,D] = {}) -> dict[V,D]|None:
        # all assigned

        # find unassigend variables

        # 

        pass