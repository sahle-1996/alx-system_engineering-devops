#!/usr/bin/python3
"""Module for counting keyword occurrences in Reddit hot posts."""

import requests
from collections import defaultdict
import re


def print_sorted_histogram(histogram):
    """Prints the histogram sorted by count and alphabetically."""
    if not histogram:
        return

    sorted_histogram = sorted(histogram.items(), key=lambda item: (-item[1], item[0]))
    for word, count in sorted_histogram:
        print(f"{word}: {count}")


def count_words(subreddit, word_list, after=None, histogram=None):
    """Recursively counts keyword occurrences in hot posts of a subreddit."""
    if histogram is None:
        histogram = defaultdict(int)

    if not isinstance(subreddit, str) or not subreddit:
        return

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after, 'limit': 100}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    posts = data.get('children', [])
    after = data.get('after', None)

    titles = [post['data']['title'].lower() for post in posts]
    for word in word_list:
        pattern = re.compile(r'\b{}\b'.format(re.escape(word.lower())), re.IGNORECASE)
        histogram[word.lower()] += sum(title.count(word.lower()) for title in titles)

    if after:
        count_words(subreddit, word_list, after, histogram)
    else:
        print_sorted_histogram(histogram) 
