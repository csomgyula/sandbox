stub

N-SAT is the unrestricted case when the number of variables is clauses is not restricted. 

# Reduction to 3-SAT
A main result here is that every N-SAT problem can be reduced to 3-SAT. 

## Case of one clause

In this case without loss of generality we can assume that each variable is in positive form, $(x_1 \lor x_2 \lor ... \lor x_n)$. Otherwise, if we have negative form(s), say  $(\lnot x_1 \lor x_2 \lor ... \lor x_n)$ then we replace the original variable(s), this case $x_1$ with negated form(s), this case $x_1' = \lnot x_1$. This then yields an equivalent problem, this case $(x_1' \lor x_2 \lor ... \lor x_n)$ which does not have negative forms. Hence logically they are equivalent, however for human brain this simple form is more visible. It is kinda proof technique, maybe less important to a computer program (?).

### Simplest case of 4 variables

Lets see the simplest case first:

$$
x_1 \lor x_2 \lor x_3 \lor x_4
$$

The task is to rewrite this to a SAT-3 problem, where each clause has at most 3 variables. 

Stub

$$
(\lnot case \lor x_1 \lor x_2)
$$

$$
\land
$$

$$
(case \lor x_3 \lor x_4) 
$$

- The main idea is to program the "divide and conqueer" principle into SAT by introducing a new variable. In the [basic algorithm](./2%E2%80%90SAT-algo:-0.-Basic-algo-by-substitution) we already saw that similar is possible in the opposite direction, we reverse it:
- Here $case$, the new variable can be thought of representing the case of $x_1 \lor x_2$ and $\neg case$ its opposite which implies $x_3 \lor x_4$. Somewhat we "code" the "divison" through a new variable into the SAT problem.

## Case of more variables

- If there are more variables we apply the above "divide and conqueer" by recursively halving the number of variables until we reach 3-SAT. We cannot go further because applying the method to 3-SAT will result in a new 3-SAT (more specifically a 3-SAT plus a 2-SAT).

### Ideas/questions: 

- This method will yield a tree-like division of variables/clauses with a depth of $\approx log\ n$, where $n$ is the number of variables. TODO: lets count it exactly and analyze the structure more closely. 
- It seems that , these freshly introduced new variables, $cases$ somewhat gives us a binary-like representation of the satisfying cases of the original clause. TODO: lets analyze it further.
- An interesting question is to reverse the operation: find such variables in a 3-SAT which represents such divisions. Can we? What are they like? That is lets reverse the method and instead of reducing the number of variables in each clause down to 3, lets reduce the number of variables/clauses by letting the number of vars grow in clauses. Until when can we do it? How N-SAT problems look like which cannot be reduced further in this way? For instance: 
- If a variable (say $c$) appears only in two clauses (in both in self and negated form): $(c \lor x) \land (\neg c \lor y)$ then this variable can be interpreted as a case variable and the two clauses can be collapsed into one: $(c\ \lor x)\ \land (\neg\ c\ \lor y)\ \iff\ (c = y) \land (\ x\ \lor\ y)$ where $\iff$ means not the logical equivalence, but equi-satisfiability, e.g. the former can be satisfied iff the latter.

## Case of more clauses

- We apply the above method to each clause

# Some related ideas

- Shall we extend/adapt divide and conquer to this case? when there can be overlapping among partitions..., but it is noproblem... Or:
- What if we extend Boolean values in the SAT domain to 3-valued variables? which besides True and False can have Any value as well. Where $Any$ means that a variable's value is irrelevant, because the other variables already satisfies the problem. Something like this:

|Formula                         |Value|Meaning                                     |
|--------------------------------|-----|--------------------------------------------|
|$Any$                           |$Any$|Value is irrelevant for satisfying the problem, can be any |
|$\lnot Any$                     |$Any$|If a formula is irrelevant, its negate, $\lnot$ too  |
|$Any \lor  Any$                 |$Any$|If two formulas irrelevant, than their or, $\lor$ is irrelevant|
|$Any \land Any$                 |$Any$|Meaningless in SAT|

Notes:

- It seems irrelevancy is closed for every operation...
- Put simply if we drop variable (or formula) from a problem (disjunction, conjunctive normal form) then it becomes a harder problem. 
- For the special case of empty formula we define it as $False$ (unsatisfying) so it works for that as well (when we drop all variables in a clause)
- The opposite of $Any$ may be $Either$ meaning the value is relevant, which can have a strict meaning: every solution consists the formula, or weaker meaning: there is at least one such formula

Off topic:

- A language idea is to define equivalence rules as well, besides tokens and grammar rules we may also define rules which make two sentences equivalent in a language - this is probably the most for a machine (without thinking and sensing capability) to understand about of semantics

# Reference

- https://en.wikipedia.org/wiki/Boolean_satisfiability_problem#3-satisfiability
- https://en.wikipedia.org/wiki/Conjunctive_normal_form
- https://en.wikipedia.org/wiki/Logical_disjunction