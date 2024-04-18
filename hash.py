import sys

# hash table with dictionary
# key value pairs of grocery items and price
item_prices = {"apple": 0.67, "milk": 1.49, "bread": 0.99, "cheese": 2.79}

# Check if the user has entered an item as a command line argument
if len(sys.argv) > 1:
    item = sys.argv[1].lower()  # Take the first command line argument as the item name
    # Check if the item is in the dictionary
    if item in item_prices:
        print(f"The price of {item} is ${item_prices[item]}")
    else:
        print("Item not found in the inventory. Please enter a valid item name.")
else:
    print("Please enter an item name when running the program. Example usage:")
    print("python hash.py apple")