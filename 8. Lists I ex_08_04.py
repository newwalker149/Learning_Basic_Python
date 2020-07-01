 #write a program to open the file romeo.txt and read it line by line
#for each line, split the line into a list of words using the split function
#for each word, check to see if the words is already in a list
#if the word is not in the list, add it to the list
#FIND HOW TO CHECK THE LIST experiment 2
#1.using for doesn't succeed
#
#ITERATE EVERY WORDS FROM SPLITING
#use for to iterate every line in the file
#
#when the program completes, sort and print the resulting words in alphabetical order



file = open('romeo.txt', 'r')
words = [] #empty list to contains all the words was splitting by the lines
for line in file: #for iterating every line inside the file
    for word in line.split(): # for splitting the line into a list of words
        if word not in words: #for checking the list of the words in empty list
            words.append(word) #to add / move the list of the word into empty list

print(sorted(words))

#lines = file.read()
#lst = list()
#print(file)
#for line in lines:
#    words = lines.split()print(words, lst)
#for line in lines:
#    line = lines.split()
#    print(line)
#line = lines.split()
#newfile = sorted(line)
#print(newfile)
