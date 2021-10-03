def countWordsFromFile():
    filename=input("Enter File Name-")
    numberOfWords=0
    file=open(filename,'r')
    for line in file:
        words=line.split()
        numberOfWords=numberOfWords+len(words)
    print("number of Words are-",numberOfWords)
countWordsFromFile()