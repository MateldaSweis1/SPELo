#!/usr/bin/env python3

import trie
import re

# initialize trie
root = trie.TrieNode('*')

# loop through lines(words) in a file and store in trie
with open("testdict.txt", "r") as afile:
#with open("studentMachineDict.txt","r") as afile:
    for line in afile:
        word=line.strip()
	# add word to trie
        trie.insert(root, word)
		
# TODO recieve user input

# remove wacky punctuation from text and
# save words as a list with standard punctuation stored as separate items in the list
wackyPunc = '[]{}()`<>\@#^_~' #"wacky" punctuation
goodPunc = '\'!-;:"|,\.?$%&*+=/'
words = []

with open("userin.txt","r") as afile:
    for text in afile:  # text refers to each line in the file
        for let in text:
            if let in wackyPunc:
                text = text.replace(let, "")
        text = text.split()
        index = 0
        for word in text:
            for letter in word:
                if letter in goodPunc:
                    word = word.translate({ord(letter): None})
            if word  == "" : #accounts for case where wacky symbol is orignially surrounded by spaces before it gets replaced with ""
                continue 
            words.append(word)
            if letter in goodPunc:
                words.append(letter)

print(words)	
# TODO spell check algorithms

for i in range(len(words)-1):
    if words[i] == '.' or word == '!' or word == '?':
            words[i+1] = words[i+1].capitalize()
for word in words:
        if word in goodPunc:
            print(f"{word} Punctuation")
        else:
            isWord = trie.is_word(root, word.lower())
            print(f"{word} {isWord}")

for word in words:
    if not trie.is_word(root, word.lower()) and word not in goodPunc:
        for index in range(len(word)):
            prefix = word[:len(word)-index]
            isPrefix = trie.find_prefix(root, prefix)
            if isPrefix[0] and len(prefix) > 2:
                print(word)
                print()
                print(prefix)

                suggestions = []
                node = trie.find_prefix_node(root, prefix)
                trie.in_order_print(node, suggestions, prefix, word)

                print(suggestions)
                print()

			#reverse = []
			#trie.reverse_print(node,reverse, prefix, word)
			#print(reverse)
			#print()

                temp = ""
                suffix = []
                trie.reverse_prefix(node,suffix, prefix,temp, word)
                #print(suffix)
                #print()

	
# TODO run through sentences

# TODO grammar check algorithm


