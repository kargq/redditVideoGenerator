from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def gen_comment_image(author, content):
    img = Image.new('RGB', (1920, 1080), color=(26, 26, 27))
    fnt = ImageFont.truetype('sans-serif.ttf', 30)
    d = ImageDraw.Draw(img)
    d.text((10, 10), author, fill=(79, 188, 255), font=fnt)
    d.text((10, 45), content, fill=(255, 255, 255), font=fnt)
    img.save('media/pil_color.png')


gen_comment_image(author="kindeep", content="why not just use bots eh")
