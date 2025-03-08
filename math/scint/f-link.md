$$
A <-f-> B
A -f-> B
$$

Such can be considered, if the link is materialized, as an extension to $A$ with $B$ through $f$ 
(and vica versa if bidirectional). How it is represented in memory, storage and UI is an 
interesting question.

- Memory: 
  - If processing is hybrid (works on A, B mixed) then they should be placed close in memory - that 
    is hard, because memory management must deal with dynamic extensions of already allocated 
	regions. If processing is not hybrid (same process will not work on both A and B at the same 
	time) then it is not necessary.
  - If either side is variable, then the link must be maintained dynamically. If not then such 
    change data capture and transfer is not relevant.
- Storage: ?
- UI: ?