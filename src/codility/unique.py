def solution(A):
    # Implement your solution here
    unique = {}
    for index, num in enumerate(A):
        if num not in unique:
            # unique
            unique[num] = index
        else:
            # duplicate
            unique.pop(num)
    result = list(unique.keys())
    if result:
        return result[0]
    else:
        return -1

A = [4, 10, 5, 4, 2, 10] 
print(solution(A))