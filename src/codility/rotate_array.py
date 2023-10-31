

def solution(A, K):
    # Implement your solution here
    if not A:
        return []
    rot = K % len(A)
    A = A[-rot:] + A[:-rot]
    return A

array = []
R = 1 # [3,1,2] -> array[]

print(solution(array, R))