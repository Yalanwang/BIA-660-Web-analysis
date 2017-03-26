import re
import requests

def run(url,my_word):
    freq = {}
    success = False
    for i in range(5):
        try:
            response = requests.get(url,headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })  
            success = True
            break
        except:
            print ('failed attempt',i)
    if not success: return None
    text = response.text
    sentences = text.split('.')
    for sentence in sentences:
        sentence=sentence.lower().strip()
        sentence = re.sub('[^a-z]',' ',sentence)# replace all non-letter characters  with a space
        words = sentence.split(' ')
        for word in words:
            if word == ' ': continue
            elif word == my_word:
                freq[my_word] = freq.get(my_word,0)+1
    return freq
if __name__=='__main__':
    print(run('http://tedlappas.com/wp-content/uploads/2016/09/textfile.txt',"the"))