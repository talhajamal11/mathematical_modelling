""" 
You have a string of letters. Return the number of letters whose lowercase count matches the uppercase count, 
but stop counting the lower case ones after the first occurence of an uppercase character of that type.
"""

string1 = "aAbBcC" # Expected Output : 3
string2 = "AaBb" # Expected Output: 0
string3 = "abBb" # Expected Output: 1

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

print(matching_counts(string1))
print(matching_counts(string2))
print(matching_counts(string3))
