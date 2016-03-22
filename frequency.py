#!/usr/bin/env python3
import string

class alphabet:
    def __init__(self,alphabet):
        self.alphabet = alphabet

    def count_freq(self,text):
        self.count = 0
        
        for word in text:
            if word.lower() == self.alphabet:
                self.count += 1
        self.percentage = (float(self.count)/float(len(text)))*100


class code:
    def __init__(self,encrypted_code=""):
        if not encrypted_code:
            print("Word Frequency Analyzer\n")
            encrypted_code = input("Enter string to analyze : ")
        alphabets = [alphabet(i) for i in string.ascii_lowercase]
        
        print("\n+==================================+")
        print("+  Alphabet : Count :  Percentage  +")
        print("+==================================+")
        for letter in alphabets:
            letter.count_freq(encrypted_code)

            if letter.count > 0:
                print("+{:^11}|{:^7}|{:^14.5}+".format(letter.alphabet,letter.count,(str(letter.percentage)+"%")))
        print("+==================================+")


if __name__ == "__main__":
    app = code()