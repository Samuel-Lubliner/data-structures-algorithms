#

## Hash tables

Also known as hash maps, maps, dictionaries, and associative arrays.

Hash tables are fast because they use a hash function to map keys to values. Most languages have a built-in hash table

## Python dictionary

`dict()` or `{}`

```python
hash["key"] = value
```

The `get` function returns the value for a key.

## Use cases

- Fast lookups
- modeling relationships from one item to another
- DNS resolution (mapping a web address to an IP address)
- Caches (storing data for quick access)
- Catching duplicates

## Performance

Search, insert, delete

- Average case: O(1) constant time
- Worst case: O(n) linear time

## Collisions

- When two keys hash to the same index
- A linked list is used to store multiple key-value pairs at the same index
- This slows down the hash table
- Good hash functions minimize collisions

## Low load factor

Load_Factor = Num_Items_in_Hash_Table / Nun_Slots

- Measures how many empty slots remain in the hash table.
- Resizing the hash table can improve performance but is expensive.
