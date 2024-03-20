# Binary search

Binary search only works when your list is in  sorted  order.

For any list of n, binary search will take log2n steps to  run  in  the  worst  case. This is much faster than linear search, which takes n steps.

For a list of 1024 elements, you have to check 10 elements to find the target in the worst case. log(1024) = 10, because 2^10 = 1024.

The `binary_search` function takes a sorted array and an item.  If  the  item  is  in  the  array,  the  function  returns  its position.

- low and high keep tack of which part of the list you'll search in.
- While you haven't narrowed it down to one element...
- Check the middle element.
- Found it? Return its position.
- Too high? Move high down.
- Too low? Move low up.
- If you exit the loop without finding the item, return nil.
