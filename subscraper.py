import time
import praw
import random
import webbrowser

print ('''
   ▄████████ ███    █▄  ▀█████████▄          ▄████████  ▄████████    ▄████████    ▄████████    ▄███████▄    ▄████████    ▄████████
  ███    ███ ███    ███   ███    ███        ███    ███ ███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███
  ███    █▀  ███    ███   ███    ███        ███    █▀  ███    █▀    ███    ███   ███    ███   ███    ███   ███    █▀    ███    ███
  ███        ███    ███  ▄███▄▄▄██▀         ███        ███         ▄███▄▄▄▄██▀   ███    ███   ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀
▀███████████ ███    ███ ▀▀███▀▀▀██▄       ▀███████████ ███        ▀▀███▀▀▀▀▀   ▀███████████ ▀█████████▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀
         ███ ███    ███   ███    ██▄               ███ ███    █▄  ▀███████████   ███    ███   ███          ███    █▄  ▀███████████
   ▄█    ███ ███    ███   ███    ███         ▄█    ███ ███    ███   ███    ███   ███    ███   ███          ███    ███   ███    ███
 ▄████████▀  ████████▀  ▄█████████▀        ▄████████▀  ████████▀    ███    ███   ███    █▀   ▄████▀        ██████████   ███    ███
                                                                    ███    ███                                          ███    ███
''')
time.sleep(2)
while True:
    sub = input("What Subreddit would you like to scrape? ")
    choice = input('''
    (1). Hot
    (2). New
    (3). Controversial
    (4). Top
    (5). Rising
    ''').lower()

    reddit = praw.Reddit(client_id='sqFdPyHILCU5WA',
    client_secret='B0gFCfhEMCv9i1DfDNQr8wVGsyY',
    user_agent='pyTerm',
    username = 'Roosty_Balboa',
    password = 'Redstone04')
    subreddit = reddit.subreddit(sub)
    if choice == "1":
        posts = subreddit.hot(limit=500)
        random_post_number = random.randint(0,100)
        for i,post in enumerate(posts):
            if i == random_post_number:
                print (post.url)
                webbrowser.open(post.url)
    elif choice == "2":
        posts = subreddit.new(limit=500)
        random_post_number = random.randint(0,100)
        for i,post in enumerate(posts):
            if i == random_post_number:
                print (post.url)
                webbrowser.open(post.url)
    elif choice == "3":
        posts = subreddit.controversial(limit=500)
        random_post_number = random.randint(0,100)
        for i,post in enumerate(posts):
            if i == random_post_number:
                print (post.url)
                webbrowser.open(post.url)
    elif choice == "4":
        posts = subreddit.top(limit=500)
        random_post_number = random.randint(0,100)
        for i,post in enumerate(posts):
            if i == random_post_number:
                print (post.url)
                webbrowser.open(post.url)
    elif choice == "5":
        posts = subreddit.rising(limit=500)
        random_post_number = random.randint(0,100)
        for i,post in enumerate(posts):
            if i == random_post_number:
                print (post.url)
                webbrowser.open(post.url)
