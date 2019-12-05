import sys
sep = "-"*50
fileName2 = sys.argv[1]
print("File name: ", fileName2)
fileObj = open(fileName2)
for index, line in enumerate(fileObj.readlines()):
    print("{} : {}".format(index + 1, line), end="")
fileObj.close()
print(sep)
