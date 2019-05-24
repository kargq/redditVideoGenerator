import praw
from clips import *

print("Subscribe or i'll end humanity.")

reddit = praw.Reddit(client_id='cr4TmbMtqyHJgQ',
                     client_secret='W63uiFhtJY3Lmy87lLlr0zZReRY',
                     user_agent='kindeep')

a_subreddit = reddit.subreddit('AskReddit')

print(a_subreddit.display_name, '\n' + ('=' * len(a_subreddit.display_name)))

enm_imgs = 0

clips = []

for submission in a_subreddit.top(limit=1):
    print("\nTitle:", submission.title)
    print("Author:", submission.author)
    print("\n")
    submission.sort = 'top'
    for comment in submission.comments[:2]:
        print("\nComment: ", comment.body)
        clips.append(create_comment_clip(author=comment.author.name, content=comment.body))
        enm_imgs = enm_imgs + 1

concat_clip = concatenate_videoclips(clips)

concat_clip.write_videofile("media/test.mp4", fps=24)
