# 13. Write a Python program to combine each line from first file with the corresponding line in second file. 

with open('file2.txt') as f2, open('file1.txt') as f1:  
	for l1, l2 in zip(f2, f1):  
        	print(l1+l2) 
'''OUTPUT :
[root@python FileHandling]# cat file1.txt
Apple
Mango
Guava
Raspberry
Peach
Orange
[root@python FileHandling]# cat file2.txt
Python Exercises
[root@python FileHandling]# python Ass13.py
Python Exercises
Apple

Java ExercisesMango
'''
