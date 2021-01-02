import tweepy

consumer_key = "GHfCvUyPAzfQYuo1D2QxYYR1c"
consumer_secret = "mwbccgrDnEx3xioehwm5FiCFmzvo4NTxpFD5MujC3pILOtzfsg"
access_key = "1343370233621467137-aVbVkTwSXK2MztBB78J8B1AhhaYouc"
access_secret = "W66x66SQo1Tb8t3ym9q9Ftt8Wap7pQyikCTTJ0mrDVspj"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

for mention in mentions:
    print(str(mention.id) + "-" + mention.text)