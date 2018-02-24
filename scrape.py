# import some Python dependencies

import datetime
import json
import time
from urllib.request import urlopen

# Since the code output in this notebook leaks the app_secret,
# it has been reset by the time you read this.

app_id = ""
app_secret = ""  # DO NOT SHARE WITH ANYONE!

access_token = app_id + "|" + app_secret

page_id = 'nytimes'


def testFacebookPageData(page_id, access_token):
    # construct the URL string
    base = "https://graph.facebook.com/v2.4"
    node = "/" + page_id
    parameters = "/?access_token=%s" % access_token
    url = base + node + parameters

    # retrieve data
    response = urlopen(url)
    d = response.read().decode('utf8')
    print(d)
    data = json.loads(d)

    print
    json.dumps(data, indent=4, sort_keys=True)


testFacebookPageData(page_id, access_token)


def request_until_succeed(url):
    success = False
    while success is False:
        try:
            response = urlopen(url)
            if response.getcode() == 200:
                success = True
        except (Exception):
            time.sleep(5)

            print("Error for URL %s: %s" % (url, datetime.datetime.now()))

    return response.read().decode('utf8')


def testFacebookPageFeedData(page_id, access_token):
    # construct the URL string
    base = "https://graph.facebook.com/v2.4"
    node = "/" + page_id + "/feed"  # changed
    parameters = "/?access_token=%s" % access_token
    url = base + node + parameters

    # retrieve data
    data = json.loads(request_until_succeed(url))

    print
    json.dumps(data, indent=4, sort_keys=True)


# testFacebookPageFeedData(page_id, access_token)


def getFacebookPageFeedData(page_id, access_token, num_statuses):
    # construct the URL string
    base = "https://graph.facebook.com"
    node = "/" + page_id + "/feed"
    parameters = "/?fields=message,link,created_time,type,name,id,likes.limit(1).summary(true),comments.limit(1).summary(true),shares&limit=%s&access_token=%s" % (
        num_statuses, access_token)  # changed
    url = base + node + parameters

    # retrieve data
    data = json.loads(request_until_succeed(url))

    return data


test_status = getFacebookPageFeedData(page_id, access_token, 1)["data"][0]
message = test_status["message"]
likes = test_status["likes"]["summary"]["total_count"]
shares = test_status["shares"]["count"]
print (json.dumps(test_status, indent=4, sort_keys=True))
print("message:", message)
print("shares:", shares)
print("likes:", likes)
