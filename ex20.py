# Exercise 20: Functions and Files

from sys import argv

script, input_file = argv

def print_all(reading):
    """print all the file content"""
    print reading.read()

# use the seek function to move the reading point.
# file.seek = seek(...)
#    seek(offset[, whence]) -> None.
#
#    Argument offset is a byte count.  Optional argument
#    whence defaults to 0 (offset from start of file,
#    offset should be >= 0); other values are 1 (move
#    relative to current position, positive or negative),
#    and 2 (move relative to end of file, usually negative,
#    although many platforms allow seeking beyond the end
#    of a file).  If the file is opened in text mode, only
#    offsets returned by tell() are legal.  Use of other
#    offsets causes undefined behavior. Note that not all
#    file objects are seekable.

def rewind(reading):
    """This function would move the reading point to the beginning"""
    reading.seek(0)

def print_a_line(line_count, reading):
    """print the file content one line at a time"""
    print line_count, reading.readline()

current_file = open(input_file)

print "First, let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

# current_line = 1
# print_a_line(current_line, current_file)

# current_line += 1
# print_a_line(current_line, current_file)

# current_line += 1
# print_a_line(current_line, current_file)

for current_line in 1, 2, 3:
    print_a_line(current_line, current_file)

current_file.seek(0)
print current_file.readline(1)
current_file.seek(2)
print current_file.readline(5)
current_file.seek(-10, 2)
print current_file.readline(1)

# newline escape sequence is 1 byte.
# space is also 1 byte.
