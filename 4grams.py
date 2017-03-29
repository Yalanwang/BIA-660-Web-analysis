
import nltk
from nltk.util import ngrams
import re
from nltk.tokenize import sent_tokenize
from nltk import load
from operator import itemgetter

def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex

def getPOSterms(terms,POStags,tagger):
	
    tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence
    #print (tagged_terms)
    POSterms={}
    for tag in POStags:POSterms[tag]=set()

    #for each tagged term
    for pair in tagged_terms:
        for tag in POStags: # for each POS tag 
            if pair[1].startswith(tag): POSterms[tag].add(pair[0])

    return POSterms
    #print (POSterms)


def processSentence(sentence,posLex,negLex,tagger):
    
    result=[]
    
    POStags=['NN'] # POS tags of interest 	
    #print(POStags)
   # POSterms=getPOSterms(sentence,POStags,tagger)

    fourgrams = ngrams(sentence,4) #compute 4-grams
    #print (fourgrams)
    #for each 4gram
    for tg in fourgrams:  
        if tg[0] == "not" and tg[2] in posLex and tg[3] in POStags: # if the 4gram is a an adverb followed by an adjective
             result.append(tg)
        elif tg[0] == "not" and tg[2] in negLex and tg[3] in POStags:
            result.append(tg)
   
    return result

def getTop3(D):
    Top3 = []
    sortedD = sorted(D.items(),key=itemgetter(1), reverse=True)
    for value in sortedD[0:3]:
        Top3.append(value[0])

    return Top3
    
def run(fpath):

    #make a new tagger
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)
    posLex=loadLexicon('positive-words.txt')
    negLex=loadLexicon('negative-words.txt')

    #read the input
    f=open(fpath)
    text=f.read().strip()
    f.close()

    #split sentences
    sentences=sent_tokenize(text)
    print ('NUMBER OF SENTENCES: ',len(sentences))

    Target_four_word=[]
    freq = {}

    # for each sentence
    for sentence in sentences:

        sentence=re.sub('[^a-zA-Z\d]',' ',sentence)#replace chars that are not letters or numbers with a spac
        sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces

        #tokenize the sentence
        terms = nltk.word_tokenize(sentence.lower())   
        #print (terms)

        #print (POSterms)

        #get the results for this sentence 
        Target_four_word+=processSentence(terms,posLex,negLex,tagger)
		
    #return Target_four_word
    freqNouns=getTop3(freq)  #atts=None#getAtts() #['bike','size']
    Fourgrams=set() # final result 

    for fgrams in Target_four_word: # for each sentence 
        for fg in fgrams: # for each matched 4gram in this sentence 
            if fg[3] in freqNouns: Fourgrams.add(' '.join(fg))
                            
    return Fourgrams
    


if __name__=='__main__':
	print (run('input.txt'))

