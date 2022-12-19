import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

PRINT_NAMES = False


def get_image_name(lastfmObject):
    name = lastfmObject.name.replace('/', '_')
    return name + '.jpg'


def add_text(text: str, img):
    width = img.size[0]
    height = img.size[1]

    if len(text) >= 19:
        text = text[:16]
        text = text + '...'

    draw = ImageDraw.Draw(img, 'RGBA')
    font = ImageFont.truetype("../config/arial.ttf", int(width/10))
    bbox = draw.textbbox((width / 2, 9 * height / 10),
                         text, font=font, anchor='mm')
    left, top, right, bottom = draw.textbbox(
        (width / 2, 9 * height / 10), text, anchor='mm', font=font)
    draw.rectangle((left - 5, top - 5, right + 5,
                   bottom+5), fill=(255, 255, 255, 130))
    draw.text((width / 2, 9 * height / 10),
              text=text, fill='black', anchor="mm", font=font)


def create_collage(lastfmObjects, X_SIZE, Y_SIZE):
    os.chdir('./cache/')

    im = Image.open(get_image_name(lastfmObjects[0]))

    width = im.size[0]
    height = im.size[1]

    im = Image.new("RGB", (width * X_SIZE, height * Y_SIZE))

    for y in range(0, Y_SIZE):
        for x in range(0, X_SIZE):
            try:
                obj = lastfmObjects[y * X_SIZE + x]
                im_buff = Image.open(get_image_name(
                    obj))

                if im_buff.format != 'RGB':
                    im_buff = im_buff.convert('RGB')

                im_buff = im_buff.resize((width, height))

                if PRINT_NAMES:
                    add_text(obj.name, im_buff)
            except Exception as e:
                print(e)
                im_buff = Image.new('RGB', (width, height), 'black')
            im.paste(im_buff, (x * width, y * height))

    os.chdir('../')

    im.save(f"{lastfmObjects[0].__class__.__name__}.jpeg")
