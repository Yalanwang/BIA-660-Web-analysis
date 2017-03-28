'''
the number of reply
the number of favorite
the date
'''

from selenium import webdriver
import time


url='https://twitter.com/SHAQ'

#open the browser and visit the url
#-----------------------------------------
#Windows
#driver = webdriver.Chrome('chromedriver.exe')
#Mac
driver = webdriver.Chrome('./chromedriver')
#--------------------------------------------
driver.get(url)

#scroll down twice to load more tweets
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

#find all elements with a class that ends in 'tweet-text'
tweets=driver.find_elements_by_css_selector("[data-item-type=tweet]")

"""
for tweet in tweets:
    print (tweet.find_element_by_css_selector("[class$=tweet-text"))
"""

#write the tweets to a file
fw=open('tweets.txt','w',encoding='utf-8')
for tweet in tweets:
    txt,retweets,number_favorite,number_reply,date='NA','NA','NA','NA','NA'
    
    try: txt=tweet.find_element_by_css_selector("[class$=tweet-text]").text
    except: print ('no text')     

    try:
        retweetElement=tweet.find_element_by_css_selector("[class$=js-actionRetweet]")
        retweets=retweetElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
    except:
        print ('no retweets')
    try:
        retweetElement=tweet.find_element_by_css_selector("[class$=js-actionFavorite]")
        number_favorite=retweetElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                                             
    except:
        print ('no likes')
        
    try:
        retweetElement=tweet.find_element_by_css_selector("[class$=js-actionReply]")
        number_reply=retweetElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
    except:
        print ('no reply')
        
    try:
        retweetElement=tweet.find_element_by_css_selector("[class$=js-tooltip]")
        date=retweetElement.find_element_by_css_selector('[class^=_timestamp]').text                                      
    except:
        print ('no reply')
        
    fw.write(txt.replace('\n',' ')+'\t'+str(retweets)+'\t'+str(number_favorite)+'\t'+str(number_reply)+'\t'+str(date)+'\n')


fw.close()


driver.quit()#close the browser