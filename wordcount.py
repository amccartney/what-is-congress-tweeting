from collections import Counter
import re

words = re.findall(r'\w{5,}', open('example.txt').read().lower())

most_frequent_words = sorted(Counter(words).most_common(1), key=lambda (x,y): (y,x))
for (word, freq) in most_frequent_words:
  print word

hashtags = re.findall(r'#(\w+)', open('example.txt').read().lower())

most_frequent_hashtags = sorted(Counter(hashtags).most_common(1), key=lambda (x,y): (y,x))
for (hashtag, freq) in most_frequent_hashtags:
  print "#" + hashtag

handles = re.findall(r'@(\w+)', open('example.txt').read().lower())

most_frequent_handles = sorted(Counter(handles).most_common(1), key=lambda (x,y): (y,x))
for (handle, freq) in most_frequent_handles:
  print "@" + handle

