string = input("Put your string here: ").lower()


# all characters that will be detected
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' , ' ', '!', "?"]


counter_list = []
word_length_counter = 0
sentence_length_counter = 0
words = string.split(" ")
sentences = string.split(".")


# character counter, writes a raw list of character frequency
for i in range(0, len(alphabet)):
    individual_character_count = string.count(alphabet[i])
    counter_list.extend([individual_character_count])

# zip alphabet and raw list to make a dictionary
full_dict = dict(zip(alphabet, counter_list))


# average word length calculator
for i in range(0 ,len(words)):
    word_length_counter += len(words[i])

average_word_length = word_length_counter / len(words)


# average sentence length calculator
for i in range(0 ,len(sentences)):
    sentence_length_counter += len(sentences[i])

average_sentence_length = sentence_length_counter / len(sentences)


# visualisation chart
for i in range(0, len(alphabet)):
    value = full_dict.get(alphabet[i])
    if alphabet[i] == " ":
        print("_", end=" ")
    else:
        print(alphabet[i], end=" ")
    
    for i in range(0, value):
        print("#", end="")
    print()


print("Length of string:", len(string))
print("Words:", len(words))
print("Average word length", average_word_length)
print("Sentences:", len(sentences))
print("Average sentence length:", average_sentence_length)