import sms
import praw

class DealBot():

    def __init__(self):
        self.post_list = []
        self.user_agent = ("/r/buildapcsales deal finder by /u/OmkarEdits")
        self.reddit = praw.Reddit(user_agent = self.user_agent)

        self.reddit.login()  # login to reddit

    def update_posts(self):
        sub = self.reddit.get_subreddit("buildapcsales", fetch=True)
        posts = sub.get_new(limit=10)

        for submission in posts:
            print submission.title
            print submission.nsfw

    def matches_search(self, submission):
        print "white space is retarded"


d = DealBot()
d.update_posts()
