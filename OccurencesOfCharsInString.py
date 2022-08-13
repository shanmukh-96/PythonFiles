str1 = input("Enter a String: ")

char = str1[0]

counter = 0

output=''

for ch in str1:
    if ch in char:
        counter += 1
    else:
        output = output+str(counter)+char
        char = ch
        counter = 1
        
output = output+str(counter)+char
print(output)