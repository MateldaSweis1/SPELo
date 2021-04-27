#!/usr/bin/env python3

import trie

# initialize trie
root = trie.TrieNode('*')

# loop through lines(words) in a file and store in trie
with open("testdict.txt","r") as afile:
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
for word in words:
	isWord = trie.is_word(root, word)
	print(f"{word} {isWord}")

for word in words:
	if not trie.is_word(root, word):
		for index in range(len(word)):
			isPrefix = trie.find_prefix(root, word[:len(word)-index])
			if isPrefix[0]:
				print(word[:len(word)-index])
				#suggestions = trie.find_quick_suggestion(root, word, len(word))
				#print(suggestions)	

# TODO run through sentences

# TODO grammar check algorithm

