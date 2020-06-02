#4. Write a Python program to read last n lines of a file and display the same.
import sys  
import os  
def readFile(file2,lines):  
        buffersize = 8192  
        filesize = os.stat(file2).st_size  
        iter = 0  
        with open(file2) as f:  
                if buffersize > filesize:  
                        buffersize = filesize-1  
                        data = []  
                        while True:  
                                iter +=1  
                                f.seek(filesize-buffersize*iter)  
                                data.extend(f.readlines())  
                                if len(data) >= lines or f.tell() == 0:  
                                        print(''.join(data[-lines:]))  
                                        break  
  
readFile('file2.txt',5)  

