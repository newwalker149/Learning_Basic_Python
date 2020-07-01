#write a program to read through the mail box data and when you find line that
#starts with "from", you will split the line into word using the split function
# we are interested in who send the message, which is the second word on the form lines
#you will parse the form line and print out the second word for each from line
#then you will also count the number of from(not from:) lines and print out a count at the end


file = open('mbox-short.txt')
count = 0
for mail in file:
    mail = mail.rstrip()
    if mail.startswith('From'):
        a = mail.split()
        if a[0] == 'From:':
            count += 1
            print(a[1])
print('There were', count, 'lines in the file with From as the first word')
