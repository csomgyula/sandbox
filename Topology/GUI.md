# GUI topológia

I think 2D GUI can be described with a 2+1D topology.

## 1+1D GUI

Before I get to it, I'll outline the 1+1D topology, which is the simpler, degenerate case within the 2D GUI:

- In the 1+1D GUI Topology, 1D is a set system in which any two sets are either disjoint or (real) parts of the other.
  - Conceptually, 1D is a hierarchical partitioning. For example, a text field, in which the elements are the characters, and the field itself is a set. But a text area is also like this, but there it is already a set system: the lines and the entire area. But this still makes it topologically 1D
  - An important feature of this is that any set can be part of any 2 other sets, only at most 1, if they do not contain each other. This is an equivalent formulation, we will generalize this.
- 1+1D means that such 1D topologies are linked together (in UI this means actions)
  - Visually 1+1D is a directed graph of hierarchical partitions
  - An interesting question here is what is the model of the textual language, it will probably be similar 1D, and what is the topology of the backend models (OO, list, hash table, etc.), I suspect it is also 1D (except for niche applications such as GIS).

## 2+1D GUI

The 2+1D topology then:

- In the 2+1D GUI Topology, 2D is a set system in which any set can be part of at most 2 out of any 3 other sets, if they do not contain each other. Or, and I am still investigating this, this should probably be closed in terms of intersection.
  - Visually, you should think of a grid here, where, unlike a text area, each cell is part of both a row and a column, and is in their intersection.
- Here, 2+1D also means links, which also express actions here. That is, it is about a directed graph of 2D topologies.

## TODO

The above model does not include the following:
- Business model, which is maybe nothing more than assigning names/numbers with UX meaning to sets (typically a navigation function should be considered here), and the business backend binding. I see these as a mapping that should first have an image set, and then we would deal with the business tooling.
- Scrolling, the fact that the full view and the view port that is visible on the interface are different. This is also a fundamental issue and can also hit to the model (dynamic loading of large models), but in the basic case (when the model fits in memory) it is not so interesting, i.e. an internal UI-level issue.
- Styles, which is fundamental in UX (uniformity) and a very exciting topic, but here I am looking at the topic from the business model's perspective. I am examining how the business model and UI model relate structurally.