import sms
import praw
import globals

class DealBot():

    def __init__(self):
        print("dealsbot is running...")
        self.post_list = []
        self.user_agent = ("/r/buildapcsales deal finder by /u/OmkarEdits")
        self.reddit = praw.Reddit(user_agent = self.user_agent)

        self.reddit.login(username=globals.USERNAME, password=globals.PASSWORD, disable_warning=True)  # login to reddit

    def update_posts(self):
        sub = self.reddit.get_subreddit("buildapcsales", fetch=True)
        posts = sub.get_new(limit=10)

        for submission in posts:
            print submission.title
            # print submission.nsfw

    def matches_search(self, submission):
        print "white space blows"


d = DealBot()
d.update_posts()
