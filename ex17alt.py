# -*- coding: utf-8 -*-

# Exercise 17: More Files

from sys import argv
from os.path import exists

script, source_file, dest_file = argv

open(dest_file, 'w').write(open(source_file).read())
# would there be memory leakage?
# how to incorporate close() into the one liner?