A = [9,3,9,3,9,7,9]

def solution(A):
    unique = {}
    for num in A:
        if num not in unique:
            unique[num] = 1
        else:
            unique[num] -= 1
            unique.pop(num)
    return list(unique.keys())[0]

print(solution(A))