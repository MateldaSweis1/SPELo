#!/usr/bin/env python3
from typing import Tuple

class TrieNode(object):

    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1

def insert(root, word: str):
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                child.counter +=1
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    node.word_finished = True

def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    node = root
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return False, 0
    return True, node.counter

def is_word(root, word: str) -> bool:
	node = root
	if not root.children:
		return False
	for char in word:
		char_not_found = True
		for child in node.children:
			if child.char == char:
				char_not_found = False
				node = child
				break
		if char_not_found:
			return False
	if node.word_finished:
		return True
	else:
		return False


def brute_force1(root, word: str):
    # Adpoted from https://norvig.com/spell-correct.html
     
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    #splitting words in every possible combination
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]

    #deleting a letter in each split
    deletes = [L + R[1:] for L,R in splits if R]

    #transposes letters in every split
    transposes = [L + R[1] + R[0] + R[2:] for L,R in splits if len(R)>1]

    #replacing letters in split with every letter in given alphabet
    replaces = [L + c + R[1:] for L,R in splits if R for c in alphabet]

    #inserting every letter from alphabet into each split
    inserts = [L + c + R for L,R in splits for c in alphabet]

    fullset = set(deletes + transposes + replaces + inserts)
    node = root
    returnlist = []
    for word in fullset:
        if is_word(node, word):
            returnlist.append(word)
    return returnlist

def brute_force2(root, word: str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return set(edits for i in brute_force1(root, word) for edits in brute_force1(root, i))

def in_order_print(root, suggestions, prefix, word):
	if(not root):
		return

	node = root 
	for child in node.children:
		start = prefix
		start += child.char
		
		node = child
		if node.word_finished:
			if(len(word)-2 <= len(start) <= len(word)+2):
				suggestions.append(start)

		in_order_print(node, suggestions, start, word)

def reverse_print(root, suggestions, prefix, word):
	if(not root):
		return

	
	reverse = "" #prefix[::-1]

	node = root 
	for child in node.children:

		start = prefix
		start += child.char

		reverse_print(child, suggestions, start, word)
		reverse +=  child.char
		node = child
		if node.word_finished:
			suggestion = reverse + prefix[::-1]
			if(len(word)-2 <= len(suggestion) <= len(word)+2):
				suggestions.append(suggestion)


def reverse_prefix(root, longestsuffix, prefix,reverse, word):
	if(not root):
		return
	
	node = root 
	for child in node.children:

		start = prefix
		start += child.char

		reverse += child.char
		node = child
		reverse_prefix(node, longestsuffix, start,reverse, word)
		if node.word_finished:
			for index in range(len(reverse)):
				suffix = reverse[index:]
				#if word.endswith(suffix):
				if suffix in word:
					if len(suffix) > len(longestsuffix):
						longestsuffix.append(suffix)


def find_prefix_node(root, prefix: str):
    node = root
    if not root.children:
        return None
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return None

    return node


def main():
    root = TrieNode('*')
    insert(root, "butterfly")
    insert(root, 'butter')
    
    print(find_prefix(root, 'but'))
    print(find_prefix(root, 'butter'))
    print(find_prefix(root, 'butterfly'))
    print(find_prefix(root, 'sun'))
    print(find_prefix(root, 'sunshine'))

if __name__ == "__main__":
    main()







