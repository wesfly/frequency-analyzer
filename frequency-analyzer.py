string = input("Put your string here: ")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

counter_list = []

for i in range(0, len(alphabet)):
    count = string.count(alphabet[i])
    counter_list.extend([count])
    #print(alphabet[i], count)

print("Total length:", len(string))
full_list = dict(zip(alphabet, counter_list))
# print(alphabet)
# print(counter_list)
print(full_list)