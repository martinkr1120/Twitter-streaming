import oauth2 as oauth
import json,requests
import os

ACCESS_KEY = "789624266954252288-2a8jGxOIZSitZcoDLrrHIZuwPWu2i5I"
ACCESS_SECRET = "6lkXgLKAKMFFqmP6QZEKcFCIvpTrREFczvYi3In9ob0GX"
CONSUMER_KEY = "CJhL6wqb56Tj5U4AiBz8rWBLg"
CONSUMER_SECRET = "DvCk0NFNJBEvogITwVuRM2iy4PUCIN6oEOOG1rVUuH2zZN6Iqu"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)#client use for http connection


term_0 = input("What do you want to search?")
count = input("How many data do you want?")
date_0 = input("What date do you want to set?:")
choose_time = int(input("What kind of date do you want to set? Input 1 means since date, input 2 means up to date.:"))

if choose_time==1:
    #global search_1
    integra_search = "%20since%3A" + date_0 + '&count=' + count
    search_1 = "https://api.twitter.com/1.1/search/tweets.json?q=" + term_0 + integra_search
if choose_time==2:
    #global search_1
    integra_search = "%20until%3A" + date_0 + '&count=' + count
    search_1 = "https://api.twitter.com/1.1/search/tweets.json?q=" + term_0 + integra_search
else:
    search_1 = "https://api.twitter.com/1.1/search/tweets.json?q=" + term_0 + "%20until%3A" + date_0 + '&count=' + count
    print("Your input is wrong, please input again")

response, data = client.request(search_1)
str_response = data.decode('utf-8')#decode
tweets = json.loads(str_response)
print(tweets)


def Save_Json():
    #/Users/mali/Desktop/
    path = input("Please input a path to save data:")
    def check_folder():
        if not os.path.exists(path):
            os.makedirs(path)

    check_folder()
    #Save tweets data in json
    json.dump(tweets, open(path + term_0 + '_data.dat', 'w'))

if __name__ == '__main__':
    Save_Json()