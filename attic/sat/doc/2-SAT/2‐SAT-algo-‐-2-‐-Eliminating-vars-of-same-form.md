# Eliminating variables appearing in the same form in every clause

Stub

## Sample

Take the following sample where we can study both cases:

$$
(x_1 \lor x_2 \lor \lnot x_4) \land (x_1 \lor x_3) \land (\lnot x_3 \lor x_4)
$$

Here 

|variable|appearance|comment|
|--------|----------|-------|
|$x_1$   |same      |variable $x_1$ appears in 2 clauses and each appearance is in the same form: $x_1$|
|$x_2$   |same      |variable $x_2$ appears in only one clause, hence trivially it is "always" in the same form: $x_2$|
|$x_3$   |different |variable $x_3$ appears in two clauses but in different forms, both in not negated form, $x_3$ and in negated form, $\lnot x_3$|
|$x_4$   |different |variable $x_4$ is similar to $x_3$: appears in two clauses but in different forms|

## Definition
TODO

## Method

Such variables can be eliminated by setting it to $True$ (or $False$ depending on their appearences) in order to satisfy their related clauses. The reduced problem is not equivalent to the original, but it implies the original. That is: if there is a solution to the original problem then there is a solution to the simpler, reduced one. This elimination hence can reduce the search space by reducing to an equivalent problem in respect with the narrower problem: "is there a solution? if yes then find at least one solution, if not prove it", but it may not find all solutions.

## Algorithm
TODO

1. Check variable appereances with same form.
2. Reduce the original problem by substituting such variables with their appropriate values in each clauses where they appear and drop those clauses
3. Return the partial solutions and the reduced problem and... also the other cases which may contain valid solutions, but "left out"

## Sample continued

Take the original sample, it will yield the following:

- reduced: 
  - partial solution: $(x_1 \land x_2)$
  - reduced 2-SAT: $(\lnot x_3 \lor x_4)$
- left out: $(\lnot x_1 \lor \lnot x_2) \land (x_1 \lor x_2 \lor \lnot x_4) \land (x_1 \lor x_3) \land (\lnot x_3 \lor x_4)$

That is we get a simplified problem to further search solution at and a more complex one to leave out. Do we really have to leave it out? Even though it is more complex, the number of clauses only increased one and it is already in the form of reduced 2-SAT, every variable has different appearences.