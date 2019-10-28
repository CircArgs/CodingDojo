#Given an unsorted array with both positive and negative elements. Find the smallest positive number missing from the array in O(n) time using constant extra space. It is allowed to modify the original array.

# Thought process

# ideally we would like to go through the pos ints and check if they are in there. brute force would be n^2
# to get around this we use a hash table to reduce checks to constant time


# note: Numpy is not necessary but just helps lean up the code rather than implement such functions ourselves. 
# some optimizing in time complexity could possible be achieve by writing everything custom. 
# The goal is a correct algorithm and understanding the complexities

# complexities:
# if the list is of length n then
# time complexity is O(n) since we iterate over the positive integers and check in constant time if the int is in our list
# space complexity is O(1) since we require no extra proportional space


def sol(l):
    length=len(l)
    l=set(l)
    for e in range(1, length):
        if not e in l:
            return e
