import praw
from clips import *

FPS = 30


def create_submission_video(submission, save_path):
    clips = []
    enm_imgs = 0
    submission.sort = 'top'
    for comment in submission.comments[:2]:
        print("\nComment: ", comment.body)
        clips.append(create_comment_clip(author=comment.author.name, content=comment.body))
        enm_imgs = enm_imgs + 1
    concat_clip = concatenate_videoclips(clips)
    concat_clip.write_videofile(save_path, fps=FPS)


print("Subscribe or i'll end humanity.")

reddit = praw.Reddit(client_id='cr4TmbMtqyHJgQ',
                     client_secret='W63uiFhtJY3Lmy87lLlr0zZReRY',
                     user_agent='kindeep')

a_subreddit = reddit.subreddit('AskReddit')

print(a_subreddit.display_name, '\n' + ('=' * len(a_subreddit.display_name)))

for index, submission in enumerate(a_subreddit.top(limit=3)):
    print("\nTitle:", submission.title)
    print("Author:", submission.author)
    print("\n")
    submission.sort = 'top'
    create_submission_video(submission, "media/askreddit_submission_test" + str(index) + ".mp4")
