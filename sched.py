import emailreminder
import argparse
import schedule
import time
import reddit

parser = argparse.ArgumentParser()
parser.add_argument('--num', dest='num', type=int, default=10)
parser.add_argument('--subs', dest='subs', type=str, nargs='+', default=['all'])
parser.add_argument('--time', dest='time', type=str, default=None, help='if this option is used and given HH:MM time format, it will run at that time every day')
def get_details_from_file():
    with open('subs.txt') as f:
        source_email = f.readline().strip()
        jobs = [tuple(x.strip().split()) for x in f]
    return (source_email, jobs)

def do_email(source, dest, jobs):
    p = reddit.get_reddit_posts(jobs)
    email = "welcome to your reddit daily digest"
    for sub in p:
        email += "<h4>%s</h4>" % sub['name']
        email += "<br>".join(["%d -- %s -- <a href=\"%s\">link</a>" % (post['score'], post['title'], post['url'])
                              for post in sub['posts']])
    emailreminder.send_email('reddit digest', email, dest, source)

args = parser.parse_args()
detalis = get_details_from_file()
if (args.time):
    schedule.every().day.at(args.time).do(do_email)
    while True:
        schedule.run_pending()
        time.sleep(60)
else:
    source, jobs =  get_details_from_file()
    destsmap = {}
    for dest, sub, n in jobs:
        if dest not in destsmap: destsmap[dest] = list()
        destsmap[dest].append((sub, n))
    for dest, jobs in destsmap.items():
        do_email(source, dest, jobs)


