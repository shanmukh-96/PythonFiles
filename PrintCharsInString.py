# Input:
# a6b5c3

# Output:
# aaaaaabbbbbccc

str1 = input("Enter a String: ")

output = ''

for c in str1:
    if c.isalpha():
        char = c
    else:
        counter = int(c)
        output = output+(char*counter)

print(output)