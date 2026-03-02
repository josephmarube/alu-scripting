#!/usr/bin/python3
"""
Module that queries Reddit API and prints the titles
of the first 10 hot posts of a subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "python:reddit.top_ten:v1.0 (by /u/anonymous)"
    }

    params = {
        "limit": 10
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        print (None)
        return
        
    data = response.json().get("data").get("children",[])

    if not data:
        print(None)
        return
        
    for post in data:
            print(post.get("data").get("title"))
    
