# Definition

The simplest case of N-SAT, when there is only one variable in each clause, which is also the trivial case to solve.

# Samples

* $(x_1)$ - trivially satistified iff $x_1$ is $True$
* $(x_1) \land (x_2)$ - trivially satistified iff $x_1$ and $x_2$ is $True$
* $(x_1) \land (\lnot x_1)$ - trivially a  controversial problem: $x_1$ cannot be both $True$ and $False$, hence this is unsatisfiable

# Algorithm

1. Check for contradiction, stop if any, return with no solution
2. Eliminate redundant clauses (same clause appears multiple times)
3. Return the normalized problem which represents the solution

As for the last... each 1-SAT clause represents a solution for the given variable, e.g. the clause, $(x_1)$ can represents the solution, $x_1 = True$. In other words a 1-SAT solution, if there is any, can be represented by 1-SAT clauses, where each variable appears at most in one clause. 

The above then may work for the general case as well. Solutions to an N-SAT problem may be represented by a set of 1-SAT problems, which are free from contradictions and not redundant, where redundant means: 
- both the trivial case when the same 1-SAT appears twice and 
- the less trivial case when it appears with one of its implications (such as e.g. $[(x_1), (x_1 \land x_2)]$ is redundant since, the first solution, $(x_1)$ implies that the second, $(x_1 \land x_2)$ is also a solution. 

So, N-SAT solutions can be represented by (mapped to) 1-SAT problems. Note however this is representation, but semantically they are not equivalent. Clearly if $(x_1)$ is interpreted as a clause then it does not imply $(x_1 \land x_2)$, the opposite is true. So this is a similarity, not an equivalence between the two interpretation equipped with the implication relation. What if we negate one of the implication relations? Does it yield isomorphism?