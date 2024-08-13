#!/usr/bin/python3
"""Module to fetch and display top 10 hot posts from a subreddit."""
import requests


def display_top_ten(subreddit):
    """Displays the titles of the top 10 hot posts on a given subreddit."""
    api_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    request_headers = {"User-Agent": "custom-agent:v1.0"}
    query_params = {"limit": 10}

    response = requests.get(api_url, headers=request_headers,
                            params=query_params, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    posts = response.json().get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title", "No Title"))
