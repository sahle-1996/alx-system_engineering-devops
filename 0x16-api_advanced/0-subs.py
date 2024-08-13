#!/usr/bin/python3
"""
Module to retrieve the number of subscribers for a subreddit.
"""

import requests


def get_subscriber_count(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"http://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0

    return response.json().get("data", {}).get("subscribers", 0)
