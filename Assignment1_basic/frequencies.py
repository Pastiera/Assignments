import os
import argparse
import string
parser = argparse.ArgumentParser(description = "Shows each character's frequency present in a book." )
parser.add_argument("-path", type = str, help="Enter the path to a book txt file.")
parser.add_argument("-hist", "--histogram", help="Shows an histogram of character's frequencies.")
args = parser.parse_args()


if os.path.isfile(args.path):
    os.path.join(args.path)
else:
    raise argparse.ArgumentTypeError("The path is invalid or doesn't exist. Please, try again or use -h command for help.")
with open(args.path) as text_book:
    alphabet = string.ascii_lowercase
    counter_dic = dict.fromkeys(alphabet, 0)
    for char in str(text_book.read()).lower():
        if char in alphabet:
            counter_dic[char] += 1
    #print(str(text_book.read()).lower())
    #print(text_book.read())




print(counter_dic)
