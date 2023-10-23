def rotLeft(a, d):
    # Use GCD and divide the array into sets
    # https://www.codewhoop.com/array/rotation-in-place.html
    return a[d:] + a[:d]

a = [1, 2, 3, 4, 5]
d = 1
print(rotLeft(a, d))