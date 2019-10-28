#Given an unsorted array with both positive and negative elements. Find the smallest positive number missing from the array in O(n) time using constant extra space. It is allowed to modify the original array.

def sol(l):
    length=len(l)
    l=set(l)
    for e in range(1, length):
        if not e in l:
            return e
