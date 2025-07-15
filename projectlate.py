file = open("code2.txt", "r")
print(file.read())
file.close()

file1 = open("code2.txt", "w")
print(file1.write("hello, this is write mode."))
file1.close()

file2 = open("code2.txt", "a")
file2.write("This file is in append mode.")
file2.close()