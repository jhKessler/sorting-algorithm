# Sorting algorithm
Basic sorting algorithm that I created.
It sorts a list of numbers by their sizes.
It can sort in both ascending and descending order, depending on what you specify it to do.

## The algorithm works like this:

### 1: It starts at the start or the end of the list, depending on the order you want to sort it.
### 2: It takes the first two values and brings them into the right order
### 3: It steps to the next 2 indeces (2 and 3) if they are not in the right order, it swaps their places and keeps iterating backwards, to the previously sorted values and compares and swaps them until the values are in the right order, then it stops
### 4: It keeps iterating through step 3 until it reaches the end of the list and then it returns the sorted list
