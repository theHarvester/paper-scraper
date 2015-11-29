import praw
import json
from download.imgur import *

sub_reddit = "earthporn"

fp = open('config.json')
config = json.load(fp)
fp.close()

reddit = praw.Reddit(user_agent='Testing out praw')

for options in config['subreddits']:
    limit = options['limit'] if 'limit' in options else 10
    submissions = reddit.get_subreddit(options['subreddit']).get_hot(limit=limit)
    for submission in submissions:
        print("Fetching: " + submission.url)
        download(submission.url, options['output'])
