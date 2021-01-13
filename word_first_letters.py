
word_counts = {}

with open('DATA/words.txt') as words_in:
    for word in words_in:
        first_letter = word[-2]
        if not first_letter in word_counts:
            word_counts[first_letter] = 0
        word_counts[first_letter] = word_counts[first_letter] + 1

print(word_counts)