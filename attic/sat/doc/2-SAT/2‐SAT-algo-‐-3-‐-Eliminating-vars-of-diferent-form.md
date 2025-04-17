stub

## Colored graphs

### Mapping 2-SAT to red-green graph

First we map the 2-SAT problem space to a colored graph:

|to  |from    |sample |desc|
|----|--------|-------|----|
|vertice pair|variable|||
|vertice|variable value|$variable(x_i) \enspace \rightarrow \enspace vertex(x_i, True), \enspace vertex(x_i, False)$|each variable $x_i$ is mapped to two, originally uncolored vertices representing the variable's two possible values, $True$, $False$|
|green edge|clause  |$clause:       \enspace (x_i, \lnot x_j) \enspace \rightarrow \enspace edge(color(green), \enspace vertex(x_i=True), \enspace vertex(x_j=False)$|every clause is mapped to a green edge between the two possible values satisfying it (must be satisfied)|
|red edge|contradiction|$contradiction(x_i \land \lnot x_i) \enspace \rightarrow \enspace edge(colr(red), \enspace vertex(x_i=True), \enspace vertex(x_i=False)$|contradictions, e.g. $x_i = True$, $x_i = False$ are mapped to red edges between values and their negates (won't happen)|
|green vertices|solution||is a red-green coloring of vertices, where each green edge is connected to at least one green vertex (satisfying the clause) but no two green vertices are connected with red edge (does not have contradiction)|
|red-green coloring|solve|||

Term: I call this graph the problem graph, since it represents all clauses and all possible solutions

### Existence of red-green cycles

Second we are looking for red-green cycles in this graph by using the following known theorem/method:

Theorem: If every vertex's degree is greater than equal 2 then the graph has circle

Method: Just walk edges starting from a random vertex until you see a vertex you already saw (here walk means you never step back, never walk an edge you already walked) 

To apply this we shall first recognize that 

- Every vertex in the graph has a connected green edge (we already eliminated 1-SAT clauses)
- Every vertex has a connected red edge (there is no variable in single form)

Now we can apply the theorem:

Theorem: 
  1. The graph has either an even red-green-... cycle
  2. or the graph has an odd red-green-...-green-green cycle

Method: just walk the red green edges in tandem until you enter a vertex you already saw

### Inference from red-green cycles

1. In case we found an even red-green cycle then we can eliminate vars, since such clause cycle can be satisfied only with two possible combination of variable substitutions (this follows from the fact that red edges are contradictionary and we have to satisfy each green edge)

2. In case we found a odd red-green-...-green-green cycle then the green-green variable must be satisfying otherwise we get to a contradiction for the remaining odd path

I call this an inference cycle, since such cycle drastically restricts the solution space based on trivial inference.

## Algorithm

1. Map 2-SAT to the solution space
2. Find a red-green cycle (aka inference cycle)
3. Eliminate variables from the cycle (using trivial inference)

## Another way
A maybe simpler or visible way of representing the above:

- Create a so called implication graph, representing the SAT problem
  - Vertices: (variable, value) pairs, such as e.g. $(x1, True)$ representing the $x_1$ variable substituted with $True$
  - Edges: for every constraint $(o x_i\ or\ o x_j)$ (where $o$ is a logic sign/operator either nothing/identity or negate, $\neg$) create two directed edges representing implications, if one part is not satisfied then the other part must be: 
    - $\neg o x_i\ \implies \ o x_j$
    - $\neg o x_j\ \implies \ x_i$
    - sample: consider this constraint: $(x_1\ or\ \neg x_2)$ then the following implication holds, satisfying this constraint is equivalent to this:
      - $\neg x_1 \implies \neg x_2$
      - $x_2 \implies x_1$
- Theorems
  - Due to the [normalization](/csomgyula/sat/wiki/2%E2%80%90SAT-algo:-2.-Eliminating-vars-of-same-form) (each variable appears in both form in constraints): 
    - each variable has both vertices when substituted with $True$ and when substituted with $False$
    - each variable has both incoming and outgoing edges
  - Hence: 
    - there is a directed cycle in the graph, in fact at least two, if we find a cycle then there is a dual cycle where each value is replaced with its negated form: $(variable, value)\ \rightarrow \(variable, \neg value)$ and direction is reversed
    - such cycle can be either satisfied or contradictionary (if it contains the same variable with both substitutions), in the latter case the SAT problem is not solvable, in the former case:
  - The dual cycle means that the variables of it are bound to each other: one variable value determines all the others through the implication cycle, hence all other variables can be eliminated