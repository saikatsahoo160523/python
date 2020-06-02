# 10. Write a Python program to get the file size of a plain file. 

def file_size(python):  
        import os  
        statinfo = os.stat(python)  
        return statinfo.st_size  
print("File size in bytes of the File3 is : ", file_size("file3.txt"))  

'''OUTPUT :
[root@python FileHandling]# python Ass10.py
('File size in bytes of the File3 is : ', 41)'''
