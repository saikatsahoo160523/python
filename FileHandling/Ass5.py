# 5. Write a Python program to read a file line by line and store it into a list. 

def file_read(python):
      with open(python) as file:             
                 content_list = file.readlines()
                 print(content_list)
file_read('file1.txt')

'''OUTPUT :
[root@python FileHandling]# python Ass5.py
['BByeee..!!!']
'''
