# Linalg mapping

## Clause

A 3-SAT clause is like this for instance:

| clause                        | meaning                                            |
|-------------------------------|----------------------------------------------------|
| $x \lor y \lor z$             | either $x,y,z$ must be true to satisfy this clause |
| $x \lor y \lor \lnot z$       | either $x,y$ must be true, or $z$ false            |
| $\lnot x \lor \lnot y \lor z$ | either $x,y$ must be false, or $z$ true            |


In general we can write this

$$
clause = logic_func_x(x) \lor logic_func_y(y) \lor logic_func_z(z))
$$

where

- $logic_func_$ is a logical unary operator applied to the variable, either $identity$ or $not$

Although it is not common in math-syntax to index a function by variable name, there is nothing to prevent this. We can write this in a more usual way:

$$
clause = logic_func_1(x_1) \lor logic_func_2(x_2) \lor logic_func_3(x_3))
$$


We can also write this in a Lisp-like syntax:

```Lisp
c@clause = (or (logic_i@func x_i) (logic_j@func x_j) (logic_k@func x_k) 
```

We wil explain what `@` means later, now consider it some meta-data, which describes the context.

The above formalisms are position independents that is they have the same meaning if we permute the variables:

| syntax | original                                          | permuted                                          | 
|--------|---------------------------------------------------|---------------------------------------------------|
|math    |$x \lor y \lor z$                                  |$x \lor z \lor y$                                  | 
|math    |$logic_1(x_1) \lor logic_2(x_2) \lor logic_3(x_3))$|$logic_2(x_1) \lor logic_1(x_1) \lor logic_3(x_3))$|
|lisp    |`(or (logic_i@func x_i) (logic_j@func x_j)...`     |`(or (logic_j@func x_j) (logic_i@func x_i)...`     |

Hence the above robust (not prone to missunderstandings) but for the cost of verbosity. 

If we fix the positions then we can use the following abbreviation for the cost of robustness:

### Abbrev

```Lisp
clause = (logic_1 logic_2 ... logic_n) @ abbrev(clause) = logic_or abbrev(logic_func)
```

## Solution

A 3-SAT solution for the problem $(x \lor y \lor \lnot z) \land (\lnot x \lor y \lor z)$

is like this for instance:

$$
x = True, y = False
$$


In general:

$$
x_1 = logic_val_1, x_2 = logic_val_2, ...
$$

where:

- $logic_val_$ is either $True$ or $False$ 

Or in Lisp-like syntax: 

```Lisp
s@(sol 3sat) = ((subs x_1@var logic_1@val) (subs x_2@var logic_2@var) ... (subs x_n@var logic_n@val))
```

where:

- $subs x_@var logic_@val$ means we substituted the value, $logic_$ into the variable, $x_$

### Abbrev

The above formalism is position independent that is it has the same meaning if we permute the values:

```Lisp
((subs x_1@var logic_1@val) (subs x_2@var logic_2@var) ...)
=
((subs x_2@var logic_2@val) (subs x_1@var logic_1@var) ...)
```

Hence the above is readable, robust (not prone to missunderstandings) but for the cost of verbosity. If we fix the positions then we can use the following abbreviation for the cost of robustness:

```Lisp
s = (logic_1 logic_2 ... logic_n) @ (abbrev sol 3sat) = (list (abbrev subs var val))
```

This is now not position independent, $(logic_2 logic_1 ... logic_n)$ means a different things (permute the values between variable $x_1$ and $x_2$).


### Formal meaning

A solution `logic 1 logic 2 ... logic n` 

is a solution to the problem 

```
(logic p(11) logic p(12) logic p(13))
(logic p(21) logic p(22) logic p(23))
...
(logic p(n1) logic p(n2) logic p(n3))
```

if for all clause, `i`:

```
sol logic p(i1) = clause logic p(i1)
or
sol logic p(i2) = clause logic p(i2)
or
sol logic p(i3) = clause logic p(i3)
```

## TODO

Can it be assumed a scalar product? or the like?

