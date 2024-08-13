#!/usr/bin/python3
"""Module to fetch subreddit subscribers."""


def fetch_subscriber_count(subreddit):
    """Fetches the number of subscribers for a given subreddit."""
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    return response.json().get("data", {}).get("subscribers", 0)
