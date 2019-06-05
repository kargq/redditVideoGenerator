from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
from moviepy.editor import *
import soundfile as sf
from pydub import AudioSegment
from pydub.playback import play

from gtts import gTTS
from io import BytesIO

WIDTH = 1920
HEIGHT = 1080


def gen_comment_image(author, content):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(26, 26, 27))
    fnt = ImageFont.truetype('sans-serif.ttf', 30)
    d = ImageDraw.Draw(img)
    d.text((10, 10), author, fill=(79, 188, 255), font=fnt)
    d.text((10, 45), content, fill=(255, 255, 255), font=fnt)
    return np.array(img)


def gen_title_message_image(msg):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(26, 26, 27))
    fnt = ImageFont.truetype('sans-serif.ttf', 60)
    d = ImageDraw.Draw(img)
    d.text((10, 10), msg, fill=(200, 188, 255), font=fnt)
    return np.array(img)


def gen_title_message_clip(msg):
    background_clip = ImageClip(gen_title_message_image(msg))
    audio_clip = gen_audio_clip(msg)
    background_clip = background_clip.set_duration(audio_clip.duration)
    background_clip = background_clip.set_audio(audio_clip)
    return background_clip


def create_comment_clip(author, content):
    background_clip = ImageClip(
        gen_comment_image(author=author, content=content))
    audio_clip = gen_audio_clip(content)
    background_clip = background_clip.set_duration(audio_clip.duration)
    background_clip = background_clip.set_audio(audio_clip)
    return background_clip


def gen_audio_clip(text):
    tts = gTTS(text, 'en')
    tts.save("temp.mp3")
    clip = AudioFileClip("temp.mp3")
    return clip
