""" 
At each step you can move from position i to i + j, or remain where you are at. 
The value of i begins at 0. The value of j begins at 1 and increments at each step by 1. 
There is one known index that must be avoided. Determine the highest index that can be reached. 
"""

steps = 4
bad_index = [1,2,3]

def solution(steps, bad_index):
    max_index = (steps*(steps + 1))//2
    while max_index > 0:
        curr_index = max_index
        for j in range(steps, -1, -1):
            curr_index -= j
            if curr_index in bad_index:
                # bad path
                break
            if curr_index == 0:
                return max_index
        max_index -= 1
    return max_index

print(solution(steps, bad_index))