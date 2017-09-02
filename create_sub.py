import praw

reddit = praw.Reddit(client_id = 'oLYnp8EvajmsTg',
                     client_secret = 'hOfdFDJmlOmiw33x2NumZYsXsSE',
                     username = 'snoos_bitch',
                     password = 'Ashes2009',
                     user_agent = 'praw_lel',)

reddit.subreddit.create('snoos_bitch', title = None, link_type = 'any', subreddit_type = 'public', wikimode = 'modonly')
