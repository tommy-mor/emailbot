import emailreminder
import argparse
import schedule
import time

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
    emailreminder.send_email()
