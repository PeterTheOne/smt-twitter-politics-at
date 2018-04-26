import tweepy
import config


def connectApi():
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    return tweepy.API(auth)


def getAccounts():
    return open('accounts.txt').read().splitlines()


def fetchTimeline(user):
    return api.user_timeline(user, count=100)


def saveTimeline(tweets, user):
    with open('data/timeline_{}.txt'.format(user), 'a') as tf:
        for tweet in tweets:
            tf.write(tweet.text + "\n")


api = connectApi()
users = getAccounts()
for user in users:
    tweets = fetchTimeline(user)
    saveTimeline(tweets, user)

