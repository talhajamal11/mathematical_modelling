""" 
You have a string of letters. Count the number of different letters that appear in both uppercase and lowercase,
where all lowercase occurrences of the letters appear before the uppercase letters
"""

STRING1 = "aAbBcC" # Expected Output : 3
STRING2 = "AaBb" # Expected Output: 0
STRING3 = "abBb" # Expected Output: 1
STRING4 = "aaAbcCABBc" # Expected Output 2
def matching_counts(string):
    lowercase = {}
    uppercase = {}
    matches = 0
    for char in string:
        if char.isupper():
            uppercase[char] = uppercase.get(char, 0) + 1
            if lowercase.get(char.lower(), 0) == uppercase[char]:
                matches += 1
        elif char.islower() and char.upper() not in uppercase:
            lowercase[char] = lowercase.get(char, 0) + 1
    return matches

#print(matching_counts(string1))
#print(matching_counts(string2))
#print(matching_counts(string3))

def solution(string):
    uppercase = {}
    lowercase = {}
    for char in string:
        if char.islower():
            if char.upper() not in uppercase:
                lowercase[char] = True
            if char.upper() in uppercase:
                try:
                    lowercase.pop(char)
                except:
                    continue
        elif char.isupper():
            uppercase[char] = True
    return len(lowercase)

print(solution(STRING4))
