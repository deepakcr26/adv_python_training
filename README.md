# adv_python_training

2nd December'2019
-----------------
File
----
	- open
	- read/write
	- close
fileObj = open("/Users/deepakcr/pgadmin.log")
dir(fileObj)
fileObj.read()
.readline()
.readlines()
.close()

=> open(filename, optionalParams)
optionalParams:
    r   read only
    w   write only (Truncate and writes freshly)
    a   write only (At the EOF)
    r+  read and write at any place
    w+  write and read
    a+  append and read

False   True
0       1
""      "data"
[]      [data]
()      (data)
{}      {data}

sys.argv => returns list of args from cmd line in string format
--------

ex: prg.py These are the parameters
    [0]     [1]    [2] [3]  [4]

Byte compiled file(*.pyc) => Python's mother tongue - It is a cross platform non executable 
Optimized Byte compiled file (*.pyo)    


in 2.x
*.py => *.pyc
python -O => import <module> => *.pyo

in 3.x
*.py =>
__pycache__ / *.cpython-37.pyc
python -O => import <module> =>  __pycache__ / *.cpython-37.opt-1.pyc

package:
__init__.py

python scripts vs python modules

Magic methods: dunder methods : __init__(self) __del__(self) => Are hooked on to certain events and are called respectively
No concept of allocation or de-allocation of memory => Dynamic Typing -> Depending on the value of object, the class/type of the object is determined

Inheritance => Depth First left to right

3rd December'2019
-----------------
Python debugger
---------------
pdb
python -m pdb scopex.py => ? -> To list the options available for debugging
ll => long listing
b -> list all breakpoints
b <line number> -> set breakpoint for line
c -> continue
s -> step
p <variables>  => Print values [p a,b,c,d]
u or up -> up [Go to previous step]
d or down -> down [Go to next step]
bt -> backtrace (How did we reach here to the current step?)
condition:
condition <breakpoint_number> <condition>
condition 1 ctr >= 8340 and ctr <= 8373
commands:
commands <breakpoint_number>
    <Provide Commands>
    c to continue
commands 1
    p ctr
    c

list
map, filter
l=[n*n for n in range(6)]
l=[n*n for n in range(26) if ((n*n)%2 == 0) if ((n*n)%5 == 0)]
l=[n*n for n in range(26) if ((n*n)%2 == 0) and ((n*n)%5 == 0)]
l=[n*n for n in range(26) if ((n*n)%2 == 0) or ((n*n)%5 == 0)]

Regular Expressions:
-------------------
glob expressions(wildcard characters)
    ex: ls *.py
    ?   -> Any single character
    *   -> Any multiple characters
    []  -> single character in the range    [a-z] [a-zA-Z0-9] [aeiou]
    [!] -> single character in the Negated range    [!a-z] [!a-zA-Z0-9] [!aeiou]
grep < sed < awk
Regular Expressions (RE, regex)
    .   -> Any single character
    ?   -> 0 or 1 occurance of previous RE  ab?c => ac or abc
    *   -> 0 or more occurance of previous RE  ab*c => ac or abc or abbbbbc
    +   -> 1 or more occurance of previous RE  ab*c => abc or abbbbbc
    []  -> Similar to glob expressions
    [^] -> Similar to glob expressions

    import glob
    print(glob.glob("*.py"))    => prints all python files in the CWD

    import re
    help(re)
    (.*) -> Greedy match
    (.*?) -> Non-Greedy match
        line = "She sells sea shells on the sea shore"
        matchObj = re.match(r'(.*) sea (.*?)(.*)', line, re.M | re.I)
    r'<contents>' -> ignore from python interpreter and the contents will be parsed in raw mode by re package

    line = "some text in this string"
    list_words = re.split(r'\s', line)

Socket Programming:
------------------
-> Network Communication between 2 or more boxes (systems)
physical address: MacAddress
logical address: IPAddress

Ideally network card reads the packets that are addressed to self or the packets that are broadcasted to everyone
Sniffer reads all the packets and looks for certain patterns (NIA, RAW, intelligence services, etc)

sub-net mask (255.255.255.0) - determines if IP's are in subnet => Local network (Ex: 192.168.1.12 & 192.168.1.15)
For Local -> ARP cache (Address Resolution Protocol) => IP + MacAddress
If MacAddress is not present in ARP cache -> ARP Broadcast => Asks for MacAddress by giving IP

Till the MacAddress is determined the packets are cached.
Broadcast cannot pass thru Routers

In different Sub-net 
(Ex: 192.168.1.12 & 192.168.2.12)   -> IPs
(    192.168.1.1 & 192.168.2.1) -> Subnets (Routers) <-> Default Gateway [It has more than one Network cards]
sub-net mask (255.255.255.0)    -> To check the bytes of address on the packets

Socket <=> Electrical Socket
Communication endpoint

2 types of sockets:
- unix socket
- inet socket

ls -l /var/run/syslog   In Linux: ls -l /dev/log
srw-rw-rw-  1 root  daemon  0 Dec  2 09:27 /var/run/syslog

import socket
sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
STREAM  ->  TCP/IP  

DGRAM   ->  UDP/IP  {Unreliable, }
Weather forecast if 10% data loss from satelite, it is still ok. We can still plot graphs

PORT: Once the packet arrives to destination Box (IP), we need to send it to the appropriate Process, this is done using PORT

sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sd.bind => bind a name to the socket

server:
socket (socket.socket)
bind    -> bind address to socket
listen  -> marks the socket as listener and specifies number of connections that can wait
accept  -> Accepts incoming connection and returns new socket descriptor
read
write

client:
socket
connect
read
write

4th Dec'2019
------------
subprocess (OS module)
----------------------
Used to execute OS commands => Cannot capture the output
import subprocess   import OS
subprocess(["attrib", "-h"])    -> Windows
subprocess(["ls", "-l"])        -> Linux (Mac)

output = subprocess.check_output(["ls", "-l"])
print("Output is: {}".format(output))
print("Output is: {} bytes".format(len(output)))

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

MultiThreading
--------------
UnitTesting
-----------
doctest module
unittest module
    python unitTest_mod.py -v => for verbose
    python -v unitTest_mod.py => for full verbose
Test Discovery
python -m unittest discover -s MyTests -p *.py -v
python -m unittest discover -s MyTests -p '*.py' -v