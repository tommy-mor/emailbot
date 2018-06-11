import emailreminder
import praw
helpmsg = """
store your reddit info in a file like this:
info.txt
-----
reddit_username
reddit_password
app client ID
app client secret
"""
def get_reddit_posts(jobs):
    try:
        with open('info.txt') as f:
            uname = f.readline().strip()
            pw = f.readline().strip()
            clientid = f.readline().strip()
            clientsecret = f.readline().strip()

        reddit = praw.Reddit(client_id=clientid,
                            client_secret=clientsecret,
                            username=uname,
                            password=pw,
                            user_agent='email reminder bot')

        posts = []
        for sub, n in jobs:
            postsforsub = {'name': sub, 'posts': list()}
            for submission in reddit.subreddit(sub).top('day', limit=int(n)):
                postsforsub['posts'].append({'score': submission.score,
                                            'title': submission.title,
                                            'url': submission.url})
            posts.append(postsforsub)
        return posts
    except FileNotFoundError as e:
        print("you need to put your reddit details in a file like: %s" % helpmsg)
