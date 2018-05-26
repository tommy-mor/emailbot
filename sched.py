import emailreminder
import argparse
import schedule
import time
import reddit

parser = argparse.ArgumentParser()
parser.add_argument('--schedule', dest='sched', action='store_const', default=False, const=True)
args = parser.parse_args()
print(args.sched)
if (args.sched):
    schedule.every().day.at("13:00").do(emailreminder.send_email)
    while True:
        schedule.run_pending()
    time.sleep(60)
else:
    p = reddit.get_reddit_posts(['hiphopheads','globaloffensive'])
    email = """
<b>this is the email test %s,</b>
second thing %s
    """ % (p[0]['posts'][0], p[1]['posts'][1])
    emailreminder.send_email('reddit digest', email)


