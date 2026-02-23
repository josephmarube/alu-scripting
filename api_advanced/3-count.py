#!/usr/bin/python3
"""
Recursively queries Reddit API and prints a sorted count
of given keywords in hot post titles.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Count keyword occurrences recursively."""
    if counts is None:
        counts = {}

    if after is None:
        word_list = [word.lower() for word in word_list]
        for word in word_list:
            counts[word] = counts.get(word, 0)

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
        return

    data = response.json().get("data")
    if not data:
        return

    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower()
        words = title.split()

        for word in counts:
            counts[word] += words.count(word)

    after = data.get("after")

    if after:
        return count_words(subreddit, word_list, after, counts)

    sorted_words = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    for word, count in sorted_words:
        if count > 0:
            print("{}: {}".format(word, count))
