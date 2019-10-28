# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.


# Though process

# When I look at the array I look for the smallest possible value
# and then I look for the next smallest value that is not in the same column in a preceding or following row.
# At each step we seach the rows above and below the last row recursively


# note: Numpy is not necessary but just helps lean up the code rather than implement such functions ourselves. 
# some optimizing in time complexity could possible be achieve by writing everything custom. 
# The goal is a correct algorithm and understanding the complexities

# complexities:
# if the array of costs is of size n then
# time complexity is O(nlog(n)) since we recursively split the array in two each time.
# space complexity is O(n) since we edit the array in place we incur nothing there. we gain space from our hashtable (dictionary) that stores our selected values

import numpy as np
from collections import defaultdict
def sol(a):
    a=np.c_[range(len(a)), a].astype(float)
    # mins := {row:(val, col)...}
    mins=defaultdict(lambda: (None, None))
    def min_val(a):
        if not a.size:
            return
        a_view=a[:, 1:]
        min_i=a_view.argmin()
        row=min_i//a_view.shape[1]
        real_row=a[row][0]
        col=min_i-a_view.shape[1]*row
        # does a row before or after already have that column occupied?
        if (mins[real_row-1][1]==col or mins[real_row+1][1]==col):
            # can't choose that value so make it a value that wont be chosen
            a[row, col+1] = np.inf
            # and try again
            min_val(a)
        else:
            mins[real_row]=a_view[row, col], col
            min_val(a[:row])
            min_val(a[row+1:])
    min_val(a)
    return sum([v[0] for k,v in mins.items() if k>-1 and k<len(a)])

test1=[[17,2,17],[16,16,5],[14,3,19]]
test2=[[17,2,17, 16,16,5 ,14,3,19]]
test3=[[29, 39, 76, 30, 68,  5, 39],
       [58, 82, 96, 62, 60, 90, 83],
       [ 3, 47, 50, 99,  4,  7, 98],
       [71, 21, 79, 61, 22, 92, 90]]

assert sol(test1)==10
assert sol(test2)==2
assert sol(test3)==89
