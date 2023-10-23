def checkMagazine(magazine, note):
    # Write your code here
    magazine = magazine.split(" ")
    note = note.split(" ")
    mag_words = {}
    for word in magazine:
        mag_words[word] = 1 + mag_words.get(word, 0)
    for word in note:
        if word in mag_words:
            mag_words[word] -= 1
            if not mag_words[word]:
                mag_words.pop(word)
        else: 
            print("No")
            return
    print("Yes")
    return

mag = "two times three is not four"
note = "two times two is four"
checkMagazine(mag, note)