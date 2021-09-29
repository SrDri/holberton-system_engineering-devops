#!/usr/bin/python3
""" Script number subs Reddit API """
from requests import get


def number_of_subscribers(subreddit):
    """ number of subscribers get the count from Reddit"""

    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {"User-Agent": "0x16. API advanced by Juan Carabali"}

    response = get(url, headers=headers).json()
    return response.get('data', {}).get('subscribers', 0)
