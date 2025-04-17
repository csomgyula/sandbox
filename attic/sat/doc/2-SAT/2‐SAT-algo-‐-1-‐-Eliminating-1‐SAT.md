# Eliminating 1‐SAT clauses from a 2-SAT problem

[2-SAT](2%E2%80%90SAT) is by definition a problem where each clause contains at max. 2 variables. Hence this definition allows cases when a 2-SAT problem contains 1-SAT clauses. Such hybrid case increases the problem's perceived complexity. Fortunately they can be "simplified", that is each 2-SAT problem can be transformed to an equivalent form, where is clause contains exactly 2 variables.

## Samples

### Simplest cases

Say you have the following simplest case:

$$
(x_1) \land (x_1 \lor x_2)
$$


The first clause can only be satisfied if $x_1$ is $True$ (necessary condition), which then satisfies the second clause (sufficient condition). 

Now lets see a bit more complicated sample:

$$
(x_1) \land (\lnot x_1 \lor x_2)
$$

Again the first clause can only be satisfied if $x_1$ is $True$ (necessary condition), however, since the second clause  $(\lnot x_1 \lor x_2)$ contains $\lnot x_1$ this cannot be satisfied by $x_1$, it can only be satisfied iff $x_2$ is $True$.

In respect with the length of clauses, these are the prototype minimal 2 SAT cases which has 1-SAT clause but the whole problem is not a 1-SAT problem. Lets see all cases:

|Problem                                 |Solution                      |Reason                            |
|----------------------------------------|------------------------------|----------------------------------|
|$(x_1) \land (x_1 \lor x_2)$            |$x_1 = True$                  |$x_1$ appears in the same form in both clauses|
|$(x_1) \land (\lnot x_1 \lor x_2)$      |$x_1 = True \land x_2 = True$ |$x_1$ appears in the opposite form in the clauses|
|$(x_1) \land (x_1 \lor \lnot x_2)$      |$x_1 = True$                  |You tell|
|$(x_1) \land (\lnot x_1 \lor \lnot x_2)$|$x_1 = True \land x_2 = False$|You tell|
|$(\lnot x_1) \land (\lnot x_1 \lor x_2)$|You tell|You tell|
|$(\lnot x_1) \land (x_1 \lor x_2)$      |You tell|You tell|
|$(\lnot x_1) \land (\lnot x_1 \lor \lnot x_2)$|You tell|You tell|
|$(\lnot x_1) \land (x_1 \lor \lnot x_2)$      |You tell|You tell|

### Moderate cases

Some clauses, no recursion, but can yield contradiction

### Complex cases

Recursion

### Samples as a methodology

Samples is a technique learnt from pedagogy and software testing. 

* They say human brain excels in abstraction, can quickly extract common things from a bunch of examples, that is rebuild abstractions. However it only works in this direction and not the other way: one may not understand abstract terms unless samples are presented to her.

Side note: If I were a teacher, which I am not, I would consider this as a core practice: present samples before abstractions. This then requires the teacher to understand her students, since even samples will be only understood if students already experienced them, know them. This is also why I think the idea behind segregation is silliness, thinking that different people with different background are less intelligent usually means that the teacher does not know her students and is pushing her stories not familiar to her student, hence not understood by them. This then gives the wrong impression that students with different background of the teacher are less that talented than the ones having the same background. I think, teaching must be tailored to the culture, habits of the students.

* Software testing: by sample...

## Algorithm
stub

Algoritm:

1. Main loop: While there is 1-SAT clause:
   1. Solve 1-SAT clauses
      - Check for contradiction, stop if any and return with no solution
      - Remember the partial solutions and remove solved clauses
   2. Reduce related 2-SAT clauses by substituting the 1-SAT solutions
      - Check for contradiction, stop if any, return with no solution
      - Remove solved clauses (0-SAT case)
      - Replace reduced clauses with reduced ones (2-SAT -> 1-SAT)
2. Return
   - the partial solution along with the simplified 2-SAT problem, if there are remaining clauses
   - the solution, if reduction lead to a full solution

Normal flow:

- You repeat the same two step "solve-reduce" procedure until there is no more 1-SAT or a contradiction found. 
- The main idea is that satisfying a 1-SAT clause is trivial: e.g. a $(x_1)$ can only be satisfied iff $x_1$ is $True$. 
- Once you solved the 1-SAT clauses of the problem, you can carry its consequences to the 2-SAT clauses. In other word you can apply the "knowledge" from 1-SAT solutions to the other clauses by substituting there the solution, which then simplifies them.
- Each solve step produces partial solutions which shall be remembered, since that is the main goal
- Solve steps simplifies the original problem to a new problem with less variables and less clauses
- If the second step produced new 1-SAT clauses then you repeat until there is no more

Exceptions:

- Each step may lead to contradiction, then you stop

Memory:
- Each step produces partial solutions (to 1-SAT clauses) which shall be remembered

### Solve 1-SAT clauses

Step 1. Solve 1-SAT-s and check if there were contradictions. If there was contradiction, the problem is unsatisfiable, hence the algorithm can stop.

1. Solve 1-SATs
   1. assign truth value to related variables (such as $satisfying~(x_1) \implies binding~x_1 = True$)
   2. check for contradiction, stop if any and return with no solution (such as $(x_1) \land (\lnot x_1) \implies \bot$)
   3. if no contradiction
      1. remove solved 1-SAT clauses
      2. return partial solutions and modified problem

### Reduce related 2-SAT clauses

2. Simplify 2-SAT clauses by substituting 1-SAT solutions
   1. substitute solved 1-SAT variables into 2-SAT clauses they also appear in, such as  
      $satisfying~(x_1) \land (x_1 \lor x_2) \land (\lnot x_1 \land x_3)$ implies binding $x_1 = True$ and satisfying $(True) \land (True) \land (True \lor x_2) \land (False \lor x_3)$ 
   2. check for 0-SAT contradiction, stop if any and return with no solution   
   3. if no contradiction
      1. drop solved 2-SAT clauses (0-SAT)
      2. replace reduced 2-SAT clauses with the reduced 1-SAT ones, if any
      3. return modified problem

Solving 1-SAT clauses has no direct consequence for 2-SAT clauses where the 1-SAT variables do not appear. However it has direct consequences for such 2-SAT clauses where such variables do appear: you substitute those variables into those 2-SATs which contain  those variable. This then leads to either 0-SATs (when two variables were substituted) or 1-SATs (when one variables were substituted). More specifically:
- If the substituted variable appeared in the same form then such clauses will be already satisfied (no more task, just drop that clause). 
- If however the substituted variable appeared in the opposite form then such clause can only be satisfied with the other variable of the clause, hence substitution can produce new 1-SAT clauses (recursion)
- In the special case if two 1-SAT variables were substituted into the same 2-SAT clause then, depending on the variable values and the 2-SAT clause it will become either $True$ (no more task, just drop that clause) or $False$ (contradiction so we stop)

