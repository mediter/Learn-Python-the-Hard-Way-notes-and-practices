# -*- coding: utf-8 -*-

# Exercise 10: What was That?

# This \ (backslash) character encodes difficult-to-type
# characters into a string. There are various "escape
# sequences" available for different characters you might
# want to use. We'll try a few of these sequences so you
# can see what I mean.

# An important escape sequence is to escape a single-quote
# ' or double-quote ". You need a way to tell Python that
# the " inside the string isn't a real double-quote.

# To solve this problem you escape double-quotes and
# single-quotes so Python knows to include in the string.
# Here's an example:

print "I am 6'2\" tall."
print 'I am 6\'2" tall.'

# Escape double quote enclosed by double-quotes
# Escape single quote enclosed by single-quotes


# Another method: using triple-quotes

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ just a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# All of the "Escape Sequences" Python supports:
# \\  Backslash (\)

# *--------------------*
# \'  Single-quote (')

# *--------------------*
# \"  Double-quote (")

# *--------------------*
# \a  ASCII bell (BEL)

# *-----------------------*
# \b  ASCII backspace (BS)
print "test\bproficient"
# Output -> tesproficient

# *-----------------------*
# \f  ASCII formfeed (FF)
print "persian\fsexgod"
# Output -> persian
#                  sexgod

print "1\f2\f3\f4\f5"
# Output -> 1
#            2
#             3
#              4
#               5


# *----------------------*
# \n  ASCII linefeed (LF)

# ******************************************************** #
# Difference between \n and \r?                            #
#                                                          #
# In terms of ascii code, it's 3                           #
# -- since they're 10 and 13 respectively;-).              #
#                                                          #
# But seriously, there are many:                           #
# 1. in Unix and all Unix-like systems, \n is the          #
#    code for end-of-line, \r means nothing special.       #
#    As a consequence, in C and most languages that        #
#    somehow copy it (even remotely), \n is the standard   #
#    escape sequence for end of line (translated to/from   #
#    OS-specific sequences as needed)                      #
# 2. in old Mac systems (pre-OS X), \r was the code        #
#    for end-of-line instead                               #
# 3. in Windows (and many old OSs), the code for end       #
#    of line is 2 characters, \r\n, in this order          #
# 4. as a (surprising;-) consequence (harking back         #
#    to OSs much older than Windows), \r\n is the          #
#    standard line-termination for text formats on         #
#    the Internet                                          #
# 5. for electromechanical teletype-like "terminals",      #
#    \r commands the carriage to go back leftwards until   #
#    it hits the leftmost stop (a slow operation), \n      #
#    commands the roller to roll up one line (a much       #
#    faster operation) -- that's the reason you always     #
#    have \r before \n, so that the roller can move while  #
#    the carriage is still going leftwards!-)              #
# 6. for character-mode terminals (typically emulating     #
#    even-older printing ones as above), in raw mode,      #
#    \r and \n act similarly (except both in terms of      #
#    the cursor, as there is no carriage or roller;-)      #
#                                                          #
# In practice, in the modern context of writing to a       #
# text file, you should always use \n (the underlying      #
# runtime will translate that if you're on a weird OS,     #
# e.g., Windows;-). The only reason to use \r is if        #
# you're writing to a character terminal (or more          #
# likely a "console window" emulating it) and want the     #
# next line you write to overwrite the last one you        #
# just wrote (sometimes used for goofy "ascii animation"   #
# effects of e.g. progress bars) -- this is getting        #
# pretty obsolete in a world of GUIs, though;-).           #
# ******************************************************** #


# *---------------------------------------------*
# \N{name}  Character named name in the Unicode
#           database (Unicode only)
print u"\N{AMPERSAND}"
# Output -> &

# *-----------------------*
# \r  Carriage Return (CR)
while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,

# ************************************************* #
# Since the condition is always True, the sequence  #
# would be executed indefinitely. It is shown as a  #
# spinning / with 45º interval.                     #
#                                                   #
# \r Carriage Return would move the insertion point #
# to the begining of the line it appeared in.       #
# ************************************************* #


# *-----------------------*
# \t  Horizontal Tab (TAB)

# *-------------------------------------------*
# \uxxxx  Character with 16-bit hex value xxxx
#         (u'' string only)

# *----------------------------------------------------*
# \Uxxxxxxxx  Character with 32-bit hex value xxxxxxxx
#             (u'' string only)

# ******************************************* #
# If you use \N{name} or \U or \u then you'll #
# need to put a u in front of the string      #
# ******************************************* #

# *----------------------------------------*
# \v  ASCII vertical tab (VT)

# ************************************************* #
# \v is \x0b:                                       #
# '\v'                                              #
# Output -> '\x0b'                                  #
# but the string literal representation in Python   #
# is using the \x0b notation instead.               #
#                                                   #
# The Python string literal representation only     #
# ever uses \n, \r and \t, everything else that     #
# is not a printable ASCII character is represented #
# using the \xhh notation instead.                  #
#                                                   #
# \x0c is a form feed; it forces a printer to move  #
# to the next sheet of paper. You can also express  #
# it as \f in Python:                               #
# '\f'                                              #
# Output -> '\x0c'                                  #
#                                                   #
# In terminals the effects of \v and \f are often   #
# the same.                                         #
# ************************************************* #

# *----------------------------------------*
# \ooo  Character with octal value ooo

# *----------------------------------------*
# \xhh  Character with hex value hh
