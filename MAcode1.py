import re
import pandas as pd
import numpy as np
from collections import Counter
import datetime

time1 = datetime.datetime.now()
commentdf = pd.read_csv('2016 Super Bowl Data/1.Search Super Bowl Ads from Official Channels And Individual Users/comments.csv')
commentdf = commentdf.loc[:,('Video ID', 'Video Title', 'Text')]
commentdf = commentdf.apply(lambda x: x.astype(str).str.lower())
commentdf['positive words'] = 0
commentdf['negative words'] = 0

positive = pd.read_csv('positive.txt')['words'].tolist()
negative = pd.read_csv('negative.txt')['words'].tolist()
stoplst = pd.read_csv('terrier-stop.txt')['words'].tolist()
comment = {} # pro or con
lst = {} # freq
vlst = {}


def wordcheck(i, id, cmt, pos, neg, allcmt):
    for word in cmt:
        if len(word) >= 2 and word not in stoplst:
            if word in positive:
                pos += 1
            if word in negative:
                neg += 1
                print 'neg,', word
                comment[id]['negkeyword'] += [word]
    commentdf.loc[i, 'positive words'] = pos
    commentdf.loc[i, 'negative words'] = neg
    if pos > neg:
        comment[id]['positive'] += 1
    elif pos < neg:
        comment[id]['negative'] += 1
    if neg != 0:
        comment[id]['allnegwords'] += allcmt
    #print 'text,', commentdf.loc[i, 'Text']
    comment[id]['allwords'] = vlst[id]
    comment[id]['negcomments'] += [commentdf.loc[i, 'Text']]
    return comment

def countword(cmt):
    dic = dict(Counter(cmt))
    map(dic.pop, list(set(dic.keys()).intersection(stoplst)))
    sortwordlst = sorted(dic, key=dic.get, reverse=True)
    return sortwordlst

def countword_neg(cmt, allwords):
    dic = dict(Counter(cmt))
    map(dic.pop, list(set(dic.keys()).intersection(stoplst)))
    map(dic.pop, list(set(dic.keys()).intersection(allwords)))
    sortwordlst = sorted(dic, key=dic.get, reverse=True)
    return sortwordlst


for i in range(len(commentdf.index)):
    print i
    id = commentdf.loc[i, 'Video ID']
    allcmt = re.findall('[A-Za-z]+', commentdf.loc[i, 'Text'])
    cmt = list(set(re.findall('[A-Za-z]+', commentdf.loc[i, 'Text'])))
    pos = 0
    neg = 0
    if id not in lst.keys():
        lst[id] = cmt
        vlst[id] = allcmt
        comment[id] = {}
        comment[id]['positive'] = 0
        comment[id]['negative'] = 0
        comment[id]['count'] = 1
        comment[id]['allnegwords'] = []
        comment[id]['negkeyword'] = []
        comment[id]['negcomments'] = []
        wordcheck(i, id, cmt, pos, neg, allcmt)
    else:
        lst[id] += cmt
        vlst[id] += allcmt
        lst[id] = list(set(lst[id]))
        comment[id]['count'] += 1
        wordcheck(i, id, cmt, pos, neg, allcmt)
    comment[id]['Top10WordsinAll'] = countword(comment[id]['allwords'])[:10]
    comment[id]['Top10WordsinNeg'] = countword(comment[id]['allnegwords'])[:10]

#print lst
cdf = pd.DataFrame(comment)
print cdf
cdf.to_csv('cdf_0427.csv')
time2 = datetime.datetime.now()
print time2 - time1
#print commentdf.head()



#lst = list(set(re.findall('[A-Za-z]+',t)))
#KeyWorksStr = ','.join(lst)




