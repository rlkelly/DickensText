from bs4 import BeautifulSoup
from urllib2 import urlopen

text = []
for each in range(1,4):
    url = 'http://literatureproject.com/great-expectations/great_%s.htm' %(str(each))
    words = BeautifulSoup(urlopen(url).read()) 
    text.append(' '.join(words.get_text().splitlines()[21:-25]))

print text

# with open('great_expectations2.txt', 'w') as f:
#     f.write(text.encode('utf-8'))