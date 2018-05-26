import emailreminder
import argparse
import schedule
import time
import reddit

parser = argparse.ArgumentParser()
parser.add_argument('--num', dest='num', type=int, default=10)
parser.add_argument('--subs', dest='subs', type=str, nargs='+', default=['all'])
parser.add_argument('--time', dest='time', type=str, default=None, help='if this option is used and given HH:MM time format, it will run at that time every day')
def do_email():
    p = reddit.get_reddit_posts(args.subs, args.num)
    email = "welcome to your reddit daily digest"
    for sub in p:
        email += "<h4>%s</h4>" % sub['name']
        email += "<br>".join(["%d -- %s -- <a href=\"%s\">link</a>" % (post['score'], post['title'], post['url'])
                              for post in sub['posts']])
    emailreminder.send_email('reddit digest', email)

args = parser.parse_args()
if (args.time):
    schedule.every().day.at(args.time).do(do_email)
    while True:
        schedule.run_pending()
        time.sleep(60)
else:
    do_email()


