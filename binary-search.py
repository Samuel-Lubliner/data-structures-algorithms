def binary_search(arr, item):
    # Low and high keep track of which part of the list you'll search in.
    low = 0
    high = len(arr) - 1
    
    # While you haven't narrowed it down to one element ...
    while low <= high:
        # ... check the middle element
        mid = (low + high) // 2
        guess = arr[mid]
        # If so, return the index.
        if guess == item:
            return mid
        # The guess was too high
        elif guess > item:
            high = mid -1
        # The guess was too low
        else:
            low = mid + 1
        # Item doesn't exist
    return None

# Test
my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # 1
print(binary_search(my_list, -1)) # None