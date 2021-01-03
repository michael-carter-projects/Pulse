# -*- coding: utf-8 -*-
# Python file that retrieves a list of youtube urls to embed in website
# given the search term input by the user

import os
import googleapiclient.discovery # import google api

def main(user_input):

    api_name = "youtube"                                 # use youtube api
    api_ver  = "v3"                                      # version 3
    API_KEY  = os.getenv("PULSE_YOUTUBE_API_KEY", False) # csci3308-pulse key
    if not API_KEY:
        raise ValueError(
            "Unable to get YouTube API key- is PULSE_YOUTUBE_API_KEY set?"
        )

    # create object to use search and list below and store as "youtube"
    youtube = googleapiclient.discovery.build(api_name, api_ver, developerKey=API_KEY)

    num_results = 25 # stores the number of results to include in the search

    request = youtube.search().list(
        q = user_input,           # stores string to be searched
        part = "id",              # retrieve the video ID to construct url string
        maxResults = num_results, # retrieve 10 video results
        order="viewCount"         # sort videos by number of views
    )
    response = request.execute() # execute API call and store in "response"

    url = 'https://www.youtube.com/embed/' # stores beginning of video url

    url_list = [] # list to store urls for top videos returned
    num_found = 0 # will count the number of videos youtube search found

    for item in response['items']: # use the list of items found on Youtube to
        if item['id']['kind'] == 'youtube#video':
            url_list.append(url + item['id']['videoId']) # append urls to url_list &
            num_found += 1                               # count number of videos

    youtube_dict = [] # create a youtube dictionary for return

    for i in range(0, num_found):  # use a loop to populate url dictionary
        video = {}                 # create dictionary listing
        video['url'] = url_list[i] # set 'url' for video to url
        youtube_dict.append(video) # append video to dictionary

    return tuple(youtube_dict) # return a tuple for use in views.py

if __name__ == "__main__":
    main()
