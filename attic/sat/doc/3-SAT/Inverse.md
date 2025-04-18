If a vector $(x1,x2,...)$ solves a SAT problem
then its inverse 
- solves the inverse problem
- cannot be a full solution of any clause

where
- the inverse problem means we negate the logics within the clause:  
  $(l1 x1 \lor l2 x2 \lor l3 x3) \rightarrow (~l1 x1 \lor ~l2 x2 \lor ~l3 x3)$
- a full solution of $(l1 x1 \lor l2 x2 \lor l3 x3)$ means it solves the stronger $(l1 x1 \land l2 x2 \land l3 x3)$


there is map 
- between clauses and solutions
- problems/solutions and inverse problems/solutions