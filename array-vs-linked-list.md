# Arrays and Linked Lists

Arrays and linked lists are two options for storing multiple items of data.

## Arrays

In Python an array is called a list.

Arrays allocate elements in contiguous memory locations, enabling direct access to any item based on its address. You know the address for every item in your array.

Arrays are great if you want to read random elements, because you can look up any element in your array instantly with random access. Reading run time: O(1).

Inserting and deleting elements in an array is slow. Inserting and deleting run time: O(n). Inserting or deleting an element requires shifting all subsequent elements. 

## Linked lists

It's a common practice to track both the first (head) and last (tail) elements of a linked list. Inserting and deleting elements at either the beginning or end can be performed efficiently, with a time complexity of O(1).

One element stores the address of the next one. Linked lists can only do sequential access. Sequential access means reading the elements one by one, starting at the first element. You can't read the last element without reading all the elements before it. Reading run time: O(n).

With a linked list, the elements aren’t next to each other, so you can’t instantly calculate the position of the fifth element in memory—you have to go to the first element to get the address to the second element, then go to the second element to get the address of the third element, and so on until you get to the fifth element

Linked lists are optimal for operations that iterate over elements sequentially, as you can easily move from one item to the next by following the links. However, for random access or operations that require frequent jumping between elements, linked lists are less efficient compared to arrays.
