# Neighbourhood topology

## Adjacency relation

- In this modell the business modell is not just a set of elements where the relation between elements is unimportant, but a system which contains one or more relations that are interesting and meaningful to the user.
  - For example, in the case of text, such a relation is the sequence of characters (previous character, next character)
- Then, the adjacency relation is defined in the model as an element is adjacent to another element if they are in a relation.
- In the view, adjacency is defined differently, geometrically. For example, two bounding boxes are adjacent if there is no other box between them horizontally/vertically

## Discrete topology

Based on the adjacency relation, we define topology (set system) as follows (a little different from the mathematical definition):

- Domain: The domain of topology is the elements
- Base sets: Every element and any of its neighbors are part of the base set
- Other sets: Every set that is formed by the union of the base sets, i.e. closed to the union

However, we do not require closure to the intersection because in this discrete case it would result in a trivial topology, the power set of the elements.

The above can be imagined a little more clearly if I define the above in a graph-like manner. The elements of the graph are the elements, and the edges connect the neighbors. I consider the environment to be the connected sets, where a path between any two points through the points is in the set, no need to exit. I also used the more formal definition to make it appear that we are not taking the classical mathematical definition as a basis, because that would be empty.

If we want to follow the mathematical definition, which makes the results applicable here, then an alternative definition is as follows:

- Domain: The domain of topology is the elements
- Base sets: Every set containing an element and all its neighbors
- Other sets: Closed under union (and intersection) 

## See also
- https://en.wikipedia.org/wiki/Topology
- https://chatgpt.com/share/679ccfdb-5e4c-800f-8ad7-4db76a71fb35


