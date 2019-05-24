from moviepy.editor import *
import imgkit
from clips import  *

def comment_html(username, content):
    str = "<!DOCTYPE html><html><head>" \
          "<style>body {background-color: rgb(26, 26, 27);color: white;font-family: BentonSans, sans-serif;}.username {color: rgb(79, 188, 255);}.content {padding: 5px}.header {padding: 0 0 0 5px}</style>" \
          "</head>" \
          "<body><div><div class = 'header'><span class=username>"+username + \
        "</span></div><div class = 'content'>" + content + "</div></div></body></html>"
    return str


gen_comment_image("kindeep", "something", "media/test.png")
img_clip = ImageClip("media/test.png").set_duration(10)

imgs = ["media/test.png", "media/test.1.png"]

clips = [ImageClip(m).set_duration(2) for m in imgs]

concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile("media/test.mp4", fps=24)
