import tweepy, time, sys, os, ConfigParser, re
from collections import Counter

sys.path.append('keys-dir')

from key_file import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

filename = open('congress_screen_names_SHORT.txt','r')
f = filename.readlines()
filename.close()





#writes latest two tweets to a txt file
tmp_write = open('tmp.txt','w')
count = 1;

for a in f:
	a = a.rstrip()
	timeline = api.user_timeline(id=a, count=count)
	for status in timeline:
		x = status.text.encode('utf-8')
		tmp_write.write(x)
		sleep(2)

tmp_write.close()




#reads the text file of tweets and finds the most common words, hashtags and handles
words = re.findall(r'\w{5,}', open('tmp.txt').read().lower())

most_frequent_words = sorted(Counter(words).most_common(1), key=lambda (x,y): (y,x))
for (word, freq) in most_frequent_words:
  print word
  #api.update_status("Congress' most used word today was" + word)

#most common hashtags
hashtags = re.findall(r'#(\w+)', open('tmp.txt').read().lower())

most_frequent_hashtags = sorted(Counter(hashtags).most_common(1), key=lambda (x,y): (y,x))
for (hashtag, freq) in most_frequent_hashtags:
  print "#" + hashtag
   #api.update_status("Congress' most used hashtag today was" + hashtag)

#most common handles
handles = re.findall(r'@(\w+)', open('tmp.txt').read().lower())

most_frequent_handles = sorted(Counter(handles).most_common(1), key=lambda (x,y): (y,x))
for (handle, freq) in most_frequent_handles:
  print "@" + handle
   #api.update_status("Congress' most mentioned user today was" + handle)

os.remove('tmp.txt')