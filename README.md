# Sorting algorithm
Basic sorting algorithms that I created.
They sorts a list of numbers by their sizes.

## The first algorithm (comparison sort) works like this and can be used for all dtypes of arrays (int, float, int/float mix) but is not very efficient:

### 1: It starts at the start or the end of the list, depending on the order you want to sort it.
### 2: It takes the first two values and brings them into the right order
### 3: It steps to the next 2 indeces (2 and 3) if they are not in the right order, it swaps their places and keeps iterating backwards, to the previously sorted values and compares and swaps them until the values are in the right order, then it stops
### 4: It keeps iterating through step 3 until it reaches the end of the list and then it returns the sorted list

## The second algorithm (radix-count) can only sort arrays with integers but is very efficient and can be used to sort huge arrays very easily using not alot of computing power