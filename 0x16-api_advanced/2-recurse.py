#!/usr/bin/python3
"""Module to recursively fetch hot post titles from a subreddit."""

from requests import get


def fetch_all_hot_posts(subreddit, hot_posts=None, after_param=None):
    """Recursively queries Reddit API to retrieve all hot post titles."""
    if hot_posts is None:
        hot_posts = []

    if not isinstance(subreddit, str) or not subreddit:
        return None

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after_param, 'limit': 100}

    response = get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    after_param = data.get('after')
    posts = data.get('children', [])

    for post in posts:
        hot_posts.append(post.get('data', {}).get('title', 'No Title'))

    if after_param:
        return fetch_all_hot_posts(subreddit, hot_posts, after_param)

    return hot_posts
