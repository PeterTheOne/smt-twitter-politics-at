import tweepy
import config
# todo: fix requirements

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)


users = ['@HCStracheFP', '@sebastiankurz']
for user in users:
    public_tweets = api.user_timeline(user, count=100)
    with open('data/timeline_{}.txt'.format(user), 'a') as tf:
        for tweet in public_tweets:
            print(tweet.text)
            tf.write(tweet.text + "\n")

