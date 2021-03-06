from string import maketrans
from collections import Counter
from operator import itemgetter
from difflib import SequenceMatcher
from itertools import combinations
import re
pattern = re.compile("<category>([^<]+)</category>")
import ipdb

REPLACE_CHARS = maketrans('-', ' ')
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87



def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    with open(RSS_FEED,'r') as fil:
        rss = fil.read()
    return [t.translate(REPLACE_CHARS) for t in pattern.findall(rss)]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return Counter(tags).most_common(TOP_NUMBER)

def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    sim = combinations(set(tags),2)
    return [(a,b) for (a,b) in sim if SequenceMatcher(None, a, b).ratio() > SIMILAR and a!=b]
    

if __name__ == "__main__":
    tags = get_tags()
    print tags
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = get_similarities(tags)
    print('* Similar tags:')
    for singular, plural in similar_tags:
        print('{:<20} {}'.format(singular, plural))
