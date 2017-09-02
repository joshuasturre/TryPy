import praw

reddit = praw.Reddit(client_id = 'oLYnp8EvajmsTg',
                     client_secret = 'hOfdFDJmlOmiw33x2NumZYsXsSE',
                     username = 'snoos_bitch',
                     password = 'Ashes2009',
                     user_agent = 'praw_lel',

subreddit = reddit.subreddit('cairns')
hot_cairns = subreddit.hot(limit = 5)

for post in hot_cairns:
    print(post)
