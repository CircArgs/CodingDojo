This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.


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
