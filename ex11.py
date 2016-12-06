# -*- coding: utf-8 -*-

# Exercise 11: Asking Questions

print "How old are you?",
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heav." % (
    age, height, weight)

# How old are you? 38
# How tall are you? 6'2"
# How much do you weigh? 180lbs
# So, you're '38' old, '6\'2"' tall and '180lbs' heavy.

# Because the return type of raw_input() is string, so
# if the input contains quote marks, it would be escaped.

s = raw_input('--> ')
# --> Monty Python's Flying Circus
s
# "Monty Python's Flying Circus"

raw_input(["Show me your money"])
# ['Show me your money']haha
# 'haha'

# Q: What's the difference between input() and raw_input()?
# A: The input() function will try to convert things you
#    enter as if they were Python code, but it has security
#    problems so you should avoid it. Why?
