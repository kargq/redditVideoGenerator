import praw
from clips import *
from yt_upload import upload_video

FPS = 30
# DURATION: int = 25
BACKGROUND_TRACK_VOLUME = 0.12
DURATION: int = 60 * 10
DESCRIPTION = "Yes I'm an actual robot. \n"


def random_title_msg():
    return "Subscribe or I'll end humanity."


def write_to_log(text):
    f = open("ask_reddit_log.txt", "a+")
    f.write(text)
    f.close()


def create_submission_video(submission, save_path):
    clips = []
    enm_imgs = 0
    curr_duration: int = 0
    TRANSITION_LEN = gen_transition_clip().duration
    clips.append(gen_intro_clip())
    clips.append(create_comment_clip(
        submission.author.name, "AskReddit: " + submission.title))
    clips.append(gen_transition_clip())
    clips.append(gen_title_message_clip(random_title_msg()))
    submission.sort = 'top'
    submission.comments.replace_more(limit=50)
    for comment in submission.comments:
        print("\nComment: ", comment.body if comment.body else "[deleted]")
        temp = create_comment_clip(
            author=comment.author.name if comment.author else "[deleted]",
            content=comment.body if comment.body else "[deleted]")
        clips.append(gen_transition_clip())
        clips.append(temp)
        enm_imgs = enm_imgs + 1
        curr_duration = curr_duration + temp.duration + TRANSITION_LEN
        if curr_duration >= DURATION:
            break
        print(curr_duration)
    clips.append(gen_intro_clip())
    concat_clip = concatenate_videoclips(clips)
    background_audio = gen_background_audio_clip(
        concat_clip.duration).fx(volumex, BACKGROUND_TRACK_VOLUME)
    concat_clip.audio = CompositeAudioClip(
        [background_audio, concat_clip.audio])
    concat_clip.write_videofile(save_path, fps=FPS)


print("Subscribe or i'll end humanity.")

reddit = praw.Reddit(client_id='cr4TmbMtqyHJgQ',
                     client_secret='W63uiFhtJY3Lmy87lLlr0zZReRY',
                     user_agent='kindeep')

type = input("1. Top 2. Custom 3. Hot: ")

if int(type) == 1:
    a_subreddit = reddit.subreddit('AskReddit')

    print(a_subreddit.display_name, '\n' + ('=' * len(a_subreddit.display_name)))

    for index, submission in enumerate(a_subreddit.top(limit=1)):
        print("\nTitle:", submission.title)
        print("Author:", submission.author)
        print("\n")
        submission.sort = 'top'
        path = "rtemp" + str(index) + ".mp4"
        create_submission_video(submission, path)
        upload_video(path, description="", title="AskReddit: " +
                                                 submission.title, keywords="AskReddit, Reddit")
        clean_temp()
elif int(type) == 2:
    url = input("Enter subreddit submission url: ")
    submission = praw.models.Submission(reddit, url=url)
    print("\nTitle:", submission.title)
    print("Author:", submission.author)
    print("\n")
    submission.sort = 'top'
    path = "media/" + submission.title + "_" + submission.id + ".mp4"
    create_submission_video(submission, path)
    upload_video(path,
                 description=DESCRIPTION + "Link to subreddit post: " + url + "\n" + submission.title,
                 title="AskReddit: " + submission.title, keywords="AskReddit, Reddit")
elif int(type) == 3:
    a_subreddit = reddit.subreddit('AskReddit')
    print(a_subreddit.display_name, '\n' + ('=' * len(a_subreddit.display_name)))
    for index, submission in enumerate(a_subreddit.hot(limit=1)):
        print("\nTitle:", submission.title)
        print("Author:", submission.author)
        print("\n")
        submission.sort = 'top'
        path = "rtemp" + str(index) + ".mp4"
        create_submission_video(submission, path)
        upload_video(path, description="", title="AskReddit: " +
                                                 submission.title, keywords="AskReddit, Reddit")
        clean_temp()