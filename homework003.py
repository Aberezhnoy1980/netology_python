def build_list_of_words():
    words = []
    for i in range(0, int(input("Enter number of languages: "))):
        words.append(input("Enter the name of the language you know: "))
    return words
    
words = build_list_of_words()
searchSynbol = 'c'

def count_letter(words, symbol):
    count = 0
    for word in words:
        if symbol in word:
            count += 1
    return count

print(count_letter(words, 'c'))