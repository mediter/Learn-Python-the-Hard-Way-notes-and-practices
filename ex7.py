# -*- coding: utf-8 -*-

# Exercise 7: More Printing

print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 12  # what would that do?

end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

# watch that comma at the end.
# try removing it to see what happens

print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

# Shorthand for printing a string multiple times
# string * number [the number can only be an integer]
print "*" + "." * 12 + "*"
print "*", "." * 12, "*"

# Use the comma inline in print would also add a
# space between the elements.

# Now without the comma in the middle
print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12

print "Summary"
print "1. When using a comma at EOL after a print statement,",
print "the result of the next print statement will follow in",
print "the same line with a space added in between them."
print "2. Otherwise, it would print on separate lines."
