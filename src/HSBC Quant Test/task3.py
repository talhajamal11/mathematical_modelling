def solution(S):
    # Implement your solution here
    answer = []
    dig = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
    # Count the number of occurrences of each number
    hashmap = {}
    for i in range(len(S)):
        hashmap[S[i]] = 1 + hashmap.get(S[i], 0)
    for digit in dig:
        try:
            c = hashmap[digit]
        except:
            continue
        length = len(answer)
        if length % 2 == 0:
            if c > 0:
                answer = answer[: length // 2] + [digit] * c + answer[length // 2:]
        else:
            if digit == '0':
                if len(answer) != 1:
                    answer = answer[:length // 2] + [digit] * (c // 2) + [answer[length // 2]] + [digit] * (c // 2) + answer[length // 2 + 1:]
            else:
                if c >= 2:
                    answer = answer[:length // 2] + [digit] * (c // 2) + [answer[length // 2]] + [digit] * (c // 2) + answer[length // 2 + 1:]
    res = ''.join(answer).lstrip('0')
    return res if res else '0'

print(solution('39878'))