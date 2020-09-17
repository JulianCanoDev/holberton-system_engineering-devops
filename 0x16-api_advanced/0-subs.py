#!/usr/bin/python3
"""Reddit subs"""
import json
import requests


def number_of_subscribers(subreddit):
    URL = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    headers = {'User-agent': 'URL'}
    req = requests.get(URL, headers=headers, allow_redirects=False).json()
    try:
        return (req.get('data').get('subscribers'))
    except:
        return 0
