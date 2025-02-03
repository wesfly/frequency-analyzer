'''
Quick ideas
average word length
'''
string = input("Put your string here: ").lower()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' , ' ']

counter_list = []

for i in range(0, len(alphabet)):
    count = string.count(alphabet[i])
    counter_list.extend([count])

print("Length of string:", len(string))
full_list = dict(zip(alphabet, counter_list))

print(full_list)
word_length_counter = 0
words = string.split(" ")
for i in range(0 ,len(words)):
    word_length_counter += len(words[i])

average_word_length = word_length_counter / len(words)
print("Average word length", average_word_length)