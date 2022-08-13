# Frequency of words in a String
# Input:
# Ram is a good boy. Hari is also a good boy.

# output:

def freq_words():
    str1 = input("Enter a String: ")
    
    final = {}
    
    word_list = str1.split()
    
    print(word_list)
    
    for word in word_list:
        if word in final:
            final[word] += 1
        else:
            final[word] = 1
            
    print(final)
    
freq_words()