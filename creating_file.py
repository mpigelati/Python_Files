#!/usr/bin/env python

fs = open("sample.c", "r+")

fd= open("dest.txt","ab+")

fd.write("fs");	
str  =fs.read();
str1 =fd.read();

print"Read string FS: ",str
print"Read string FD: ",str

fs.close()
fd.close()

