#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns a list
of titles of all hot posts.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return list of all hot post titles using recursion."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "linux:api.advanced.project:v1.0 (by /u/anonymous)"
    }

    params = {
        "limit": 100,
        "after": after
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    if not data:
        return None

    posts = data.get("children", [])

    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")

    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
