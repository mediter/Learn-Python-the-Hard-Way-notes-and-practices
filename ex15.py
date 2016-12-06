# -*- coding: utf-8 -*-

# Exercise 15: Reading Files

# the following code shows how to
# open a file in Python:
# 1. pass the filename as an argument
#    when running the script
# 2. get user input for filename when
#    the script is already running

from sys import argv

script, filename = argv

txt = open(filename)

# Q: Does txt = open(filename) return the
#    contents of the file?
# A: No, it doesn't. It actually makes
#    something called a "file object." You
#    can move around inside them, and then
#    "read" them, but the DVD player is not
#    the DVD the same way the file object
#    is not the file's contents.

print "Here's your file %r:" % filename
print txt.read()

# use the variable txt to represent the file object
# allow us to easily manipulate the content of the
# memory space ocupied by the file object.

txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()

# But:
# Type the filename again:
# > ~/Desktop/test.txt
# Traceback (most recent call last):
#   File "ex15.py", line 17, in <module>
#     txt_again = open(file_again)
# IOError: [Errno 2] No such file or directory:
#          '~/Desktop/test.txt'
# So how to open a file is in a dir other than the curdir?

# Type the filename again:
# > ../test.txt
# Exercise 15: Reading Files
