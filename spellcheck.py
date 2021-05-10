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
		
commonWords = {}
with open("commonWords2.txt", "r") as bfile:
    for index, word in enumerate(bfile): 
        commonWords[word.strip()] = index

print(commonWords)


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
            
final_list = []
for i,word in enumerate(words):
    brutelist = []
for word in words:
    if not trie.is_word(root, word.lower()) and word not in goodPunc:
        brutelist = trie.brute_force1(root, word) + list(trie.brute_force2(root, word))
        brutelist = set(brutelist)

        found = False
        for index in range(len(word)):
            prefix = word[:len(word)-index]
            isPrefix = trie.find_prefix(root, prefix)
            if isPrefix[0] and len(prefix) > 2:
                
                suggestions = []
                node = trie.find_prefix_node(root, prefix)
                trie.in_order_print(node, suggestions, prefix, word)
                
                #Compare
                '''
                bestOption=""
                closeness = 5
                for brute in brutelist:
                    if brute in suggestions:
                        final_list.append(brute) 
                        found = True
                        if closeness >= abs(len(word) - len(brute)): 
                            bestOption = brute
                            closeness = abs(len(word) - len(brute))

                '''
                bestOption=""
                lowestRank = 10000 
                for brute in brutelist:
                    if brute in suggestions:
                        final_list.append(brute) 
                        if brute in commonWords: 
                            found = True
                            tempRank = commonWords[brute]
                            if tempRank < lowestRank: 
                                bestOption = brute 

                if bestOption:
                    words[i] = bestOption
                    
                if found:
                    break


                bestOption=""
                closeness = 5
                for brute in brutelist:
                    if brute in suggestions:
                        final_list.append(brute) 
                        found = True
                        if closeness >= abs(len(word) - len(brute)): 
                            bestOption = brute
                            closeness = abs(len(word) - len(brute))

                if bestOption:
                    words[i] = bestOption 

                if found:
                    break
                    
                if not found and len(prefix) == 3:
                    print(word)
                    suffix = []
                    temp = ""
                    trie.reverse_prefix(node,suffix, prefix,temp, word)

                    maxSuffix = ""
                    for suff in suffix:
                        if len(suff) > len(maxSuffix):
                            maxSuffix = suff

                    print(maxSuffix)

                    for sugg in suggestions:
                        if maxSuffix in sugg: 
                            words[i] = sugg


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
for word in words:
    print(f'{word} ')     
  	

# TODO run through sentences


# vim: set sts=4 sw=4 ts=8 expandtab ft=python:

