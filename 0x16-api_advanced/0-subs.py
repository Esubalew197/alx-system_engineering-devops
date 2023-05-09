#!/usr/bin/python3
""" web scrapping with requests module """


import requests
url_base = "https://www.reddit.com/r/"


def number_of_subscribers(subreddit):
    """ gets the number of subscribers of a subreddit """
    url = url_base + subreddit + "/about.json?raw_json=1"
    headers = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        try:
            return r.json().get("data")["subscribers"]
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("provide url")
        sys.exit(1)
    else:
        print(number_of_subscribers(sys.argv[1]))
