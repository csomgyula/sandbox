If there is such a mapping between $A$ and $B$ as

$$
A <-f-> B
$$

or

$$
A -f-> B
$$

then such can be considered, if the link is materialized, as an extension to $A$ with $B$ through $f$ 
(and vica versa if bidirectional). How it is represented in memory, storage and UI is an 
interesting question.

- Memory: 
  - If processing is hybrid (a process frequently works on $A$ and $B$ mixed) then they should be placed close to each other
    in memory. This is then hard, because memory management must deal with dynamic extensions of already allocated regions.
    If however processing is not hybrid (same process will not frequently work on both $A$ and $B$ at the same time) then it
    is not necessary.
    - An interesting question is whether hybrid processes can be factored into homogenous parallel processes where each factored
      process only works on $A$ or $B$ but not both? The answer seems to be obviously true, so: the other question is how much
      sync is necessary between such factored processes (call them `A-process` and `B-process`)?
  - If either side is variable, then the link must be maintained dynamically. If not then such 
    change data capture and transfer is not relevant.
- Storage: ?
- UI: ?
