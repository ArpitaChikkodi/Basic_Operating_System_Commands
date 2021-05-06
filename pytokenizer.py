'''
Author : Arpita Chikkodi

Date : 16-02-2021

Objective : To implement 'Tokenizer' in Python

Synopsis : 
>pytokenizer.py  -input <text file>

>python pytokenizer.py -input input1.txt
>python pytokenizer.py -input input2.txt

Details : 
To implement the following functions 
- Function that reads in a text file and returns a list of the tokens in that file. For the purpose of this project, a token is a sequence of alphanumeric characters, independent of capitalization (so Apple, apple, aPpLe are the same token). 
- Function that counts the number of occurrences of each token in the token list. 
- A method that prints out the word frequency count onto the screen. The print out should be ordered by decreasing frequency (so, the highest frequency words first)
'''

import argparse
import re
from os import path

class PyTokenizer():
    
    version = '1.0.0'
    
    def tokenize(self, input_text_file):
        ''' It tokenizes the words of given input file and returns the tokenlist ''' 
        tokenslist = []
        with open(input_text_file,'r',encoding="utf-8") as file_pointer:   #utf-8 or latin-1 encoding is used to avoid UnicodeDecode Error
            content = file_pointer.read().splitlines() #using splitlines instead of readlines to avoid newline(\n) character
            for line in content:
                tokenslist.extend([word.lower() for word in re.split(r'(\W)', str(line.split(" "))) if word.isalnum()])     #split each line into tokens by checking if it is alphanumeric or not,add the tokens to tokenslist
        return tokenslist

    def calculateWordFrequency(self,list):
        ''' This function is used to calculate and return the frequency of each word using dict '''
        compute_map = {}
        #For every word in list,it creates a dict or map to the remove duplicate words and it returns the count
        for word in list:
            if word in compute_map.keys():
                compute_map[word] = compute_map.get(word) + 1
            else:
                compute_map[word] = 1
        return compute_map

    def printSorted(self, frequency):
        ''' It sorts the dictionary in descending order based on the token frequency  '''
        for word in sorted(frequency, key=frequency.get, reverse=True):   
            print(word, frequency[word])
 
 
if __name__ == "__main__":
    ''' Main function '''
    # create parser object 
    parser = argparse.ArgumentParser(prog="PyTokenizer",description = "This is a Pytokenizer!") 
  
    # defining arguments for parser object
    parser.add_argument("-input","--input",type = str, nargs = 1, default = None, metavar = "input_text_file",help="It fetches the input text file name!",required=True)
    parser.add_argument("-v","-V","--version", action='version', version='%(prog)s '+PyTokenizer.version)
    # parse the arguments from standard input 
    args = parser.parse_args() 
    
    if((path.exists(args.input[0])) == False):
        print("File does not Exist in the path or working directory!!")
        exit()
    pytokenizer_instance = PyTokenizer()
    tokenlist = pytokenizer_instance.tokenize(args.input[0])
    token_frequency = pytokenizer_instance.calculateWordFrequency(tokenlist)
    pytokenizer_instance.printSorted(token_frequency)