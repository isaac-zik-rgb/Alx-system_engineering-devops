#!/usr/bin/python3
"""a function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit."""
from security import safe_requests


def top_ten(subreddit):
    """a function that queries the Reddit API and prints the titles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    header = {'User-Agent': 'PythonScript/3.0'}
    response = safe_requests.get(url, header)
    data = response.json()
    if response.status_code == 200:
        posts = data.get('data', {}).get('children', [])
        top_ten_title = []
        for post in posts[:10]:
            title = post.get('data', {}).get('title')
            if title:
                top_ten_title.append(title)
        for i, title in enumerate(top_ten_title, 1):
            print(title)
    else:
        print('None')
