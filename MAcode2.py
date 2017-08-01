import pandas as pd
from collections import Counter
import re

commentdf = pd.read_csv('cdf_0427.csv',index_col=0).T
stoplst = pd.read_csv('terrier-stop.txt')['words'].tolist()
print commentdf.head()

word = {}
negkeys = []
negwords = []
allwords = []

for id in commentdf.index:
    word[id] = {}
    neg = re.findall('[a-z]+', commentdf.loc[id, 'negkeyword'])
    negwords += re.findall('[a-z]+', commentdf.loc[id, 'allnegwords'])
    allwords += re.findall('[a-z]+', commentdf.loc[id, 'allwords'])
    negkeys += neg
    word[id]['negkeywordfreq'] = dict(Counter(neg))
    word[id]['negword10'] = re.findall('[a-z]+', commentdf.loc[id, 'Top10WordsinNeg'])
    word[id]['allword10'] = re.findall('[a-z]+', commentdf.loc[id, 'Top10WordsinAll'])
    word[id]['negkeyword10'] = sorted(dict(Counter(neg)), key=dict(Counter(neg)).get, reverse=True)[:10]
    word[id]['count'] = commentdf.loc[id, 'count']
    word[id]['negative'] = commentdf.loc[id, 'negative']
    word[id]['neg%'] = 100*int(word[id]['negative'])/int(word[id]['count'])



nk = {}
nk['count'] = dict(Counter(negkeys))
negkeywordfreq = pd.DataFrame(nk).sort(['count'], ascending=False)

nw = {}
nw['count'] = dict(Counter(negwords))
map(nw['count'].pop, list(set(nw['count'].keys()).intersection(stoplst)))
negwordfreq = pd.DataFrame(nw).sort(['count'], ascending=False)

aw = {}
aw['count'] = dict(Counter(allwords))
map(aw['count'].pop, list(set(aw['count'].keys()).intersection(stoplst)))
allwordfreq = pd.DataFrame(aw).sort(['count'], ascending=False)

print pd.DataFrame(word)
words = pd.DataFrame(word).T.sort(['neg%'], ascending=False)
words.to_csv('words_new.csv')
print 'negkeywordfreq,\n',negkeywordfreq
negkeywordfreq.to_csv('negkeywordfreq.csv')
print 'negwordfreq,\n',negwordfreq
negwordfreq.to_csv('negwordfreq.csv')
print 'allwordfreq,\n',allwordfreq
allwordfreq.to_csv('allwordfreq.csv')
