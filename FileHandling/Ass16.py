# 16. Write a Python program to remove newline characters from a file.

def remove_newlines(file3):  
    filelist = open(file3).readlines()  
    return [s.rstrip('\n') for s in filelist]    
print(remove_newlines("file3.txt")) 

''' OUTPUT :
[root@python FileHandling]# cat file3.txt
Apple
Mango
Guava
Raspberry
Peach
Orange
[root@python FileHandling]# python Ass16.py
['Apple', 'Mango', 'Guava', 'Raspberry', 'Peach', 'Orange']
'''
