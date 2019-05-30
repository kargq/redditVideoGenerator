from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
from moviepy.editor import *

WIDTH = 1920
HEIGHT = 1080


def gen_comment_image(author, content):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(26, 26, 27))
    fnt = ImageFont.truetype('sans-serif.ttf', 30)
    d = ImageDraw.Draw(img)
    d.text((10, 10), author, fill=(79, 188, 255), font=fnt)
    d.text((10, 45), content, fill=(255, 255, 255), font=fnt)
    # img.save(save_path)
    return np.array(img)


def create_comment_clip(author, content):
    background_clip = ImageClip(gen_comment_image(author=author, content=content))
    return background_clip.set_duration(10)

def gen_audio_clip(text):

    