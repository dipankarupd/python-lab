fo = open("file1.txt", "r")
newFile = open("result.txt", "w")

lines = fo.readlines()
print(len(lines))
for i in range(len(lines)):
    if (i+1) % 2 != 0:
        newFile.write(lines[i])

fo.close()
newFile.close()
