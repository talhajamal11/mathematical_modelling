""" 
Given a list of weights, determine all possible combination of sums that are possible
"""

weights = [1,3,3,5]

def possible_sum(weights):
    sums = set([0])
    for weight in weights:
        new_sums = set()
        for s in sums:
            new_sums.add(s + weight)
        sums.update(new_sums)
    return sums

print(possible_sum(weights))