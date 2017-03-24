
"""
The second homework of web analysis
count the number of positive words in a text file
"""
def loadLexicon(fname):
    newLex = set ()
    Lex_con = open(fname) 
    for line in Lex_con:
        newLex.add(line.strip())
    Lex_con.close()
    return newLex

def run(path):
    
    result = dict()
    wordsList = []
    
    posLex = loadLexicon("F:/graduate study/semester2/660/BIA-660-Web-analysis/positive-words.txt")
    words = []
    my_file = open(path)
    for line in my_file:
        line.lower().strip()
        words = set(line.split(' '))
        wordsList.extend(words)
    my_file.close()
    
    for word in wordsList:
        #print(type(word))
        #print(type(result))
        if word in posLex:
            if word in result:
                result[word] += 1
            else: result[word] = 1
    return result

if __name__ == "__main__": 
    results=run('F:/graduate study/semester2/660/week2/textfile')
    print(results)

                
    
