#

## Divide and conquer

Divide and conquer is a recursive technique for
solving problems. Quicksort is a D&C sorting algorithm, and faster than selection sort.

D&C is a way to think about a problem. Here’s how D&C works:

1. Figure out a simple case as the base case.
2. Figure out how to reduce your problem and get to the base case.

Tip: When you’re writing a recursive function involving an array, the base case is often an empty array or an array with one element. If you’re stuck, try that first.

Why would I do this recursively if I can do it easily with a loop? Functional programming languages like Haskell don’t have loops, so you have to use recursion to write functions like this.

## Inductive proofs

Inductive proofs are one way to prove that your algorithm works. Each inductive proof has two steps: the base case and the inductive case.

Base Case: Prove the algorithm works for the simplest cas (arrays of size 0 and 1 for sorting algorithms).

Inductive Step: Show that if the algorithm works for a certain size, it will work for the next size up, establishing its correctness for all sizes.

Quicksort is unique because its speed depends on the pivot you choose. If you’re implementing quicksort, choose a random element as the pivot. The average runtime of quicksort is O(n log n)!

## Runtime Complexity:
Average Case: O(n log n)

Worst Case: O(n^2), which occurs with poor pivot choices.

Best Case: O(n log n) typically achieved by good pivot selection.

## Quicksort vs. Other Sorting Algorithms:

Selection sort has a runtime of O(n^2). That’s a pretty
slow algorithm. There’s another sorting algorithm called merge sort, which is O(n log(n)). Much faster!

Quicksort is a tricky case. In the worst case, quicksort takes O(n^2) time. It’s as slow as selection sort! But that’s the worst case. In the average case, quicksort takes O(n log n) time.

What do worst case and average case mean here? If quicksort is O(n log(n)) on average, but merge sort is O(n log(n))
always, why not use merge sort? You usually ignore that constant, because if two algorithms have different Big O times, the constant doesn’t matter. But sometimes the constant can make a difference. Quicksort versus merge sort is one example. Quicksort has a smaller constant than merge sort. So if they’re both O(n log(n)) time, quicksort is faster. And quicksort is faster in practice because it hits the average case way more often than the worst case.

The performance of quicksort heavily depends on the pivot you choose. Suppose you always choose the first element as the pivot. And you call quicksort with an array that is already sorted. Quicksort doesn’t check to see whether the input array is already sorted. So it will still try to sort it.

In the worst case, the stack size is O(n), leading to O(n^2) time complexity.

In the best case, the stack size is O(log n). The best case is also the average case. If you always choose a random element in the array as the pivot, quicksort will complete in O(n log n) time on average. Quicksort is one of the fastest sorting algorithms out there, and it’s a very good example of D&C.
