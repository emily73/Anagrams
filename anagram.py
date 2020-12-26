def anagrams(word):
    #produces all anagrams of a word
    if len(word) < 2:
        yield word
    else:
        for i, letter in enumerate(word):
            if not letter in word[:i]: #avoid duplicates
                for j in anagrams(word[:i]+word[i+1:]):
                    yield j+letter 

if __name__ == "__main__":
    wordlist = []
    x = input("Please enter a word: ")
    print("All possible anagrams of ", x.upper(), " are below:")
    for i in anagrams(x):
        #adds each arrangement to a list
        wordlist.append(i)
    #sorts list in aphabetical order
    wordlist.reverse()
    choice = input("Would you like to: \n 1. View the output \n 2. Save it to a file? ")
    if choice == "1":
        print(wordlist)
    elif choice == "2":
        #print to file
        filename = "%s.txt" % x
        with open(filename, 'w') as wordfile:
            for item in wordlist:
                #prints each word on new line
                 wordfile.write("%s\n" % item)
    else:
        print("invalid choice chosen")

