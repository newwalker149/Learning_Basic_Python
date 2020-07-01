#Write a program that reads the words in words.txt and
#stores them as keys in a dictionary.
#It doesn’t matter what the values are.
#Then you can use the in operator as a fast way
#to check whether a string is in the dictionary.


words = dict()
file = open('words.txt')
print(words)
for word in file:
    for word in word.split():
        words[word] = words.get(word)
checking = input('Enter a key: ')
print(checking in words)





    #word = word.split():
    #words[word] = words.get(word, 0) + 1
    #print(words)
