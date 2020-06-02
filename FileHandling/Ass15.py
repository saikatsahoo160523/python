# 15. Write a Python program to assess if a file is closed or not.

f = open("file1", "wb")
print "Name of the file: ", f.name
print "Closed or not : ", f.closed

''' OUTPUT :
[root@python FileHandling]# python Ass15.py
Name of the file:  file1
Closed or not :  False'''
