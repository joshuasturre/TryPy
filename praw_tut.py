import praw

reddit = praw.Reddit(client_id = 'oLYnp8EvajmsTg',
                     client_secret = 'hOfdFDJmlOmiw33x2NumZYsXsSE',
                     username = 'snoos_bitch',
                     password = 'Ashes2009',
                     user_agent = 'praw_lel',)


subreddit = reddit.subreddit(input('What sub should we fetch?'))

hot_subreddit = subreddit.hot(limit=int(input('# posts to show: ')))
show_stickied = input('Show stickied posts? (y/n) ')
for post in hot_subreddit:
    if show_stickied == 'n':
        if not post.stickied:
            print(post.ups,
                  '\n',
                  post.title,
                  '\n', '\n')
    if show_stickied == 'y':
        print(post.ups,
              '\n',
              post.title,
              '\n', '\n')
