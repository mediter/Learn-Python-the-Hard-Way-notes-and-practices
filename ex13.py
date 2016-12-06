# -*- coding: utf-8 -*-

# Exercise 13: Parameters, Unpacking, Variables

# an "import." is how you add features to your
# script from the Python feature set. Rather
# than give you all the features at once, Python
# asks you to say what you plan to use. This
# keeps your programs small, but it also acts
# as documentation for other programmers who
# read your code later.

# The argv is the "argument variable"
from sys import argv

#  "unpacks" argv so that, rather than holding
#  all the arguments, it gets assigned to four
#  variables you can work with: script, first,
#  second, and third. This may look strange,
#  but "unpack" is probably the best word to
#  describe what it does. It just says, "Take
#  whatever is in argv, unpack it, and assign
#  it to all of these variables on the left
#  in order."
script, first, second, third = argv

# What's the difference between argv and raw_input()?
#  The difference has to do with where the user is
#  required to give input. If they give your script
#  inputs on the command line, then you use argv.
#  If you want them to input using the keyboard
#  while the script is running, then use raw_input().

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# Input -> python ex13.py
# Traceback (most recent call last):
#   File "ex13.py", line 7, in <module>
#     script, first, second, third = argv
# ValueError: need more than 1 value to unpack

# Input -> python ex13.py kiwi
# Traceback (most recent call last):
#   File "ex13.py", line 25, in <module>
#     script, first, second, third = argv
# ValueError: need more than 2 values to unpack

# Input -> python ex13.py kiwi pear
# Traceback (most recent call last):
#   File "ex13.py", line 25, in <module>
#     script, first, second, third = argv
# ValueError: need more than 3 values to unpack

# Input -> python ex13.py apple orange grapefruit
# The script is called: ex13.py
# Your first variable is: apple
# Your second variable is: orange
# Your third variable is: grapefruit

# Are the command line arguments strings?
#  Yes, they come in as strings, even if
#  you typed numbers on the command line.
#  Use int() to convert them.

int(raw_input())

# Input -> haha
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: 'haha'
