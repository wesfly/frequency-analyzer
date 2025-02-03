'''
Quick ideas
average word length
'''
string = input("Put your string here: ").lower()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' , ' ']

counter_list = []

# character counter
for i in range(0, len(alphabet)):
    count = string.count(alphabet[i])
    counter_list.extend([count])

full_list = dict(zip(alphabet, counter_list))


word_length_counter = 0
words = string.split(" ")

# average word length calculator
for i in range(0 ,len(words)):
    word_length_counter += len(words[i])

average_word_length = word_length_counter / len(words)

print("Length of string:", len(string))
print(full_list)
print("Average word length", average_word_length)