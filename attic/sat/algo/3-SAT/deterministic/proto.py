# Deterministic Thread-Based 3-SAT Solver Prototype

from itertools import combinations, product
from typing import List, Tuple, Dict, Set

Literal = Tuple[str, bool]  # (variable name, is_positive)
Clause = List[Literal]
Formula = List[Clause]
Assignment = Dict[str, bool]


def literal_negation(literal: Literal) -> Literal:
    return (literal[0], not literal[1])


def literals_conflict(a: Literal, b: Literal) -> bool:
    return a[0] == b[0] and a[1] != b[1]


def clause_satisfied(clause: Clause, assignment: Assignment) -> bool:
    for var, is_pos in clause:
        if var in assignment:
            if assignment[var] == is_pos:
                return True
    return False


def clause_contradicted(clause: Clause, assignment: Assignment) -> bool:
    for var, is_pos in clause:
        if var not in assignment:
            return False  # clause is still neutral
        if assignment[var] == is_pos:
            return False  # clause is satisfied
    return True


def validate(formula: Formula, assignment: Assignment) -> bool:
    print("Validating assignment:", assignment)
    for clause in formula:
        if not clause_satisfied(clause, assignment):
            print("Clause not satisfied:", clause)
            return False
    return True


def find_generator_clause(formula: Formula, a: Literal, b: Literal, assigned_vars: Set[str], used_clauses: Set[int]) -> Tuple[int, Literal]:
    for i, clause in enumerate(formula):
        if i in used_clauses:
            continue
        if a not in clause or b not in clause:
            continue
        if clause_satisfied(clause, {a[0]: a[1], b[0]: b[1]}):
            continue
        for lit in clause:
            if lit != a and lit != b and lit[0] not in assigned_vars:
                print(f"Generator clause found (index {i}): {clause} for pair {a}, {b}, adding literal {lit}")
                return i, lit
    return -1, None


def build_thread(formula: Formula, init_pair: Tuple[Literal, Literal], exclude_indices: Set[int]) -> Tuple[str, Assignment]:
    print("\n--- Building thread for pair:", init_pair, "---")
    sequence = [init_pair[0], init_pair[1]]
    assignment = {init_pair[0][0]: init_pair[0][1], init_pair[1][0]: init_pair[1][1]}
    used_pairs = set()
    used_clauses = set(exclude_indices)

    while True:
        extended = False
        for a, b in combinations(sequence, 2):
            pair_id = tuple(sorted([a, b]))
            if pair_id in used_pairs:
                continue
            used_pairs.add(pair_id)

            ci, new_lit = find_generator_clause(formula, a, b, set(assignment.keys()), used_clauses)
            if ci == -1:
                continue
            used_clauses.add(ci)
            assignment[new_lit[0]] = new_lit[1]
            sequence.append(new_lit)
            print(f"Extended with: {new_lit}, from clause {ci}")
            extended = True
            break
        if not extended:
            print("No more extensions possible.")
            break

    if validate(formula, assignment):
        print("Thread result: SAT")
        return "SAT", assignment
    elif any(clause_contradicted(cl, assignment) for cl in formula):
        print("Thread result: UNSAT due to contradiction.")
        return "UNSAT", assignment
    else:
        print("Thread result: TBD (partial solution)")
        return "TBD", assignment


def solve_3sat(formula: Formula) -> Tuple[str, Assignment]:
    has_tbd = None
    for i, j in combinations(range(len(formula)), 2):
        for l1, l2 in product(formula[i], formula[j]):
            if literals_conflict(l1, l2):
                continue
            if l1 == l2:
                continue  # optional: skip (x, x)
            print(f"Trying pair: {l1}, {l2} from clauses {i}, {j}")
            status, assign = build_thread(formula, (l1, l2), exclude_indices={i, j})
            if status == "SAT":
                print("Final decision: SAT")
                return status, assign
            elif status == "TBD" and has_tbd is None:
                has_tbd = (status, assign)
    if has_tbd:
        print("Final decision: TBD (partial solution exists)")
        return has_tbd
    print("Final decision: UNSAT")
    return "UNSAT", {}


# Example formula to test (user can later replace this with random or handcrafted samples)
example_formula: Formula = [
    [("x1", True), ("x2", False), ("x3", True)],
    [("x1", False), ("x2", True), ("x4", False)],
    [("x2", True), ("x3", False), ("x5", True)],
    [("x1", True), ("x3", False), ("x5", False)],
    [("x1", False), ("x4", False), ("x5", True)],
    [("x1", True), ("x2", True), ("x5", False)],
    [("x2", False), ("x4", True), ("x5", True)],
    [("x3", True), ("x4", False), ("x5", False)],
    [("x1", True), ("x2", True), ("x4", True)],
    [("x1", True), ("x3", True), ("x4", False)],
    [("x1", False), ("x2", False), ("x3", False)],
    [("x1", False), ("x4", False), ("x5", False)]
]

if __name__ == "__main__":
    result, final_assignment = solve_3sat(example_formula)
    print("\nResult:", result)
    print("Assignment:", final_assignment)
