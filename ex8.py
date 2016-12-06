# -*- coding: utf-8 -*-

# Exercise 8: Printing, Printing

# Recommendation: use %r only for debugging
# %r would give out "raw programmer's" version of variable
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)

print formatter % ("one", "two", "three", "four")

# Why do I have to put quotes around "one"
# but not around True or False?
#  Python recognizes True and False as keywords
#  representing the concept of true and false.
print formatter % (True, False, False, True)

print formatter % (formatter, formatter, formatter, formatter)

# if a comma is ommited in the tuple, it would cause
# TypeError: not enough arguments for format string
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

print "%s" % "中华人民共和国"
# 中华人民共和国

print "%r" % "中华人民共和国"
# '\xe4\xb8\xad\xe5\x8d\x8e\xe4\xba\xba\xe6\xb0
#  \x91\xe5\x85\xb1\xe5\x92\x8c\xe5\x9b\xbd'
# above is a binary string
