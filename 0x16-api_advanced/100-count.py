#!/usr/bin/python3
"""Module with functions for Reddit API interaction."""

import requests


def print_sorted_histogram(histogram=None):
    """Sorts and prints the given histogram."""
    if histogram is None:
        histogram = []

    histogram = [item for item in histogram if item[1]]
    histogram_dict = {}
    for key, value in histogram:
        histogram_dict[key] = histogram_dict.get(key, 0) + value

    sorted_histogram = sorted(histogram_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    result_str = '\n'.join(f'{key}: {value}' for key, value in sorted_histogram)

    if result_str:
        print(result_str)


def count_word_occurrences(subreddit, words, histogram=None, count=0, after=None):
    """Counts occurrences of words in a subreddit and prints the histogram."""
    if histogram is None:
        histogram = [(word.lower(), 0) for word in words]

    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
    }
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=30&count={count}&after={after or ""}'
    
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        posts = data.get('children', [])
        titles = [post['data']['title'] for post in posts]

        histogram = [(word, count + sum(title.lower().split().count(word) for title in titles))
                     for word, count in histogram]

        if len(posts) == 30 and data.get('after'):
            count_word_occurrences(subreddit, words, histogram, count + len(posts), data['after'])
        else:
            print_sorted_histogram(histogram)
    else:
        return
