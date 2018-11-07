import tweepy
from youtube_driver import get_channel_details
from time import sleep

consumer_key = 'BfNPOwA1gRGmqLB28zo3315hG'
consumer_secret = 'TQxZTQOXS1ctzMrOIrrj8UyIMXppp6b3P1HxRVUw4Nr1AqKZa3'
access_token = '91826016-X3KhSGJ6KdqxhG1Eg5SY6vSCXSwA8ohuNaxkCA85f'
access_token_secret = 'I5WYhH4ZwiHcugkdgfaWAHfcIKSrKc8yD7sm1DYKJftYZ'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

passed = False

while not passed:
    if int(get_channel_details('pewdiepie')['subscribers']) > 69696969:
        passed = True
        status = "@pewdiepie has just reached 69696969 subscribers on @YouYube. That's something to celebrate. Check out http://www.topsubs.xyz for real time comparison #tseries vs #pewdiepie"
        user = api.update_status(status)
    print("sleeping for 5 sec")
    sleep(5)


