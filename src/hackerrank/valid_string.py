def isValid(s):
    result = 'YES'
    arr = sorted(s)  # Sort the string characters
    freq = arr.count(arr[0])
    first_letter = arr[0]
    counter = 0

    for i in range(1, len(arr)):
        if arr[i] != first_letter:
            temp_freq = arr.count(arr[i])
            if abs(freq - temp_freq) > 1 and temp_freq != 1:
                result = 'NO'
                break
            if temp_freq != freq:
                if temp_freq > freq:
                    counter += 1
                else:
                    counter += 1
                    if i == 1:
                        freq = temp_freq
            if counter > 1:
                result = 'NO'
                break
            first_letter = arr[i]

    return result

s = "aabbcd" #YES
print(isValid(s))