## words

### clause

clauses can be represented with `01_` patterns (words maded from letters `0 1 _`  
samples:

| clause                            | word          |
|-----------------------------------|---------------|
| $x1 \lor x2 \lor x3$              | `clause 111_` |
| $\lnot x1 \lor \lnot x2 \lor x3$  | `clause 001_` |
| $x1 \lor  x2 \lor \lnot x4$       | `clause 11_0` |

Hence:

- 0 means negate (~)
- 1 means don't negate (id)
- _ means space, no restriction

### solution

solutions can be also represented with `01_` patterns  
samples:

| solution                   | word            |
|----------------------------|-----------------|
| $x1=True,  \ x2=False$ | `solution 10__` |
| $x1=False, \ x2=True$  | `solution 01__` |
| $x3=True,  \ x4=False$ | `solution __10` |

Hence:

- 0 means False
- 1 means True
- _ means Any value 

## match

by representiing clauses and solutions with words, the satisfaction problem can be mapped to a 
pattern matching problem, put simply a solution solves a problem if its word matches all 
clause words

where 

- matches defined for letters, words as follows:

### letter

| letter       | matches    |
|--------------|------------|
| `solution 1` | `clasue 1` |
| `solution 0` | `clause 0` |
| `solution _` | `None`     |

### word

- a solution word matches a clause word if at least one of the solution letters matches the clause 
  letter at the same position
- samples:
  
| word            | matches       | matches | match pos |
|-----------------|---------------| --------|-----------|
| `solution 11__` | `clasue 111_` | True    | 1,2       |
| `solution 11__` | `clasue 10_1` | True    | 1         |
| `solution 11__` | `clasue 0_11` | False   | None      |
| `solution 111_` | `clasue 111_` | True    | 1,2,3     |
| `solution 011_` | `clasue 111_` | True    | 2,3       |
| `solution 0_1_` | `clasue 111_` | True    | 3         |
| `solution 0_0_` | `clasue 111_` | False   | None      |
  
### solution

then a solution matches a problem if its word matches all clauses of the problem
