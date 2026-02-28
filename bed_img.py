from PIL import Image, ImageOps
from pathlib import Path

BED_TOP = (256, 512) # Dimensions of the top of bed texture at 1024x1024
LEFT_UPPER = (96, 96) # Coordinate of left upper bed top for 1024x1024 bed texture
RIGHT_LOWER = (351, 607) # Coordinate of right lower bed top for 1024x1024 bed texture

def load_bed(color: str) -> Image.Image:
    color_path = f"beds/{color}.png"
    if Path(color_path).exists():
        bed = Image.open(color_path)
        return bed

    return None

def load_img(path: str) -> Image.Image:
    try:
        bed = Image.open(path)
        return bed
    except Exception as e:
        print(e)

    return None
    
# Basically, crop out the center of the image that has a 1:2 aspect ratio and then resize it to 256x512
def crop_image(img: Image.Image) -> Image.Image:
    if not img:
        return None
    
    # Is the width greater than half of the height?
    # Then get the part that is a 1:2 ratio... or something
    if img.width > img.height / 2:
        diff = img.width - img.height / 2
        return img.resize(size = BED_TOP, box = (diff / 2, 0, img.width - diff / 2, img.height))
    # Is the height greater than twice the width?
    # I'm not gonna lie, I don't remember how this works
    elif img.height > img.width * 2:
        diff = img.height - img.width * 2
        return img.resize(size = BED_TOP, box = (0, diff / 2, img.width, img.height - diff / 2))
    # Otherwise, just resize that thing to 256x512
    else:
        return img.resize(size = BED_TOP)
    
# Time to stretch an image to 256x512, doesn't matter about any aspect ratios
def stretch_image(img: Image.Image) -> Image.Image:
    if not img:
        return None
    
    # Just resize that image, that's all
    return img.resize(size = BED_TOP)


# Pad out the top of the image to have a 1:2 aspect ratio and bring that thing to 256x512
def pad_image(img: Image.Image) -> Image.Image:
    if not img:
        return None
    
    # Is the height greater than twice the width?
    # Pad out the width to get a 1:2 aspect ratio
    elif img.height > img.width * 2:
        diff = int((img.height / 2 - img.width)//2)
        return ImageOps.expand(img, border=(diff, 0, diff, 0)).resize(size = BED_TOP)
    # Otherwise, just pad out the height and resize that thing to 256x512
    else:
        diff = int((img.width * 2 - img.height)//2)
        return ImageOps.expand(img, border=(0, diff, 0, diff)).resize(size = BED_TOP)


# MAKE THAT CUSTOM BED TEXTURE
def make_bed(bed_img: Image.Image, img: Image.Image, fit='crop') -> Image.Image:
    if not bed_img or not img:
        return None
    
    # Make resized bed texture
    new_bed = bed_img.resize([1024,1024], resample=0)

    # Make a variable for the eventual image
    bed_top = None
    match fit:
        case 'crop':
            bed_top = crop_image(img)
        case 'stretch':
            bed_top = stretch_image(img)
        case 'pad':
            bed_top = pad_image(img)

    # I do in fact need this
    bed_top = bed_top.convert('RGBA')
    # Paste that image on top of the bed
    new_bed.alpha_composite(im = bed_top, dest = LEFT_UPPER)
    return new_bed