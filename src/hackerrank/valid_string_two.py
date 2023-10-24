def substrCount(n, s):
    count = 0

    for i in range(n):
        j = i
        while j < n and s[i] == s[j]:
            j += 1
            count += 1

            if j < n:
                k = j + 1
                while k < n and s[k] == s[i]:
                    count += 1
                    k += 1
                if k < n and s[k] == s[j]:
                    count += 1
                else:
                    break

    return count

        


s = "mnonopoo"
n = len(s)
print(substrCount(n, s))