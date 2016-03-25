import pandas as pd
import re
from sklearn import svm
import numpy as np
import nltk
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords 
from sklearn.feature_extraction.text import CountVectorizer
########################################
import MySQLdb

#import mysql.connector
db1 = MySQLdb.connect("localhost","root","ashish","db" )
#db1 = mysql.connector.connect(user='a8090155_pos',password='positivenews',host='mysql7.000webhost.com',database='a8090155_pos')
cursor = db1.cursor()

#######################################
########################################################3
import feedparser
import pandas as pd
import re
d = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533965/index.rss')
d1 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533916/index.rss')
d2 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533917/index.rss')
d3 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/7098551.cms')
d4 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533919/index.rss')
d5 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533920/index.rss')
d6 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533921/index.rss')
d7 = feedparser.parse('http://dynamic.feedsportal.com/c/33039/f/533968/index.rss')
d8 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533922/index.rss')
d9 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533925/index.rss')
d10 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533923/index.rss')
d11 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533924/index.rss')
d12 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533933/index.rss')
d13 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533927/index.rss')
d14 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533928/index.rss')
d15 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533929/index.rss')
d16 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533975/index.rss')
d17 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533976/index.rss')
d18 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533977/index.rss')
d19 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533978/index.rss')
d20 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533979/index.rss')
d21 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533980/index.rss')
d22 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/3947060.cms')
d23 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/4118235.cms')
d24 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/7503091.cms')
d25 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/6547154.cms')
d26 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/4118215.cms')
d27 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/3942695.cms')
d28 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/3947067.cms')
d29 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533981/index.rss')
d30 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/3947051.cms')
d31 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/3942690.cms')
d32 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/3942693.cms')
d33 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/8021716.cms')
d34 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533982/index.rss')
d35 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/3012535.cms')
d36 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533984/index.rss')
d37 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533985/index.rss')
d38 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533986/index.rss')
d39 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533987/index.rss')
d40 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533988/index.rss')
d41 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/3942663.cms')
d42 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/4118245.cms')
d43 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/3942660.cms')
d44 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/3942666.cms')
d45 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/3947071.cms')
d46 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533989/index.rss')
d47 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533990/index.rss')
d48 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533991/index.rss')
d49 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533992/index.rss')
d50 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533993/index.rss')
d51 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533994/index.rss')
d52 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533995/index.rss')
d53 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533996/index.rss')
d54 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533997/index.rss')
d55 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533998/index.rss')
d56 = feedparser.parse('http://timesofindia.feedsportal.com/c/33039/f/533999/index.rss')
d57 = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/7098551.cms')

TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)
i=0
title = []
desc = []
link = []
c = []
date=[]
image=[]
m=0

for post in d.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("0")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d1.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("1")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d2.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("2")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d3.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("3")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d4.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("4")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d5.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("5")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d6.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("6")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d7.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("7")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d8.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("8")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d9.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("9")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d10.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("10")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values

print "10"

for post in d11.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("11")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d12.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("12")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d13.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("13")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d14.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("14")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d15.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("15")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values

for post in d16.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("16")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d17.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("17")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d18.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("18")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d19.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("19")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d20.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("20")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values

print "20"

for post in d21.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("21")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d22.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("22")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d23.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("23")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d24.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("24")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d25.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("25")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values

for post in d26.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("26")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d27.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("27")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d28.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("28")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d29.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("29")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d30.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("30")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values

print "30"

for post in d31.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("31")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d32.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("32")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d33.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("33")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d34.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("34")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d35.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("35")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d36.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("36")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d37.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("37")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d38.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("38")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d39.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("39")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d40.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("40")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values

print "40"

for post in d41.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("41")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d42.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("42")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d43.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("43")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d44.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("44")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d45.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("45")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d46.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("46")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d47.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("47")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d48.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("48")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d49.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("49")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d50.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("50")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values

print "50"

for post in d51.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("51")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values
for post in d52.entries:
	#print post.title + ": \n" + post.description +"\n" + post.link + "\n"+"  a"
	title.append(post.title)
	img=re.findall('http://timesofindia.indiatimes.com/photo/[A-Z0-9]*.cms', post.description)
    	b=remove_tags(post.description)
	image.append(img)
	desc.append(b)
	#print d.entries[0].updated	
	#print date
#	d= post.pubDate()
	#print d
	date.append(post.updated)
	link.append(post.link)
	c.append("52")
	d = {'Status':c, 'Link':link,'Title':title ,'Description':desc,'Image':image,'Date':date}
	#print title
	#i=i+1
	#df1 = pd.DataFrame({'headline':a , 'content':b, 'link':c},index=[i])
	#print df1.values

print "end"

df1 = pd.DataFrame(d)
df1.to_csv('test_headlines.csv' ,sep = '\t' , quoting = 3 , index = [0] , encoding = 'utf-8',escapechar='\t')
#.to_csv('news.csv',header = None ,index = None)

print "inserted"

#######################################################
def review_to_words( raw_review ):
    # Function to convert a raw review to a string of words
    # The input is a single string (a raw movie review), and 
    # the output is a single string (a preprocessed movie review)
    #
    # 1. Remove HTML
    #review_text = BeautifulSoup(raw_review).get_text() 
    #
    # 2. Remove non-letters        
    letters_only = re.sub("[^a-zA-Z]", " ", raw_review) 
    #
    # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split()                             
    #
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))                  
    # 
    # 5. Remove stop words
    meaningful_words = [w for w in words if not w in stops]   
    #
    # 6. Join the words back into one string separated by space, 
    # and return the result.
    return( " ".join( meaningful_words ))

train = pd.read_csv("news1_test400.csv", header=0, \
                    delimiter="\t", quoting=3,error_bad_lines=False)

# Get the number of reviews based on the dataframe column size
num_reviews = train["id"].size


# Initialize an empty list to hold the clean reviews
clean_train_reviews = []

# Loop over each review; create an index i that goes from 0 to the length
# of the movie review list 
for i in xrange( 0, num_reviews ):
    # Call our function for each one, and add the result to the list of
    # clean reviews
    clean_train_reviews.append( review_to_words( train["Title"][i] ) )

vectorizer = CountVectorizer(analyzer = "word",tokenizer = None,preprocessor = None,stop_words = None,max_features = 5000) 
train_data_features = vectorizer.fit_transform(clean_train_reviews)
train_data_features = train_data_features.toarray()
print train_data_features.shape

vocab = vectorizer.get_feature_names()
print vocab

# Sum up the counts of each vocabulary word
dist = np.sum(train_data_features, axis=0)

# For each, print the vocabulary word and the number of times it 
# appears in the training set
for tag, count in zip(vocab, dist):
    print count, tag

clf = MultinomialNB()
clf.fit(train_data_features, train["Polarity"])

#################################################

test = pd.read_csv("test_headlines.csv", header=0, delimiter="\t", quoting=3 )

# Verify that there are 25,000 rows and 2 columns
print test.shape

# Create an empty list and append the clean reviews one by one
num_reviews = len(test["Title"])
clean_test_reviews = [] 

print "Cleaning and parsing the test set news reviews...\n"
for i in xrange(0,num_reviews):
    
    clean_review = review_to_words( test["Title"][i] )
    clean_test_reviews.append( clean_review )

# Get a bag of words for the test set, and convert to a numpy array
test_data_features = vectorizer.transform(clean_test_reviews)
test_data_features = test_data_features.toarray()

# Use the random forest to make sentiment label predictions
result = clf.predict(test_data_features)

print "start inserting to db"

for l in range(0 , num_reviews):
	a=test['Title'][l]
	b=test['Description'][l]
	c=test['Date'][l]
	d=test['Image'][l]
	e=test['Link'][l]
	f=test['Status'][l]
	g=result[l]
	#sql = "INSERT INTO sample VALUES (%s,%s)",(a,b)
	try:
   # Execute the SQL command
		cursor.execute("INSERT INTO sample (Title,Description,Date,Image,Link,Category,Result) VALUES (%s,%s,%s,%s,%s,%s,%s)",(a,b,c,d,e,f,g))
   # Commit your changes in the database
		db1.commit()
	except:
   # Rollback in case there is any error
   		db1.rollback()
	#cursor.execute(sql)
#	print  train['headline'][l]
#	print result[k]
			
#for k in range(0,20):
#	print result[k]

# Copy the results to a pandas dataframe with an "id" column and
# a "sentiment" column

print "into db"

print result
output = pd.DataFrame( data={"id":test["Status"], "sentiment":result} )

# Use pandas to write the comma-separated output file
output.to_csv( "Bag_of_Words_model.csv", index=False, quoting=3 )
