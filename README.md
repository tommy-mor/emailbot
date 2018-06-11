# emailbot
personal script that can email me reminders/digests etc

connects to the google api
run the script in an env with a browser to setup the credentials with google api.
to run headless, copy the credentials.json and client_secret.json to the same directory as script

to setup the gmail api, run emailreminder.py when connected to a monitor.


to setup the reddit api, make a reddit api bot according to [this tutorial](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps), then create a file in the root directory of project according to the instructions in reddit.py

also, make a file named subs.txt with this format
```
sender email (the account you used for gmail api)
destination_email subreddit number_of_posts
destination_email subreddit number_of_posts
... (for as many subreddits as you want)
```

to run, run the file sched.py with arguments with python3

## todo
- make it so it emails actually the right person
- make it so that you can config ur subreddits in a file
- make it so that you can email ur friends too
