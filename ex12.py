# -*- coding: utf-8 -*-

# Exercise 12: Prompting People
import os

for i in range(1, 100):
    if (i < 10):
        print "- 0%d" % i,
    else:
        print "- %d" % i,
    if (i % 10 == 0):
        print "\n"

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# How old are you?  38
# How tall are you?  6'2"
# How much do you weigh?  180lbs
# So, you're '38' old, '6\'2"' tall and '180lbs' heavy.

print "%r" % os.__getattribute__('linesep')
# '\n'

print "%r" % os.curdir
# '.'

print "%r" % os.defpath
# ':/bin:/usr/bin'
