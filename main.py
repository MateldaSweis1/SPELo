#!/usr/bin/env python3

import trie

# initialize trie
root = trie.TrieNode('*')

# loop through lines(words) in a file and store in trie
with open("smalldict.txt","r") as afile:
	for line in afile:
		word=line.strip()
		# add word to trie
		trie.insert(root, word)
		


# TODO recieve user input

# save words as a list without punctuation
punc = '''!()-[]{};:'"\,`<>./?@#$%^&*_~'''
with open("userin.txt","r") as afile:
	for text in afile:
		for let in text:
			if let in punc:
				text = text.replace(let,"")
		words=text.split()


# TODO spell check algorithms

# TODO run through sentences

# TODO grammar check algorithm

