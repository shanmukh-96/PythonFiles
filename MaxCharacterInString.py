# Max occurence of a character in a string

# Input:
# hello world

# Output:
# l

str = input("Enter a String: ")

count = {}

for c in str:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1
        
max_char = max(count, key = lambda x: count[x])

print(max_char)
