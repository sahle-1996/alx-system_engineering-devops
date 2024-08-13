#!/usr/bin/python3
"""
0-main
"""
import sys

if __name__ == '__main__':
    fetch_subscriber_count = __import__('0-subs').fetch_subscriber_count
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
