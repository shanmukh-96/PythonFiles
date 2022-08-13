Sorting a String with Alphabets and numbers,
first print sorted alphabets and then sorted numbers

Input:
n2m4n5v3a6i87

output:
aimnnv234578

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
