import os
from PIL import Image


def get_image_name(album):
    return album.album_name + '.jpg'


def create_collage(albums):
    os.chdir('./cache/')

    im = Image.open(get_image_name(albums[0]))

    width = im.size[0]
    height = im.size[1]

    im = Image.new("RGB", (width * 5, height * 5))

    for y in range(0, 5):
        for x in range(0, 5):
            print(get_image_name(albums[y * 5 + x]))
            im_buff = Image.open(get_image_name(albums[y * 5 + x]))
            im.paste(im_buff, (x * width, y * height))

    os.chdir('../')
    im.save("result.jpeg")
