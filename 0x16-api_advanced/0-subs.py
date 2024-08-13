#!/usr/bin/python3
"""Module to get the number of subscribers for a subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Fetches and returns the number of subscribers for a given subreddit."""
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "RedditAPIClient/1.0"}

    response = requests.get(api_url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data", {})
    return data.get("subscribers", 0)
