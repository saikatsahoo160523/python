#1. Write a Python program to read an entire text file and print its contents.

f=open("File.txt","w+")
f.write("hello...!!!")
f.seek(0,0)
print(f.read())
f.close()
''' OUTPUT :
[root@python FileHandling]# python Ass1.py
hello...!!!
 '''
