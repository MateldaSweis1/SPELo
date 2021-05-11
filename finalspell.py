#!/usr/bin/env python3

import trie

# initialize trie
root = trie.TrieNode('*')

def main(string):

# loop through lines(words) in a file and store in trie
    with open("studentMachineDict.txt","r") as afile:
            for line in afile:
                    word=line.rstrip()
                    # add word to trie
                    trie.insert(root, word)
                    
    commonWords = {}
    with open("commonWords2.txt", "r") as bfile:
        for index, word in enumerate(bfile): 
            commonWords[word.strip()] = index


# TODO recieve user input

# save words as a list without punctuation
    wackypunc = '[]{}()`<>\@#^_~'
    goodpunc = '\'!-;:"|,\.?$%&*+=/'
    words = []

    with open(string,"r") as afile:
        for text in afile:
            for let in text:
                if let in wackypunc:
                    text = text.replace(let,"")
            text = text.split()
            for word in text:
                for letter in word:
                    if letter in goodpunc:
                        word = word.translate({ord(letter): None})
                    if word == "":
                        continue
                
                    addPunc = []
                    if letter in goodpunc:
                        addPunc.append(letter)
                words.append(word)
                for punc in addPunc:
                    words.append(punc)

            
# TODO spell check algorithms
    final_list = []
    for i,word in enumerate(words):
        brutelist = []
        if not trie.is_word(root, word.lower()):
            brutelist = trie.brute_force1(root, word)
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
                    bestOption=""
                    lowestRank = 10000 
                    for brute in brutelist:
                        if brute in commonWords:
                            final_list.append(brute)  
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
                        suffix = []
                        temp = ""
                        trie.reverse_prefix(node,suffix, prefix,temp, word)

                        maxSuffix = ""
                        for suff in suffix:
                            if len(suff) > len(maxSuffix):
                                maxSuffix = suff

                        for sugg in suggestions:
                            if maxSuffix in sugg: 
                                words[i] = sugg

               
    #for word in words:
    #    print(f'{word} ', end='')     
    
    return words

if __name__ == "__main__":
    main("test1.txt")

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
