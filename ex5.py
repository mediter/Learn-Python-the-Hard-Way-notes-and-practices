# -*- coding: utf-8 -*-

# Exercise 5: More Variables and Printing

name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
metricHeight = height * 2.54  # cm
weight = 180  # lbs
metricWeight = weight * 0.45  # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# String and Unicode objects have one unique built-in operation:
# the % operator (modulo). This is also known as the string
# formatting or interpolation operator.
#
# If format requires a single argument, values may be a single
# non-tuple object. Otherwise, values must be a tuple with
# exactly the number of items specified by the format string,
# or a single mapping object (for example, a dictionary).
#
# If format is a Unicode object, or if any of the objects being
# converted using the %s conversion are Unicode objects, the result
# will also be a Unicode object.

# print a string that contains a formatting placeholder %s
# to replaced with data of a variable. use % after the quote
# mark to separate the format string and the variable
print "Let's talk about %s." % name

# print a format string containing %d as placeholder for a number
print "He's %d inches tall." % height

# print a format string containing %d as placeholder for a number
print "He's %d pounds heavy." % weight

print "In metric terms, his height and weight are %d cm, and %d kg respectively." % \
    (metricHeight, metricWeight)

print "Actually that's not too heavy."

# print a format string containing two %s, use (firstVar, secondVar)
# after % to reference the two variables
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right

# print a format string containing n %s, use (firstVar, secondVar, ......, n-thVar)
# after % to reference the n variables
print "If I add %d, %d, and %d I get %d." % (
      age, height, weight, age + height + weight)

# Ref: https://docs.python.org/2.4/lib/typesseq-strings.html
# A conversion specifier contains two or more characters and has
# the following components, which must occur in this order:
#
# 1. The "%" character, which marks the start of the specifier.
# 2. Mapping key (optional), consisting of a parenthesised sequence of characters
#    (for example, (somename)).
#
#    When the right argument is a dictionary (or other mapping type),
#    then the formats in the string must include a parenthesised
#    mapping key into that dictionary inserted immediately after the
#    "%" character. The mapping key selects the value to be formatted
#    from the mapping. For example:

print '%(language)s has %(#)03d quote types.' % \
    {'language': "Python", "#": 2}
#   Output –> Python has 002 quote types.

# 3. Conversion flags (optional), which affect the result of some conversion types.
# +-----+--------------------------------------------------------------+
# |Flag	|Meaning                                                       |
# +=====+==============================================================+
# |#    |The value conversion will use the ``alternate form''.         |
# |     |(where defined below).                                        |
# +-----+--------------------------------------------------------------+
# |0    |The conversion will be zero padded for numeric values.	(00002)|
# +-----+--------------------------------------------------------------+
# |-    |The converted value is left adjusted (overrides the "0"       |
# |     |conversion if both are given).                                |
# +-----+--------------------------------------------------------------+
# |     |(a space) A blank should be left before a positive number     |
# |     |(or empty string) produced by a signed conversion.            |
# +-----+--------------------------------------------------------------+
# |+    |A sign character ("+" or "-") will precede the conversion     |
# |     |(overrides a "space" flag).                                   |
# +-----+--------------------------------------------------------------+

n = 89
print "%03d" % n
# 089

print "%-03d" % n
# 89

print "%+3d" % n
# +89

print "% 3d" % n
# „89 ( here we use "„"" to denote a space in the output)

n = -89
print "%+3d" % n
# -89


# 4. Minimum field width (optional). If specified as an "*" (asterisk), the actual
#    width is read from the next element of the tuple in values, and the object to
#    convert comes after the minimum field width and optional precision.

print "% *d" % (4, n)
# „„89

# 5. Precision (optional), given as a "." (dot) followed by the precision. If specified
#    as "*" (an asterisk), the actual width is read from the next element of the tuple
#    in values, and the value to convert comes after the precision.

r = 3.1415926

print "% +3.5d" % r
# +00003

print "% +.5d" % r
# +00003

print "%.5d" % r
# 00003

print "%.3d" % r
# 003

print "% +3.5f" % r
# +3.14159

print "%03.5f" % r
# 3.14159

print "%.*f" % (3, r)
# 3.142


# 6. Length modifier (optional).
#
# 7. Conversion type.
#
# +-----+--------------------------------------------------------+
# |Type | Meaning	Notes                                        |
# +=====+========================================================+
# |d	| Signed integer decimal.                                |
# +-----+--------------------------------------------------------+
# |i	| Signed integer decimal.                                |
# +-----+--------------------------------------------------------+
# |o	| Unsigned octal.                                        |
# +-----+--------------------------------------------------------+
# |u	| Unsigned decimal.                                      |
# +-----+--------------------------------------------------------+
# |x	| Unsigned hexadecimal (lowercase).                      |
# +-----+--------------------------------------------------------+
# |X	| Unsigned hexadecimal (uppercase).                      |
# +-----+--------------------------------------------------------+
# |e	| Floating point exponential format (lowercase).         |
# +-----+--------------------------------------------------------+
# |E	| Floating point exponential format (uppercase).         |
# +-----+--------------------------------------------------------+
# |f	| Floating point decimal format.                         |
# +-----+--------------------------------------------------------+
# |F	| Floating point decimal format.                         |
# +-----+--------------------------------------------------------+
# |g	| Same as "e" if exponent is greater than -4 or less     |
# |     | than precision, "f" otherwise.                         |
# +-----+--------------------------------------------------------+
# |G	| Same as "E" if exponent is greater than -4 or less     |
# |     | than precision, "F" otherwise.                         |
# +-----+--------------------------------------------------------+
# |c	| Single character (accepts integer or single character  |
# |     | string).                                               |
# +-----+--------------------------------------------------------+
# |r	| String (converts any python object using repr() ).     |
# +-----+--------------------------------------------------------+
# |s	| String (converts any python object using str() ).      |
# +-----+--------------------------------------------------------+
# |%	| No argument is converted, results in a "%" character   |
# |     | in the result.                                         |
# +-----+--------------------------------------------------------+

# "Unsigned" means for a positive number, no plus sign would be shown
# before the number, but the minus sign would always be shown in front
# of a negative number.

# Since Python strings have an explicit length, %s conversions do not
# assume that '\0' is the end of the string.

# For safety reasons, floating point precisions are clipped to 50; %f
# conversions for numbers whose absolute value is over 1e25 are replaced
# by %g conversions.2.9 All other errors raise exceptions.
