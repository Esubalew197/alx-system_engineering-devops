#!/usr/bin/python3
""" web scrapping with requests module """


import requests
url_base = "https://www.reddit.com/r/"


def top_ten(subreddit):
    """ gets the number of subscribers of a subreddit """
    url = url_base + subreddit + "/hot.json?raw_json=1&limit=10"
    headers = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        try:
            data = r.json()
            list_of_subreddits = data['data']['children']
            for sub_r in list_of_subreddits:
                print(sub_r['data']['title'])
            return
        except Exception:
            pass
    print(None)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("provide url")
        sys.exit(1)
    else:
        top_ten(sys.argv[1])
