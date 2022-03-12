# Python code to
# demonstrate readlines()

L = ["Geeks\n", "for\n", "Geeks\n"]

# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()

# Using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

#

L2 = ["I am a \n", "Specialist\n", "Software \n", "Engineer"]

# write data
file2 = open('myfile2.txt', 'w')
file2.writelines(L2)
file2.close()

# using Readlines

file2 = open('myfile2.txt', 'r')
lines2 = file2.readlines()

count2 = 0

for line in lines2:
    count2 += 1
    print(line.strip())
    #print("Line{}: {}".format(count2, line.strip()))

L3 = ["I like \n", "to play \n", "Cricket"]

file3 = open("mytext3.txt", 'w')
file3.writelines(L3)
file3.close()

file3 = open("mytext3.txt", "r")
lines3 = file3.readlines()

count3 = 0

for line in lines3:
    count3 += 1
    print(line.strip())
