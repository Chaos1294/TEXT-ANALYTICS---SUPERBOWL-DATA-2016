import re
import pandas as pd
import numpy as np
from collections import Counter
import datetime

videodf = pd.read_csv('2016 Super Bowl Data/1.Search Super Bowl Ads from Official Channels And Individual Users/views.csv')
videotdf = videodf.loc[:,('Video ID', 'Video Title', 'Channel Title', 'Url')]
videodf = videodf.loc[:,('Video ID', 'Channel Title')] # 'Video Title',
videodf = videodf.apply(lambda x: x.astype(str).str.lower())
videodf = videodf.drop_duplicates()
videodf = videodf.set_index('Video ID')
videodf.to_csv('video.csv')

videotdf = videotdf.drop_duplicates()
videotdf = videotdf.set_index('Video ID')
videotdf.to_csv('videotitle.csv')

commentdf = pd.read_csv('cdf_0427.csv', index_col = 0).T
commentdf = commentdf.drop(commentdf.index[[0, 1]])
print len(commentdf.index)
#print commentdf.head()
stoplst = pd.read_csv('terrier-stop.txt')['words'].tolist()
commentdf = commentdf.merge(videodf, left_index=True, right_index=True, how = 'left')
print len(commentdf.index)
#print commentdf.head()
commentdf['Vedio ID'] = commentdf.index
commentdf = commentdf.reset_index(drop=True)
print commentdf.head()
channel = {}

for id in commentdf.index:
    print 'id',id
    if pd.isnull(id): continue
    ct = commentdf.loc[id, 'Channel Title']
    if pd.isnull(ct): continue
    if ct not in channel.keys():
        channel[ct] = {}
        channel[ct]['count'] = commentdf.loc[id, 'count']
        channel[ct]['negative'] = commentdf.loc[id, 'negative']
        channel[ct]['negkeyword'] = re.findall('[a-z]+', commentdf.loc[id, 'negkeyword'])
        channel[ct]['negwords'] = re.findall('[a-z]+', commentdf.loc[id, 'allnegwords'])
        channel[ct]['allwords'] = re.findall('[a-z]+', commentdf.loc[id, 'allwords'])
    else:
        channel[ct]['count'] += commentdf.loc[id, 'count']
        channel[ct]['negative'] += commentdf.loc[id, 'negative']
        channel[ct]['negkeyword'] += re.findall('[a-z]+', commentdf.loc[id, 'negkeyword'])
        channel[ct]['negwords'] += re.findall('[a-z]+', commentdf.loc[id, 'allnegwords'])
        channel[ct]['allwords'] += re.findall('[a-z]+', commentdf.loc[id, 'allwords'])
    channel[ct]['neg%'] = 100 * int(channel[ct]['negative'])/int(channel[ct]['count'])

for ct in channel.keys():
    dic1 = dict(Counter(channel[ct]['negkeyword']))
    map(dic1.pop, list(set(dic1.keys()).intersection(stoplst)))
    dic2 = dict(Counter(channel[ct]['negwords']))
    map(dic2.pop, list(set(dic2.keys()).intersection(stoplst)))
    dic3 = dict(Counter(channel[ct]['allwords']))
    map(dic3.pop, list(set(dic3.keys()).intersection(stoplst)))
    channel[ct]['negkeywordfrq'] = dic1
    channel[ct]['negwordsfrq'] = dic2
    channel[ct]['allwordsfrq'] = dic3
    channel[ct]['negkeyword'] = sorted(dic1, key=dic1.get, reverse=True)
    channel[ct]['negwords'] = sorted(dic2, key=dic2.get, reverse=True)
    channel[ct]['allwords'] = sorted(dic3, key=dic3.get, reverse=True)



pd.DataFrame(channel).T.sort(['neg%'], ascending=False).to_csv('channel.csv')
print pd.DataFrame(channel)

