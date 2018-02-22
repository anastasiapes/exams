import tweepy
import json
import re
from collections import Counter
from tweepy import OAuthHandler

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

while True:
	try:
		screename = (raw_input("Enter username: "))
		text = " "
		for status in tweepy.Cursor(api.user_timeline, screen_name=screename).items(10):
			text= text+" "+ status._json['text']
		break
	except Exception:
		print ("\n")
text = ''.join([i for i in keim if not i.isdigit()])
text= ' '.join(re.sub("(#[A-Za-z0-9]+)|(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",text).split())
lista = text.split (' ')
counter = collections.Counter(lista)
tweets = str((counter.most_common(1)))
tweets = re.sub('[^a-zA-Z]+', '', tweets)

print tweets
