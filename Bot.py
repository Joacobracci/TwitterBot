import tweepy

consumer_key = "Enter Your Twitter Consumer key"
consumer_secret = "Enter Twitter Consumer secret"
access_key = "Enter your Twitter Access token"
access_secret = "Enter your Twitter secret acess token"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

for mention in mentions:
    print(str(mention.id) + "-" + mention.text)
