import praw
from time import sleep


def main():
    reddit = praw.Reddit(client_id='GFF6vuIdXF-pEA', client_secret='-XxyYOgtQrUcniCyRcZH48pqt3A', username='TchallaIsMySon', password='nishu5499', user_agent='suicide bot at your service')
    subreddit = reddit.subreddit('mytestinggroundforbot')
    file = open('thoughts.txt', 'r')
    triggers = []
    for f in file:
        triggers.append(f.rstrip())
    file.close()
    comments = subreddit.stream.comments(skip_existing=True)
    for comment in comments:
        replied = process_reply(comment, triggers)
        if replied:
            print('posted to ' + comment.author.name)
            break


def process_reply(comment, triggers):
    f = open('reply.txt', 'r')
    message = f.read()
    f.close()
    body = comment.body.lower()
    for trigger in triggers:
        if trigger in body:
            comment.reply(message)
            return True
    return False


if __name__ == '__main__':
    print('running...')
    while(not sleep(5)):
        main()
        print('sleeping..')
