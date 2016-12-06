# -*- coding: utf-8 -*-

# Exercise 17: More Files

from sys import argv
from os.path import exists

script, source_file, dest_file = argv

print "Copying from %s to %s :" % (source_file, dest_file)

# we could do these two in one line, how?

in_file = open(source_file)
indata = in_file.read()

print "The source file is %d bytes lone" % len(indata)

print "Does the output file exist? %r" % exists(dest_file)

print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

output_file = open(dest_file, 'w')
output_file.write(indata)

output_file.close()
in_file.close()

content = open(dest_file)

print content.read()
