import math
import numpy as np

line1 = "Physics Scores  15  12  8   8   7   7   7   6   5   3"
line2 = "History Scores  10  25  17  11  13  17  20  13  9   15"

x = [int(num) for num in line1.split()[2:]]
y = [int(num) for num in line2.split()[2:]]

def mean(lst):
    return sum(lst) / len(lst)

def var(lst):
    total = sum([(i - mean(lst))**2 for i in lst])
    return total / len(lst)

def cov(lst1, lst2):
    l1m = mean(lst1)
    l2m = mean(lst2)
    total = sum([(l1 - l1m)*(l2 - l2m) for (l1, l2) in zip(lst1, lst2)])
    return total / len(lst1)

corr = cov(x, y) / (math.sqrt(var(x)*var(y)))
print(corr)

from sklearn.feature_selection import r_regression
sk_corr = r_regression(np.array(x).reshape(-1,1), np.array(y))
print(sk_corr[0])