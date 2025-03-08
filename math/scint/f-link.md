If there is such a mapping between $A$ and $B$ as

$$
A \leftarrow f \rightarrow B
$$

or

$$
A - f \rightarrow B
$$

then such can be considered, if the link is materialized, as an extension to $A$ with $B$ through $f$ 
(and vica versa if bidirectional). 

## Implementation

How it is represented in memory, storage and UI is an interesting question.

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

## Semantics and practice

The semantics and practice seems to be another interesting question, what this f-link represents in reality, why we want to use such 
link? At first I see two cases:

1. Computing: There are algorithms which works better with one representation and others which works better with the other. This the
   case with scint. Scint may be used for sorting, compression (if it is at all), while normal binary representation works for normal
   operation. This is not saying that scint is better for sorting or compression. Similar sorting can be implemented for normal
   representation (if I understand well this is called radix sort) and... I know nothing yet about scint-based compression. So this is
   just an example.
2. UI: This case $A$ can represent the backend model (as used in storage and/or computing) and $B$ may represent the UI model. Such cases
   are interesting for two reasons. First the UI model is usually more rich then the backend model, hence the $f-link$ is not bidirectional.
   However in one UI session (for one user, one application session) the same model is usually represented once and only once in UI (here
   I do not count tabs, lists, outlines as seperate appereance). So in many case $f-link$ can be still bidirectional per UI session, though
   not mathematically computable, instead driven by the UI and the very fact that the UI representation is unique at every point in time.

Note that the last is somewhat hints that links, mappings has at least two meanings: 
 - The computational meaning, when from $a ∈ A$, $b ∈ B$ can  be computed
 - The instance meaning, when from $b ∈ B$, $a ∈ A$ can be computed, but even though the opposite is not true, there is only one instance of $b$ representing $a$. So there is still a bidirectional mapping between $A$ and $B$ within context:
    - $View  - model \rightarrow Model$
    - $Model  - view_{context} \rightarrow View$
    - constraint: $view( model(v), view_{context}(v) ) = v$
    - this then creates a temporal binding: $Model \leftarrow binding[T] \rightarrow View$ which mathematically is determined by the state of the
      view context at every given point in time, and can be also cached (materialized in memory)

Also note that I do not think that Model is more a model then the UI. I consider both of them as models, Model as a backend model (and even that can be two: storage and computational model) and UI as frontend model. However they are both models of some reality or abstraction of reality. The difference is that the backend model is more abstract while the UI model is more rich, hence we cannot compute the view from the model in general, only within a given view context (such as style, scroll position etc.). That is two say UI is a model of reality through the backend model and a contextual view mapping. Schematically

$$
Reality\ (or \ abstraction)\ -\ model\ \rightarrow\ (Backend)\ Model -\ view_{context}\ \rightarrow\ View\ (Model)
$$

Which suggests that view is just a context dependent computation of backend model... except if the backend model is normalized, which can be many time the case (data normalization, software modularization) which case the view represents the model (as seen) by the user. Question is: does the human brain also normalize? How?

$$
Reality\ (or \ abstraction)\ -\ model\ \rightarrow\ (Backend)\ Model -\ view_{context}\ \rightarrow\ View\ (Model)\ -\ see \rightarrow\ Seen\ model\ - brain\ processing\ \rightarrow\ Normalized\ model\ by\ brain
$$

Now that NLP is a subject of computation, too, one may ask the related question: What is the relation between computing NLP, backend, frontend representations and human understanding? Or a thing which is more important for me, what is the role, utility, function of such representation? How can it help? Make life better?
