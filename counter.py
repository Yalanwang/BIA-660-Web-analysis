'''
First homework of web analysis
count the most commom word in a text file
'''
def run(path):
    counts = dict()
    words = []
    textFile = open(path)
    words = textFile.read().strip().split()
    for word in words:
        counts[word] = counts.get(word,0)+1
    #print (counts)
    textFile.close()
    winner = None
    winnerFreq = -1
    for word in counts:
        if counts[word]>winnerFreq:
            winner = word
            winnerFreq = counts[word]
    return winner,winnerFreq
    
    
path = "F:/graduate study/semester2/660/week1/textfile"
print (run(path))