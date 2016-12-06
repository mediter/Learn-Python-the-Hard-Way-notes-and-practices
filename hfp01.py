# -*- coding: utf-8 -*-

from random import randint

secret = randint(1, 20)

guess = 0

while guess != secret:
    g = raw_input("Guess the number: ")

    guess = int(g)

    if guess < secret:
        print "too low"
    elif guess > secret:
        print "too high"

print "You win!\nGame Over!"