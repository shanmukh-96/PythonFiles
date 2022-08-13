str = input("Enter a String: ")
n = int(input("Enter a number: "))

count = {}

words = str.split()

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
        
word_list = []

for key in count:
    if count[key]>=n:
        word_list.append(key)
        
print(word_list)