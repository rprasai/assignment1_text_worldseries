# reading the file
text_file = open("text.txt", "r")
temp = text_file.read()

# formatting the file to lower and splitting to make a list.
temp = temp.lower()
temp = temp.split()

# listing special characters in the text file for count consistency
special_char = [
    "-",
    ",",
    ".",
    "'",
    " ",
]

# removing the special characters
text_list = []
for word in temp:
    for char in special_char:
        word = word.replace(char, "")
        if char == special_char[-1] and word:
            text_list.append(word)
# print(text_list)

# counting the words and creating the dictionary
word_count = {}

# count = 0
for word in text_list:
    # count = text_list.count(word)
    # word_count[word] = count
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# closing the original text file.
text_file.close()
