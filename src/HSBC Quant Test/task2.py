def solution(A):
    # Implement your solution here
    def sum_of_digits(num): # Function to find the sum of digits of any number
        total = 0
        while num:
            total += (num % 10)
            num = num // 10
        return total
    
    result, hashmap = -1, {} # Initialize result to -1 and hashmap to store sums
    
    for i in range(len(A)):
        number = A[i]
        curr_sum = sum_of_digits(number)
        if curr_sum not in hashmap:
            hashmap[curr_sum] = number
        else:
            result = max(result, number + hashmap[curr_sum])
            hashmap[curr_sum] = max(hashmap[curr_sum], number)
            
    return result

print(solution([22, 1003, 1021, 4000]))