# -*- coding: utf-8 -*-
# Python file that retrieves a list of youtube urls to embed in website
# given the search term input by the user

import os
import logging
import praw # import Python Wrapper for Reddit API

logger = logging.getLogger('django').getChild(__name__)

def main(user_input):

    # Personal use API
    my_clientId = os.environ.get('PULSE_REDDIT_CLIENTID', False)   
    # Secret API key
    my_secret   = os.environ.get('PULSE_REDDIT_SECRET', False)   
    my_agent    = os.environ.get('PULSE_REDDIT_USER_AGENT', False) 

    if False in (my_clientId, my_secret, my_agent):
        error_msg = "Unable to load Reddit API credentials- are" \
            "environment variables set up properly?"
        logger.error(error_msg)
        raise ValueError(error_msg)

    # create object to use search/list below and store as "reddit"
    reddit = praw.Reddit(client_id     = my_clientId,
                         client_secret = my_secret,
                         user_agent    = my_agent)

    num_results = 50 # number of results to limit search to

    results = reddit.subreddit('all').search( # perform a reddit search
        query = user_input,                   # using main fn search term
        limit = num_results,                  # and num_results
        sort  = 'hot'
    )

    url = "https://www.reddit.com" # stores beginning of post url

    url_list = [] # list to store urls for most relevant posts returned
    num_found = 0 # will count the number of videos reddit search found

    for post in results: #response['items']: # use the list of items found on Reddit
        url_list.append(url + post.permalink) # append urls to url_list &
        num_found += 1                               # count number of posts

    reddit_dict = [] # create a dictionary for return

    for i in range(0, num_found): # use a loop to populate url dictionary
        post = {}                 # create dictionary listing
        post['url'] = url_list[i] # set 'url' for video to url
        reddit_dict.append(post)  # append video to dictionary

    return tuple(reddit_dict) # return a tuple for use in views.py

if __name__ == "__main__":
    main()
