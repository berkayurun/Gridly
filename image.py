import os
from PIL import Image



def get_image_name(lastfmObject):
    name = lastfmObject.name.replace('/', '_')
    return name + '.jpg'


def create_collage(lastfmObjects, X_SIZE, Y_SIZE):
    os.chdir('./cache/')

    im = Image.open(get_image_name(lastfmObjects[0]))

    width = im.size[0]
    height = im.size[1]

    im = Image.new("RGB", (width * X_SIZE, height * Y_SIZE))

    for y in range(0, Y_SIZE):
        for x in range(0, X_SIZE):
            print(get_image_name(lastfmObjects[y * X_SIZE + x]))
            try:
                im_buff = Image.open(get_image_name(lastfmObjects[y * X_SIZE + x]))
            except:
                im_buff = Image.new('RGB',(width,height),'black')
            im.paste(im_buff, (x * width, y * height))

    os.chdir('../')

    im.save(f"{lastfmObjects[0].__class__.__name__}.jpeg")
