text = "abc"

def anagrams(phrase):
    if len(phrase) <= 1:
        return [phrase]
    else:
        collection = []
        for perm in anagrams(phrase[1:]):
            for i in range(len(phrase)):
                collection.append(perm[:i] + phrase[0:1] + perm[i:])
        return collection

print(anagrams(text))