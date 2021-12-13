import tweepy
from config import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

def tweet(content):
	auth.set_access_token(ACCESS_TOKEN, AUTH_SECRET)

	api = tweepy.API(auth)
	api.update_status(content)
