import subprocess
import os
SEP = "_"*50

""" Using subprocess Module """
process = subprocess.Popen(["python", "fileSample.py", "fileSample.py"],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
print("From subprocess module, {}".format(stdout.decode()))
print(SEP)

""" Using OS Module """
process = os.popen('python fileSample.py fileSample.py')
preprocessed = process.read()
print("From OS module, {}".format(preprocessed))
process.close()
print(SEP)
