import sys
import re

from usertweets import Tweet, UserTweets


#Strip non letters efficiently
#https://stackoverflow.com/questions/638893/what-is-the-most-efficient-way-in-python-to-convert-a-string-to-all-lowercase-st#639325
#(
import string
letter_set = frozenset(string.ascii_lowercase + string.ascii_uppercase)
tab = string.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                       string.ascii_lowercase * 2)
deletions = ''.join(ch for ch in map(chr,range(256)) if ch not in letter_set)
#string.translate(s, tab, deletions)
#)

#NLP framework
#(
from gensim import corpora, models, similarities
#)

#Stopwords
#(
from nltk.corpus import stopwords
#nltk has also a tweet tokenizer: http://www.nltk.org/api/nltk.tokenize.html
STOPWORDS = stopwords.words('english')
#)

IS_LINK_OBJ = re.compile(r'^(?:@|https?://)')

import ipdb


def tweet_parser(tweet):
	tweet = tweet.split()
	#Remove mentions and urls and strip weird characters
	tweet = [string.translate(w, tab, deletions) for w in tweet if not IS_LINK_OBJ.search(w)]
	#Remove words with less than 4 charachters and in STOPWORDS
	return [w for w in tweet if len(w)>3 and w not in STOPWORDS]


def similar_tweeters(user1, user2):
	tweets1 = [tweet_parser(t.text) for t in UserTweets(user1)]
	tweets2 = [tweet_parser(t.text) for t in UserTweets(user2)]
	ipdb.set_trace()
	dictionary = corpora.Dictionary([tweets1,tweets2])
	corpus = [dictionary.doc2bow(text) for text in [tweets1,tweets2]]

	


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
