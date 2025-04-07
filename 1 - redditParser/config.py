import praw
reddit = praw.Reddit(client_id = 'CLIENT_ID',
                     client_secret = 'CLIENT_SECRET',
                     username = 'USERNAME',
                     password = 'PASSWORD',
                     user_agent = 'Comment Extraction',
                     chache_timeout = 0)
post = 'l7ckr5'
