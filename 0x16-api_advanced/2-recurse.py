#!/usr/bin/python3
"""Module to recursively fetch all hot posts from a subreddit."""
import requests


def fetch_hot_posts(subreddit, hot_posts=None, after_param="", post_count=0):
    """Recursively collects a list of titles of all hot posts from a subreddit."""
    if hot_posts is None:
        hot_posts = []

    api_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    request_headers = {"User-Agent": "Custom-Agent"}
    query_params = {
        "after": after_param,
        "count": post_count,
        "limit": 100
    }

    response = requests.get(api_url, headers=request_headers,
                            params=query_params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    after_param = data.get("after", "")
    post_count += data.get("dist", 0)
    
    for post in data.get("children", []):
        hot_posts.append(post.get("data", {}).get("title", "No Title"))

    if after_param:
        return fetch_hot_posts(subreddit, hot_posts, after_param, post_count)

    return hot_posts
