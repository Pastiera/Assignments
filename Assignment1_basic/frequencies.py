import os
import argparse
import string
import json
import time
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description = "Shows each character's frequency present in a book." )
parser.add_argument("-path", type = str , help= "Enter the path to a book txt file to show character's frequencies.")
parser.add_argument("-hist", type = str , help= "Enter the path to a book txt file to show an histogram of the frequencies.")
args = parser.parse_args()
start = time.time()

#print of the relative frequencies and other info on the text
if args.path:

    if os.path.isfile(args.path):
        os.path.join(args.path)
    else:
        raise argparse.ArgumentTypeError("The path is invalid or doesn't exist. Please, try again or use -h command for help.")
    with open(args.path) as text_book:
        alphabet = string.ascii_lowercase
        counter_dic = dict.fromkeys(alphabet, 0)
        open_book = str(text_book.read()).lower()
        for char in open_book:
            if char in alphabet:
                counter_dic[char] += 1
        n_tot = sum(counter_dic.values())
        freq_dic = counter_dic
        for value in freq_dic:
            freq_dic[value] = (freq_dic[value]/n_tot)*100
        end1 = time.time()
        print("Total number of characters", n_tot)
        print("Relative frequency of each character, expressed as percentage:", json.dumps(freq_dic, indent=4))
        print("Time elapsed:",end1 - start, "s")

if args.hist:
    if os.path.isfile(args.hist):
        os.path.join(args.hist)
    else:
        raise argparse.ArgumentTypeError("The path is invalid or doesn't exist. Please, try again or use -h command for help.")
    with open(args.hist) as text_book:
        alphabet = string.ascii_lowercase
        counter_dic = dict.fromkeys(alphabet, 0)
        open_book = str(text_book.read()).lower()
        for char in open_book:
            if char in alphabet:
                counter_dic[char] += 1
        plt.bar(counter_dic.keys(), counter_dic.values(), color='b')
        end2 = time.time()
        print("Time elapsed:",end2 - start, "s")
        plt.show()
