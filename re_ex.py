import re


def check_strings(line):
    # line = "She sells sea shells on the sea shore"

    matchObj = re.match(r'(.*) sea (.*?)( .*)', line, re.M | re.I)
    if matchObj:
        print("matchObj.group(): ", matchObj.group())
        print("matchObj.group(1): ", matchObj.group(1))
        print("matchObj.group(2): ", matchObj.group(2))
        print("matchObj.group(3): ", matchObj.group(3))
    else:
        print("No match!")


def read_contents_from_file(fileName):
    fObj = open(fileName)
    for index, line in enumerate(fObj.readlines()):
        # if line != "\n":
        #     print("{} : {}".format(index + 1, line), end="")
        # if not re.match(r'\s*$', line, re.M | re.I):
        # emptyLines = re.match(r'^$', line, re.M | re.I)
        if not re.match(r'(^$)|(#.*\n)|(\s*#.*\n)', line):
            print("{} : {}".format(index + 1, re.sub(r'#.*', '', line)), end="")


if __name__ == "__main__":
    # check_strings("She sells sea shells on the sea shore")
    read_contents_from_file("./sampleFile.txt")
