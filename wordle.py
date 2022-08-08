# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 14:27:19 2022

@author: abackes
"""

import random

words = []


file = open('five_words.txt')


for line in file:
    line = line.rstrip()
    words.append(line)

pick = random.randint(0,len(words)-1)
word = words[pick]

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

print("Your word for Wordle is:", word.capitalize())

    