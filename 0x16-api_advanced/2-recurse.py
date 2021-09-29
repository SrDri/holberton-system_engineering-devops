#!/usr/bin/python3
""" Reddit API subreddit """
from requests import get


def recurse(subreddit, hot_list=[], after=""):
    """ script Reddit API the titles """
    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {"User-Agent": "0x16. API advanced by Juan Carabali"}

    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None

    posts = response.json().get("data").get("children")
    for post in posts:
        hot_list.append(post.get("data").get("title"))

    after = response.json().get("data").get("after")
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
