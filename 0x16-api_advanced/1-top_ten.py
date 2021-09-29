#!/usr/bin/python3
""" Reddit API first 10 hot posts subreddit """
from requests import get


def top_ten(subreddit):
    """ Reddit API first 10 hot """
    url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    headers = {"User-Agent": "0x16. API advanced by Juan Carabali"}

    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return print(None)

    posts = response.json().get("data").get("children")
    for post in posts:
        print(post.get("data").get("title"))
