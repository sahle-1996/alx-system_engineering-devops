#!/usr/bin/python3
"""Module to recursively fetch hot post titles from a Reddit subreddit."""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively retrieves titles of all hot posts from a given subreddit."""
    if hot_list is None:
        hot_list = []

    if not isinstance(subreddit, str) or not subreddit:
        return None

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    params = {'after': after, 'limit': 100}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    posts = data.get('children', [])
    after = data.get('after', None)

    for post in posts:
        title = post.get('data', {}).get('title', '')
        hot_list.append(title)

    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
