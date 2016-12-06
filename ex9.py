# -*- coding: utf-8 -*-

# Exercise 9: Printing, Printing, Printing

# Here's some new strange stuff, remember to type it exactly

days = "Mon Tue Wed Thu Fri Sat Sun"

# \n would make the stuff after it begin on a new line
months = "\nJan\nFeb\nMar\nApr\nMay\nJun"

# if a comma is added to the above statement, it would cause
# TypeError: can only concatenate tuple (not "str") to tuple
months = months + "\nJul\nAug\nSep\nOct\nNov\nDec"

print "Here are the days: ", days
print "Here are the months: ", months

flowers = "rose\nnarcissus",
flowers = flowers + ("tuplip", "gardenia")

print flowers
# Output -> ('rose\nnarcissus', 'tuplip', 'gardenia')
# Why "\n" does not behave as an escaped char?


# Use triple double-quotes to enclose paragraphs to be printed
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
