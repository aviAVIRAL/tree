

print()
print()
from collections import defaultdict

# Create a defaultdict for counting
mp = defaultdict(int)

# Example data: list of items
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Count occurrences of each x
for x in data:
    mp[x] += 1  # Automatically initializes to 0 if the key is missing

print(mp)
# Output: defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'orange': 1})
# .........................................
# .........................................
# .........................................
print("////////")
print()

from collections import defaultdict

# Create a defaultdict with int as the default factory
mp = defaultdict(int)

# Access a non-existent key
print(mp['a'])  # Output: 0    ## key nhi hai but degaul tvalu de  0 

# Increment the value at key 'a'
mp['a'] += 5
print(mp['a'])  # Output: 5

# Access another non-existent key
print(mp['b'])  # Output: 0

mp["c"] # impo 

# Modify the value for key 'b'
mp['b'] += 3
print(mp)  # Output: defaultdict(<class 'int'>, {'a': 5, 'b': 3})


print()
print("..........")
print()

from collections import defaultdict

# Create a defaultdict with list as the default type
mp = defaultdict(list)

# Adding elements to mp
mp['a'].append(1)
mp['a'].append(2)
mp['b'].append(3)

# Accessing elements
print(mp['a'])  # Output: [1, 2]
print(mp['b'])  # Output: [3]

# Accessing a non-existent key
print(mp['c'])  # Output: []
mp['L']

print(mp)