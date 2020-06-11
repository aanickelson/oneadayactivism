#!/usr/bin/env python3
# Code adapted from https://towardsdatascience.com/building-a-twitter-bot-with-python-89959ef2607f

import tweepy


def tweet_it_out(keys_file, message):
    my_keys = read_file(keys_file)
    api = authorization(my_keys)
    publish_tweet(api, message)


def read_file(filename):
    f = open(filename, 'r')
    data = []
    for line in f:
        if line[0] != '#':
            data.append(line.strip('\n'))
    return data


def authorization(keys_data):
    consumer_key = keys_data[0]
    consumer_secret = keys_data[1]
    access_token = keys_data[2]
    access_token_secret = keys_data[3]

    # Authorize to post
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def publish_tweet(api, message):
    api.update_status(message)


if __name__ == "__main__":
    my_keys = 'mykeys'
    tweet_to_publish = 'Hello World! (Obligatory test tweet from script)'
    tweet_it_out(my_keys, tweet_to_publish)
