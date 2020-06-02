# 14. Write a Python program to read a random line from a file.

import random
l = open("file2.txt").read().splitlines()
print random.choice(l)

'''OUTPUT :
[root@python FileHandling]# cat file2.txt
Python Exercises
Java Exercises
[root@python FileHandling]# python Ass14.py
Java Exercises'''
