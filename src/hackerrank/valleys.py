def countingValleys(steps, path):
    # Write your code here
    valleys, left = 0, 0
    up, down = 0, 0
    for right in range(steps):
        if path[right] == "U":
            up += 1
        else:
            down += 1
        if up == down and path[left] == "D":
            valleys += 1
            up = 0
            down = 0
            left = right + 1
        elif up == down:
            up = 0
            down = 0
            left = right + 1
    return valleys

steps = 8
path = "UDDDUDUU"
print(countingValleys(steps, path))
