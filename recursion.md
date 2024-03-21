# Recursion

Recursion is where a function calls itself.

There’s no performance benefit to using recursion. Loops are
sometimes better for performance. Loops may achieve a performance gain for
your program. Recursion may achieve a performance gain for your
programmer.

Every recursive function has two parts:

- The recursive case is when the function calls
itself.
- The base case is when the function doesn’t call itself again so it
doesn’t go into an infinite loop.

Push: Add an item to the top of the stack.
Pop: Remove the top item from the stack.

The call stack: When you insert an item, it gets added to the top of the list. When you read an item, you only read the topmost item, and it’s taken off the list.

when you call a function from another function, the calling function is paused in a partially completed state. All the values of the variables for that function are still stored in memory. 

In recursion,  using the stack is convenient because you can keep track of the state of the function, but it comes at the cost of using more memory. If the cost of using more memory is too high, you can use a loop instead of recursion.