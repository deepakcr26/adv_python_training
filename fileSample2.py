import sys
sep = "-"*50
fileName1 = "./sampleFile.txt"

fileObj = open(fileName1)
print(sep)
print("Reading Full Contents Basic Approach:\n{}".format(fileObj.read()))
print(sep)
fileObj.seek(0)
ctr = 1
print("1st Approach: \n")
for line in fileObj:
    print("{} : {}".format(ctr, line))
    ctr = ctr + 1
print(sep)


print("2nd Approach")
fileObj.seek(0)
ctr = 1
line = fileObj.readline()
while line:
    print("{}: {}".format(ctr, line))
    ctr += 1
    line = fileObj.readline()

print(sep)

print("2nd Approach without extra line")
fileObj.seek(0)
ctr = 1
line = fileObj.readline()
while line:
    print("{}: {}".format(ctr, line), end="")
    ctr += 1
    line = fileObj.readline()

fileObj.close()
print(sep)

print("3rd Approach with readlines and sys.argv")
fileName2 = sys.argv[1]
print("File name: ", fileName2)
fileObj = open(fileName2)
for index, line in enumerate(fileObj.readlines()):
    print("{} : {}".format(index + 1, line), end="")
fileObj.close()
print(sep)
