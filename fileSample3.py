import sys
sep = "-"*50
srcFile = sys.argv[1]
destFile = sys.argv[2]

srcFileObj = open(srcFile)
destFileObj = open(destFile, "w")
print("Copying conetnts from {} to {}".format(srcFile, destFile))
print(sep)
content = srcFileObj.readlines()
destFileObj.writelines(content)
print("Copy complete")
srcFileObj.close()
destFileObj.close()
print(sep)
