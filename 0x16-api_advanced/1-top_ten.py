#!/usr/bin/python3
"""Module to print the titles of the top 10 hot posts from a subreddit."""

import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "CustomAgent/1.0"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "")
        print(title)
