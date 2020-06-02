def longest_word(file3):  
    with open(file3, 'r') as infile:  
              words = infile.read().split()  
    maxlen = len(max(words, key=len))  
    return [word for word in words if len(word) == maxlen]  
print(longest_word('file3.txt'))
