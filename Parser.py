from bs4 import BeautifulSoup
import re
import requests
import time

def getCritic(review):
    critic = 'NA'
    criticChunk=review.find('a',{'href':re.compile('/critic/')})
    if criticChunk: critic=criticChunk.text#.encode('ascii','ignore')
    return critic
    
def getRating(review):
    
    Rating='NA' # initialize Rating
    if review.find('div',{'class':re.compile('review_icon icon small fresh')}):
        Rating = 'fresh'
    if review.find('div',{'class':re.compile('review_icon icon small rotten')}):
        Rating = 'rotten'
    return Rating

def getSource(review): 
    
    Source='NA' # initialize Source
    SourceChunk=review.find('div',{'class':re.compile('small subtle')})
    if SourceChunk: 
        Source=SourceChunk.text#.encode('ascii','ignore')
    return Source
    
def getDate(review): 
    
    Date='NA' # initialize Date
    DateChunk=review.find('div',{'class':re.compile('review_date subtle')})
    if DateChunk: 
        Date=DateChunk.text#.encode('ascii','ignore')
    return Date
    
def getTextLen(review): 
    
    TextLen = 'NA' # initialize TexLen
    TextLenChunk=review.find('a',{'href':re.compile('/critic/')})
    if TextLenChunk: 
        words=TextLenChunk.text#.encode('ascii','ignore')
        words.split()
        TextLen = str(len(words))
    return TextLen
    
        
def run(url):
    pageNum = 2
    fw = open ('reviews.txt','w')
    for p in range(1,pageNum+1):
        print ('page',p)
        html = None
        
        if p == 1:pageLink = url# url for page 1
        else: pageLink = url + '?page=' + str(p) + '&sort=' # the page
        
        for i in range(5):#try five times
            try:
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content # get the html
                break # we got the file, break the loop
            except:
                print('failed attempt',i)
                time.sleep(2)
        soup =  soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html    
        reviews = soup.findAll('div',{'class':re.compile('review_table_row')})#get all the reviews
       
        for review in reviews:
            Critic = getCritic(review)
            Rating = getRating(review)
            Source = getSource(review)
            Date = getDate(review)
            TextLen = getTextLen(review)
            fw.write(Critic+'\t'+Rating+'\t'+Source+'\t'+Date+'\t'+TextLen+'\n')
    fw.close()

if __name__=='__main__':
    url='https://www.rottentomatoes.com/m/space_jam/reviews/'
    run(url)