

def find_smallest_missing_pos(A):
    n = len(A)
    seen = set()
    for a in A:
        if a > 0:
            seen.add(a)
    for i in range(1, n + 2):
        if i not in seen:
            return i

array = [-1,-3]
print(find_smallest_missing_pos(array))