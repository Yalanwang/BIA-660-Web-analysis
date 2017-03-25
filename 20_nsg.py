
from sklearn.feature_extraction.text import CountVectorizer
import os
#from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC


def readFile(path):
    lables = []
    reviews=[]
    files = os.listdir(path)
    #print (files)
    
    for file in files:
        currentPath = path + "/" + file
        #print (currentPath)
        
        if currentPath == currentPath == "F:/graduate study/semester2/660\week9/homework/20_newsgroups/comp.os.ms-windows.misc" or currentPath == "F:/graduate study/semester2/660\week9/homework/20_newsgroups/comp.sys.ibm.pc.hardware" or currentPath == "F:/graduate study/semester2/660\week9/homework/20_newsgroups/comp.sys.mac.hardware" : 
            nextFiles = os.listdir(currentPath)
            for nextFile in nextFiles:
                finalPath = currentPath + "/" + nextFile
                f = open(finalPath,'rb')
                review = f.read().decode("ISO-8859-1").strip()                
                lable = "comp"
                reviews.append(review)
                lables.append(lable)
        if currentPath == "F:/graduate study/semester2/660\week9/homework/20_newsgroups/rec.motorcycles":
            nextFiles = os.listdir(currentPath)
            for nextFile in nextFiles:
                finalPath = currentPath + "/" + nextFile
                f = open(finalPath,'rb')
                review = f.read().decode("ISO-8859-1").strip()                 
                lable = "rec"
                reviews.append(review[15:])
                lables.append(lable)
        if currentPath == "F:/graduate study/semester2/660\week9/homework/20_newsgroups/rec.sport.hockey":
            nextFiles = os.listdir(currentPath)
            for nextFile in nextFiles:
                finalPath = currentPath + "/" + nextFile
                f = open(finalPath,'rb')
                review = f.read().decode("ISO-8859-1").strip()                 
                lable = "sports"
                reviews.append(review[15:])
                lables.append(lable)
        if currentPath == "F:/graduate study/semester2/660\week9/homework/20_newsgroups/talk.politics.guns" or currentPath == "F:/graduate study/semester2/660\week9/homework/20_newsgroups/talk.politics.mideast": 
            nextFiles = os.listdir(currentPath)
            for nextFile in nextFiles:
                finalPath = currentPath + "/" + nextFile
                f = open(finalPath,'rb')
                review = f.read().decode("ISO-8859-1").strip()                  
                lable = "politics"
                reviews.append(review[15:])
                lables.append(lable)
    return reviews,lables

def readFile1(path):
    lables = []
    reviews=[]
    files = os.listdir(path)
    #print (files)
    
    for file in files:
        currentPath = path + "/" + file
        #print (currentPath)
        
        if currentPath == "F:/graduate study/semester2/660\week9/homework/20_newsgroups/comp.windows.x" : 
            nextFiles = os.listdir(currentPath)
            for nextFile in nextFiles:
                finalPath = currentPath + "/" + nextFile
                f = open(finalPath,'rb')
                review = f.read().decode("ISO-8859-1").strip()                
                lable = "comp"
                reviews.append(review[15:])
                lables.append(lable)
        if currentPath == "F:/graduate study/semester2/660\week9/homework/20_newsgroups/rec.autos" :
            nextFiles = os.listdir(currentPath)
            for nextFile in nextFiles:
                finalPath = currentPath + "/" + nextFile
                f = open(finalPath,'rb')
                review = f.read().decode("ISO-8859-1").strip()                 
                lable = "rec"
                reviews.append(review[15:])
                lables.append(lable)
        if currentPath == "F:/graduate study/semester2/660\week9/homework/20_newsgroups/rec.sport.baseball":
            nextFiles = os.listdir(currentPath)
            for nextFile in nextFiles:
                finalPath = currentPath + "/" + nextFile
                f = open(finalPath,'rb')
                review = f.read().decode("ISO-8859-1").strip()                 
                lable = "sports"
                reviews.append(review[15:])
                lables.append(lable)
        if currentPath == "F:/graduate study/semester2/660\week9/homework/20_newsgroups/talk.politics.misc": 
            nextFiles = os.listdir(currentPath)
            for nextFile in nextFiles:
                finalPath = currentPath + "/" + nextFile
                f = open(finalPath,'rb')
                review = f.read().decode("ISO-8859-1").strip()                  
                lable = "politics"
                reviews.append(review[15:])
                lables.append(lable)
                #print (reviews)
    return reviews,lables

my_path = "F:/graduate study/semester2/660\week9/homework/20_newsgroups"
rev_train,labels_train=readFile(my_path)
rev_test,labels_test=readFile1(my_path)
counter = CountVectorizer()

counter = CountVectorizer()
counter.fit(rev_train)
counts_train = counter.fit_transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data
#print (counts_train.shape)
#print (counts_test.shape)
#train classifier
clf=SVC(C=1, cache_size=200, class_weight=None, coef0=0.0, 
    decision_function_shape=None, degree=3, gamma='auto', kernel='linear',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

#train all classifier on the same datasets
clf.fit(counts_train,labels_train)

#use hard voting to predict (majority voting)
pred=clf.predict(counts_test)

#print accuracy
print (accuracy_score(pred,labels_test))

