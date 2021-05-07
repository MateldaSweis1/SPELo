#!/usr/bin/env python3

import trie

# initialize trie
root = trie.TrieNode('*')

# loop through lines(words) in a file and store in trie
with open("studentMachineDict.txt","r") as afile:
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
	isWord = trie.is_word(root, word.lower())
	print(f"{word} {isWord}")


final_list = []
for word in words:
    brutelist = []
    if not trie.is_word(root, word.lower()):
        brutelist = trie.brute_force1(root, word) + list(trie.brute_force2(root, word))
        brutelist = set(brutelist)
        for index in range(len(word)):
            prefix = word[:len(word)-index]
            isPrefix = trie.find_prefix(root, prefix)
            if isPrefix[0] and len(prefix) > 2:
                
                suggestions = []
                node = trie.find_prefix_node(root, prefix)
                trie.in_order_print(node, suggestions, prefix, word)
                                
                                #Compare 
                for brute in brutelist:
                    if brute in suggestions:
                        final_list.append(brute)

				#print(suggestions)
				#print()

				#reverse = []
				#trie.reverse_print(node,reverse, prefix, word)
				#print(reverse)
				#print()

		#temp = ""
		#suffix = []
		#trie.reverse_prefix(node,suffix, prefix,temp, word)
				#print(suffix)
				#print()
                                
        #print(word)
				#print()
				#print(prefix)
         
print(final_list)        	
# TODO run through sentences

# TODO grammar check algorithm

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
