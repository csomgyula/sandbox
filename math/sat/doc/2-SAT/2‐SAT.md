# Definition

2-SAT is a special case of the [SAT problem](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem), where each clause has at most 2 variables. 

# Samples

- $(x_1) \land (\neg x_1 \lor x_2)$, which is satisfiable but only in one way: $x_1 = True, x_2 = True$
- $(x_1) \land (\neg x_1 \lor x_2) \land (\neg x_1 \lor \neg x_2)$, which is unsatisfiable

# Complexity

Unlike 3-SAT or the general N variable case, which is [NP-complete](https://en.wikipedia.org/wiki/NP-completeness), 2-SAT is known to have [polynomial](https://en.wikipedia.org/wiki/Time_complexity#Polynomial_time) algo

# References

- [https://en.wikipedia.org/wiki/Boolean_satisfiability_problem](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem)
- [https://en.wikipedia.org/wiki/NP-completeness](https://en.wikipedia.org/wiki/NP-completeness)
- https://en.wikipedia.org/wiki/Time_complexity#Polynomial_time