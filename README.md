# TEXT ANALYTICS - SUPERBOWL ADVERTISEMENTS 2016 

## 1. INTRODUCTION

Advertising is the best way to communicate to the customers. It helps in informing the customers about the brands available in the market and the variety of products
which can be of use to them. Marketing a product is as important as launching the product itself. Unlike traditional (radio, television, or print) channels of advertising,
running an ad on YouTube allows you to connect with potential customers the exact moment they perform a keyword search related to your business.

The main advantage of having an ad put up on YouTube relative to audience is, reach and targeted reach. The fact that YouTube has over 1 billion unique users and 6
billion hours of video viewed every month strengthens the value that an advertisement can add by mere viewing. From the aspect of the target audience, you can channel
your efforts to a specific location, a particular time of the day, viewing device etc. The advertisements on YouTube are affordable, durable and shareable giving a whole new
meaning to mass marketing.

The Super Bowl is the most watched American TV spectacle, and companies annually put forth their biggest efforts to make stunning commercials aimed at creating
impressions and buzz. These ads are then casted on YouTube via various channels. It could be either a parent channel or multiple child channels.

## Goal: The goal of this project is to help marketers create improved ads that would help in getting better engagement on these ads. This could be done
by analyzing a viewer&#39;s response to these ads. The output of the project would assist the ad makers to better comprehend reasons behind why a viewer didn’t like an ad 
or if the ad was able to get their message across its audience. This would eventually help in creating better ads for the upcoming seasons.

## 2. DATA UNDERSTANDING &amp; DESCRIPTION:
There are 4 unique datasets provided for this project. Of them, three of the files are data pertaining to ‘views’ of videos and one for the ‘comments’. These datasets can be
 used to describe the attractiveness of TV advertisements on YouTube during Super Bowl Season in 2016. Below is the description of different fields in the data.
The dataset used by us is the ‘Search Super Bowl Ads from Official Channels and Individual Users’.

The two sub data sets under this has been used for our analysis purpose:
a. Comments Dataset
b. Views Dataset

## 3. MODELLING APPROACH:

To answer the business questions, we used text mining to derive information from the comments. Our approach was to understand audience sentiment from the comments on video ads. 
As such, we identified the number of positive and negative words for each comment. Using external data of positive and negative word dictionary, different words in the comments 
were categorized into these two categories. And the words in the stop list were discarded. The next step was to calculate the proportion of negative words in these comments with 
respect to overall words. An assumption was made that those comments having higher proportion of negative words when compared to positive words as negative comments. The main focus is on video or 
channel with a high proportion of negative comments, as well as a large amount of total comments, and then did the analysis. 

In order to figure out the reason why people did not like a particular video, we gather all the negative words as well as the words in all negative comments, grouping by each video.
The negative keywords themselves represents viewers’ mood, actions or opinions. Meanwhile, the words in the negative shows the corresponding subjects or objects. For example, 
“I hate wars” and “It’s a stupid story.” The words “hate” and “stupid” here is the negative keywords, which show viewers’ opinions. And the “wars” and “story” are the corresponding objects. 
At the beginning, we wanted to analyze the word right before and after the negative words showed in the example. However, it wasn’t easy and we then decided to calculate word frequencies, 
assuming that the words with high frequencies are the hottest topics in the negative comments. Thus, we mainly focused on the nouns and adjectives in word lists of negative comments. And then integration 
all the top negative keywords as opinions, and all the top words in the negative comments as the corresponding objectives. This gives us a comprehensive view about what every video
conveys to the audience in real. The words create a story in itself about the sentiment to each video which the ad makers can use to make any requisite changes. Then  words from all the comments for each video 
are checked to see whether the advertisements are so interesting that they shadowed the products or services rather than the content of the video. Since people tend to discuss about things they are
interested in, another assumption was made that the advertisements are effective when people mentioned the products a lot in the comments, which means that the name of the product or related words
have a high frequency in all the comments. This analysis gives an in depth understanding of what clicks or remains with the viewer after watching an advertisement. It helps in redefining the 
primary objective of conveying a message through the advertisement, that being the product rather than the channel.

## 4.  ANALYSIS AND EXAMPLES:

Below are a few ad examples showing ads with high percentage of negative comments and ad performance of 2 different channels showing if they were able to deliver the message to their audience.  

### a. Ads with high percentage of negative comments:
#### Doritos:
This ad received 18,886 comments, out of which 56% were negative comments.
First, let’s look at the result from our model:

Top negative keywords in all comments 
['funny', 'sh*t', 'f**k', 'f**king', 'upset', 'murder', 'disliked', 'poor', 'd*mn', 'wrong']

Top 10 words in negative comments 
['funny', 'people', 'choice', 'baby', 'abortion', 'sh*t', 'don', 'f**k', 'doritos', 'ad'

The first thing we noticed is that there are a lot of curse words, which is no surprise because this advertisement received a lot of negative comments. But if we checked the top keywords again, we will notice that there are some certain words, like “murder”, and “wrong”. Also, from the top words in negative comments, we can also see there appears “baby” and “abortion”. It’s understandable that people may use some hateful words to say that they dislike one advertisement, but there must be some reason that people were talking about certain words like “baby” and “abortion”. So we can assume that this advertisement has somehow been associated with “abortion”. Next thing we do is to go to this ad’s url and check this video online, we can see the content of this ad is: 
A pregnant woman is receiving a sonogram in her hospital bed. The screen shows the baby. The father is snacking on Doritos and he notices the child’s arms moving in the direction of the chip, as Dad takes it from the bag and puts it in his mouth. Finally, after the annoyed mom grabs a chip and tosses it across the room, the baby emerges from the womb to go after the chip.
It’s clear that the advertisement’s content has verified our model’s result accuracy: the most controversial part is “the baby emerges from the womb to go after the chip”. Although it’s a creative way to express the idea of how good taste the doritos are, but still, no food advertisement wants to be associated with the abortion debate.

#### Toyoto Prius:
Another high negative percentage example is Toyota Prius advertisement. Total number of comments for this ad is 16,591 with 29% negative comments. 

Top negative keywords in all comments: 
['steal', 'hate', 'funny', 'stupid', 'crime', 'sh*t', 'break', 'wrong', 'annoying', 'dead']

Top 10 words in negative comments: 
['prius', 'toyota', 'car', 'commercial', 'police', 'can', 'like', 'just', 'cars', 'bank']

After we looked at the top negative keywords in all comments and top words in negative comments, we can see that besides hateful words, there are some certain words like “steal” “police”, and “bank”. So we can assume that this advertisement might have some improper content that involve crime scenes. After double check, the advertisement’s content is:

A group of men robbed a bank and came out to find their getaway car being towed. They came across a 2016 Prius, hopped in, and thus began an extremely long police chase. 

Based on the analysis of these two examples, we can see that our text mining model have a great accuracy of extract negative comment and can help us to further analysis why advertisements received many negative comments. 
   
### b. Comparison of content penetration in audience:
Below ads show if the channel was able to convey the message of their ad to the audience. 

#### Jeep Channel: 
Top keywords in all comments 
['jeep', 'song', 'commercial', 'like', 'love', 'jeeps', 'just', 'great', 'best', 'who', 'made']

For the channel ‘Jeep’, we found that the top keywords are about the product, and we conclude that they were able to deliver the content to their audience. 

#### Pepsi Channel:  
Top keywords in all comments 
['clark', 'bowl', 'video', 'thanks', 'utter', 'still', 'opportunity', 'section', 'comments', 'amazing', 'waste', 'twitter', 'status',  'modest', 'super','working', 'experience', 'fun', 'dwight', 'awesome] 

However, for the second example, we see that the product or brand is not mentioned in the top keywords. This shows that the content of this ad was not conveyed to the audience. 

So based one our model, the Jeep channel does a better job than the channel Pepsi on delivering the message about their product to the audience. In the Jeep channel, the viewer would talk about the Jeep’s product after they watched their advertisement, which is not the same case with the Pepsi channel. This analysis gives a clear indication of how advertisements can penetrate to the audience in a better fashion.   

## 5.    FUTURE STEPS: 

We identified two future steps that could further improve our analysis and help gain additional value from this analysis as mentioned below:

Cleaning data: This is an important step to further improve our analysis. There exist many different words that don’t fall under the positive or negative categories, such as ‘still’, ‘just’ etc. These words can be added as stop words, which would help in better categorization of comments. 

Predict future views: Our project focus was mainly on the comments dataset to understand viewer response to the ads. We could use this analysis to predict future views of these videos. Frequency of negative words, percentage of negative comments could be used as variables to see the change in views in the upcoming months.      

## 6.    CONCLUSION:

Super Bowl is one of the most attractive events that provides a huge platform for marketers to create engaging ads for the audience. This project provides an approach to understand the success of these ads by analyzing audience behaviour towards the ads, which could be a useful tool for creating better and more appealing ads for the audience. Understanding the comments not only help companies contemplate if viewers reacted to their ads in a positive way, but also helps them to know if they were able to create an impression about their brand and product in a viewer’s mind. Improving this approach by cleaning data better and predicting future views can further assist these companies in creating impactful and captivating ads.

#### References:

［1］Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, Washington, USA, 
［2］Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing and Comparing Opinions on the Web." Proceedings of the 14th International World Wide Web conference (WWW-2005), May 10-14, 2005, Chiba, Japan.


