# -*- coding: utf-8 -*-

# Exercise 6: Strings and Text

x = "There are %d types of people." % 10

binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# Using r as conversion type, then use print would print out
# a string variable would output double quote marks in the string
# as single quote marks; using s as conversion type, the result would
# delete the quote marks.
print "I said: %r." % x
# I said: 'There are 10 types of people.'.

print "I said: %s." % x
# I said: There are 10 types of people..

print "I also said: '%s'." % y
# I also said: 'Those who know binary and those who don't.'.

hilarious = False

# Assign a string to a variable, the string
# can contain format specifier
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# String Concatenation
print w + e
