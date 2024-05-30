# Breadth-first search

- Is there a path from A to B
- Solves the shortest path problem.
- Check search list in the order added (Queue)
- Avoid an infinite loop by keeping track of what is searched.

## Graphs

Graphs use nodes and edges to model connections.

## Queues

- First-in, first-out, in contrast to a stack which is last-in, first-out.
- Cannot access random elements
- enqueue and dequeue operations

## Hash table

- Maps a key to a value
- Map a node to its neighbors
- Order does not matter

Simple graph example:
```python
graph = {}

# an array of all the neighbors of you
graph[“you”] = [“alice”, “bob”, “claire”]
```

Bigger graph example:

```python
graph = {}
graph[“you”] = [“alice”, “bob”, “claire”] graph[“bob”] = [“anuj”, “peggy”] graph[“alice”] = [“peggy”] graph[“claire”] = [“thom”, “jonny”] graph[“anuj”] = []
# Directed graph becuase peggy is a neighbor of alice but alice is not a neighbor of peggy
graph[“peggy”] = []
graph[“thom”] = []
graph[“jonny”] = []
```

## Implementing the algorithm

1. Initialize the search queue
2. Track list of searched people
3. Begin search loop: While the queue is not empty:
   1. Dequeue: Pop the first person off the queue.
   2. Check for mango seller:
      1. If this person is a mango seller print message and return True.
      2. If this person is not a mango seller: Add all of this person’s neighbors to the queue.
4. Mark as searched: Add the checked person to the list of searched people.
5. End condition: If the queue becomes empty, there is no mango seller in your network.

## Run time

- Breadth-first search takes O(number of people + number of edges)
- Commonly written as O(V+E) or O(Vertices + Edges)
