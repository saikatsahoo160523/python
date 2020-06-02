# 11. Write a Python program to write a list to a file. 

MyFruits = ['Apple', 'Mango', 'Guava', 'Raspberry', 'Peach', 'Orange']   
with open('file1.txt', "w") as file:   
  for f in MyFruits:   
    file.write("%s\n" % f)       
content = open('file1.txt')   
print(content.read())   

''' OUTPUT :
[root@python FileHandling]# python Ass11.py
Apple
Mango
Guava
Raspberry
Peach
Orange
'''
