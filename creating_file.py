#!/usr/bin/env python

fs=open("sample.c","r");

fd=open("testing","ab+");
for line in fs:

	fd.write(line);
	fd.write("\n");

fs.close();
fd.close();

