#!/usr/bin/python3
"""
Module to get the subscriber count of a subreddit.
"""

import requests


def get_subscribers(subreddit):
    """Fetches the number of subscribers for a given subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'reddit-subscriber-checker:v1.0 (by /u/firdaus_cartoon_jr)'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0

    data = response.json().get("data", {})
    return data.get("subscribers", 0)
