# -*- coding: utf-8 -*-

# Exercise 16: Reading and Writing Files

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

# use 'rw' as 2nd parameter for open() cause error:
# IOError: [Errno 22] Invalid argument
#
# File can be opened in read mode or write mode,
# but both at the same time.

# the second parameter in open() indicate mode:
# r for read, w for write

print "Truncating the file. Goodbye!"

# the following line of code is unnecessary, because
# openning a file with 'w' as mode will truncate the
# file if it already exist.
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

# the following 6 lines of code are a bit messy.
#
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

# if we didn't use r as part of the 2nd parameter
# in open(), this would produce the following error:
# IOError: File not open for reading

print "And finally, we close it."
target.close()

# file content is changed after the written
# file is closed. If we put the following
# two lines before target.close(), nothing
# will be printed.
content = open(filename, 'r')

# If the next line of code is active, readline
# function would only output newline. So we can
# deduce that read() and readline() are continuous
# reading if we did not reset the insertion point.
# print content.read()

print "Read 1 byte of content:\n%s" % content.readline(1)
# Retain newline.  A non-negative size argument limits the maximum
# number of bytes to return (an incomplete line may be returned then).
# Return an empty string at EOF.

print "Read 1st line of content:\n%s" % content.readline()

print "Read the followine line of content:\n%s"\
   % content.readline()

# open(filename) also opens the file in 'r' (read) mode,
# since that is the default mode.

content.close()
