# Finding Comman Letters b/w two Strings
# Input:
# naina
# reena

# Output:
# an


str1 = input("Enter first String: ")
str2 = input("Enter Second String: ")

s1 = set(str1)
s2 = set(str2)

final = []

for c in s1:
    if c in s2:
        final.append(c)

output = ''.join(final)

print(output)