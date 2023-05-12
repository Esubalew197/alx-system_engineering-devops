#!/usr/bin/python3
""" web scrapping with requests module """


import requests
url_base = "https://www.reddit.com/r/"


def count_words(subreddit, kw_list=[]):
    """ count the no of key words in a list of titles """
    lst = recurse(subreddit, hot_list=[])
    res = " ".join(lst)
    res = res.lower()
    res = res.split()
    kw_list = " ".join(kw_list)
    kw_list = kw_list.lower()
    kw_list = kw_list.split()
    size = len(kw_list)
    dct = recurse_count(res, kw_list, dct={}, index=0, size=size)
    if not dct:
        return
    srted = sorted(dct.items(), key=lambda k: k[0])
    srted = sorted(srted, key=lambda k: k[1], reverse=True)
    rec_print(srted, index=0, size=len(srted))


def recurse_count(lst, kw_list, dct={}, index=0, size=0):
    """ recursively count kw_list[index] in lst """
    if index == size:
        return dct
    itm = kw_list[index]
    count = lst.count(itm)
    if itm in dct:
        dct[itm] = dct[itm] + count
    else:
        if count:
            dct[itm] = count
    index += 1
    return recurse_count(lst, kw_list, dct, index, size)


def rec_print(lst, index=0, size=0):
    """ recursively print tupule list """
    if index == size:
        return
    print("{}: {}".format(lst[index][0], lst[index][1]))
    index += 1
    return rec_print(lst, index=index, size=size)


def recursor(subreddit, lst, url):
    """ implementation of recursion to get multi pages """
    headers = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        try:
            data = r.json()
            list_of_subreddits = data['data']['children']
            titles = [x.get('data').get('title') for x in list_of_subreddits]
            lst.extend(titles)
            after = data['data']['after']
            if after:
                url = url_base + subreddit + "/hot.json?raw_json=1&after=" + \
                    after
                return recursor(subreddit, lst, url)
            else:
                return lst
        except Exception as e:
            print(e)


def recurse(subreddit, hot_list=[]):
    """ gets the number of subscribers of a subreddit """
    url = url_base + subreddit + "/hot.json?raw_json=1"
    headers = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        try:
            data = r.json()
            list_of_subreddits = data['data']['children']
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
    if len(sys.argv) < 3:
        print("provide url and or subreddit")
        sys.exit(1)
    else:
        kw = [x for x in sys.argv[2].split()]
        count_words(sys.argv[1], kw)
