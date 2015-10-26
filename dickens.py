###DICKENS BOT

from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import os

dickens = os.listdir('dickens')[1:]
quote_blocks = []

for snobbery in dickens:
    talks = []
    text = open('dickens/'+snobbery).read()
    text = text.split('\n')

    for i, each in enumerate(text):
        if each not in ["", [], None]:
            if each[0] in ['\'', '\"', '\xe2']:
                try:
                    while text[i+1] != '':
                        each += ' '+text[i+1]
                        i+=1
                    talks.append(''.join(each))
                except IndexError:
                    talks.append(''.join(each))

    text = talks
    text1 = map(lambda x: re.findall('"([^"]*)"', x), text)
    text2 = map(lambda x: re.findall(r'\'(.+?)\'', x), text)

    text = map(lambda x: ''.join(x), text)

    if text1[:10][0] > text2[:10][0]:
        text = text1
    else:
        text = text2
    quote_blocks.extend(text)

quote_blocks = [x for x in quote_blocks if x]
quote_blocks = map(lambda x: ' '.join(x), quote_blocks)

with open('temp.txt', 'w') as f:
    f.write(str(quote_blocks))

    # quotes2 = map(lambda x: re.findall(r'\'(.+?)\'', x), text)
    # quotes.extend(quotes2)
    # quotes = map(lambda x: ' '.join(x), quotes)
    # quotes = [x if x else 1 for x in quotes]

    # counter = 0
    # ans = []
    # for each in quotes:
    #     if type(each) == int:
    #         counter+=1
    #     if type(each) == str:
    #         ans.append(counter)
    #         ans.append(each)
    #         counter=0

    #print ans[:10]

#     temp = [ans[0]]
#     quote_blocks = []

#     for each in ans[1:]:
#         if len(temp) < 3:
#             temp.append(each)
#         else:
#             quote_blocks.append(temp)
#             temp = [temp[2]]
#             temp.append(each)

#     quotespace.extend(quote_blocks)

# import re

# s = '\'test test test, According to some, dreams express "profound aspects of personality" (Foulkes 184), though others disagree.\''
# lst = re.search('\'(?<=\().*?(?=\))\'',s)

# matches=re.findall(r'\'(.+?)\'',s)
# print matches


