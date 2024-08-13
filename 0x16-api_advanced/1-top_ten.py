#!/usr/bin/python3
"""Module for retrieving top 10 hot posts from a subreddit."""


def fetch_top_ten(subreddit):
    """Fetches and prints the top 10 hot posts of a subreddit."""
    import requests

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "custom-agent:v1.0 (by /u/your_username)"}
    
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title", "No Title"))
