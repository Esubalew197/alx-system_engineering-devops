#!/usr/bin/python3
""" Contains recurse function to get hot topics """


import requests
url_base = "https://www.reddit.com/r/"


def recursor(subreddit, lst, url):
    """ implementation of recursion to get multi pages """
    headers = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(url, headers=headers)
    #  print("entered")
    if r.status_code == 200:
        try:
            data = r.json()
            list_of_subreddits = data['data']['children']
            #  for sub_r in list_of_subreddits:
            #    lst.append(sub_r['data']['title'])
            titles = [x.get('data').get('title') for x in list_of_subreddits]
            lst.extend(titles)
            after = data['data']['after']
            if after:
                url = url_base + subreddit + "/hot.json?raw_json=1&after=" + \
                    after
                return recursor(subreddit, lst, url)
            else:
                return lst
        except Exception:
            pass


def recurse(subreddit, hot_list=[]):
    """ gets the number of subscribers of a subreddit """
    url = url_base + subreddit + "/hot.json?raw_json=1"
    headers = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        try:
            data = r.json()
            list_of_subreddits = data['data']['children']
            #  for sub_r in list_of_subreddits:
            #    hot_list.append(sub_r['data']['title'])
            titles = [x.get('data').get('title') for x in list_of_subreddits]
            hot_list.extend(titles)
            after = data['data']['after']
            if after:
                url = url_base + subreddit + "/hot.json?raw_json=1&after=" + \
                    after
                return recursor(subreddit, hot_list, url)
            else:
                return hot_list
        except Exception:
            pass
    else:
        return None


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("provide url")
        sys.exit(1)
    else:
        res = recurse(sys.argv[1], [])
        print(res, "\n", len(res))
