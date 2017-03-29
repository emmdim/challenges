from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET


DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100



Tweet = namedtuple('Tweet', 'id_str created_at text')

class UserTweets(object):
    """TODOs:
    - create a tweepy api interface
    - get all tweets for passed in handle
    - optionally get up until 'max_id' tweet id
    - save tweets to csv file in data/ subdirectory
    - implement len() an getitem() magic (dunder) methods"""
    
    def __init__(self, handle, max_id=None):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self._api = tweepy.API(auth)
        self._handle = handle
        self.output_file = "{}.{}".format(os.path.join(DEST_DIR,self._handle),EXT)
        self.user = self._api.get_user(self._handle)
        self._max_id = max_id
        self._tweets = list(self._get_tweets())
        self._tweets = self._parse_tweets()
        #self._save_tweets()


    def _parse_tweets(self):
        parsed_tweets = []
        for tweet in self._tweets:
            tw = vars(tweet)
            parsed_tweets.append(Tweet(tw['id_str'].encode('utf-8'),tw['created_at'],tw['text'].replace('\n', '').encode('utf-8')))
        return parsed_tweets



    def _get_tweets(self): 
        return self._api.user_timeline(id=self._handle, count=100) if not self._max_id else self._api.user_timeline(id=self._handle, max_id=self._max_id)

    def _save_tweets(self):
        with open(self.output_file,'w') as f:
            w = csv.writer(f)
            w.writerow(Tweet._fields)
            w.writerows(self._tweets)

    def __len__(self):
        return len(self._tweets)

    def __getitem__(self, key):
        return self._tweets[key]

if __name__ == "__main__":

    for handle in ('pybites', 'techmoneykids', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
