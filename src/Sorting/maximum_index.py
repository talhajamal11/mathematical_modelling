# Start at 0, take steps mentioned, avoid badElement, return the highest number reached
# At each step you can jump the exact amount as the step e.g. at step 4 you can jump 4 steps
# Determine the maximum index that can be reached

def maximum_index(steps, badElement) -> int:
    max_pos = int((steps * (steps + 1)) / 2)
    if max_pos == badElement:
        max_pos -= 1
    for pos in range(max_pos, -1, -1):
        for step in range(steps, -1, -1):
            pos -= step
            if pos == badElement:
                max_pos -= 1
                break
            if pos == -1:
                return max_pos

#print(maximum_index(steps, badElement))

def new_maximum_index(steps, badElements):
    max_index = steps * (steps + 1) // 2
    while max_index >= 0:
        index = max_index
        valid = True
        for j in range(steps, 0, -1):
            if index == badElement:
                valid = False
                break
            if index - j <= 0:
                break
            index -= j
        if valid:
            return max_index
        max_index -= 1
    return 0

steps = 4
badElement = 3

print(new_maximum_index(steps, badElement))