f = open('we.txt', 'r')
for line in f:			# file is an iterable object
    print(line, end='')
f.close()
