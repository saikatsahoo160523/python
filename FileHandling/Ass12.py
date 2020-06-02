# 12. Write a Python program to copy the contents of a file to another file . 

from shutil import copyfile
import os
os.system("touch file3.txt ")
copyfile('file1.txt', 'file3.txt')
'''[root@python FileHandling]# cat file1.txt
Apple
Mango
Guava
Raspberry
Peach
Orange

[root@python FileHandling]# cat file3.txt
Apple
Mango
Guava
Raspberry
Peach
Orange'''
