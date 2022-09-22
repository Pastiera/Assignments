#!/usr/bin/env python3
"""First assignment.
Module: basic Python
Assignment #1 (September 30, 2019)
Download a book (not covered by copyright) in plain-text format, e.g.,
from <https://www.gutenberg.org/>
(If you have a hard time picking one, we suggest this English
translation of "The Republic" by Plato:
<http://www.gutenberg.org/cache/epub/1497/pg1497.txt>)
# Goal
Write a Python program that prints the relative frequence of each letter
of the alphabet (without distinguishing between lower and upper case) in
the book.
# Specifications
- the program should have a --help option summarizing the usage
- the program should accept the path to the input file from the command
  line
- the program should print out the total elapsed time
- the program should have an option to display a histogram of the
  frequences
- [optional] the program should have an option to skip the parts of the
  text that do not pertain to the book (e.g., preamble and license)
- [optional] the program should have an option to print out the basic
  book stats (e.g., number of characters, number of words, number of
  lines, etc.)
"""

import os
import argparse
import string
import json
import time
import matplotlib.pyplot as plt
import logging

parser = argparse.ArgumentParser(description = "Shows each letter's frequency present in a book." )
parser.add_argument('path', type = str , help= "Enter the path to a book txt file to show letter's frequencies.")
parser.add_argument("-hist", action = 'store_true' , help= "Enter the path to a book txt file to show an histogram of the frequencies.")
parser.add_argument('-debug', action = 'store_true', help= "Shows debug informations.")
start = time.time() # star counting time after user enters the path to file
args = parser.parse_args()

if args.debug:
    logging.basicConfig(level=logging.INFO)

#print of the relative frequencies and other info on the text

logging.info("Reading input file %s...", args.path)
if os.path.isfile(args.path):
    os.path.join(args.path)
else:
    raise argparse.ArgumentTypeError("The path is invalid or doesn't exist. Please, try again or use -h command for help.")
num_char = 0
alphabet = string.ascii_lowercase
counter_dic = dict.fromkeys(alphabet, 0)

logging.info("Opening %s...", args.path)
with open(args.path) as text_book:
    open_book = str(text_book.read()).lower()
    logging.info("Counting characters in %s...", os.path.basename(args.path))
    for char in open_book:
        if char in alphabet:
            counter_dic[char] += 1
        num_char += 1
    logging.info("Done")
    n_tot = sum(counter_dic.values())
    n_words = len(open_book.split())
    n_lines = len(open_book.splitlines())
    for value in counter_dic:
        counter_dic[value] = (counter_dic[value]/n_tot)*100
print(f'The text contains {num_char} characters of which {n_tot} are letters. The number of words are {n_words}, while the number of lines are {n_lines}')
print("Relative frequency of each character, expressed as percentage:", json.dumps(counter_dic, indent=4))


#print the histogram
if args.hist:
    plt.bar(counter_dic.keys(), counter_dic.values(), color='b')
    plt.show()
end = time.time()
print("Time elapsed:",end - start, "s")
