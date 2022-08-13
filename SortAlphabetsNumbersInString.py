str1 = input("Enter a String: ")

alphabets = []
numbers = []

for ch in str1:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        numbers.append(ch)
        
sort_list = sorted(alphabets)+sorted(numbers)

final_output = ''.join(sort_list)

print(final_output)