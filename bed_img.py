from PIL import Image
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

def preview_img(img: Image.Image) -> Image.Image:
    if not img:
        return None
    
    scale = 1.0

    if img.width >= img.height:
        scale = 256 / img.width
    else:
        scale = 256 / img.height

    return img.resize([int(img.width * scale), int(img.height * scale)])
    
def make_bed(bed_img: Image.Image, custom_img: Image.Image) -> Image.Image:
    if not bed_img or not custom_img:
        return None
    
    # Make resized bed texture
    new_bed = bed_img.resize([1024,1024], resample=0)

    # Modify custom image to be placed on bed
    bed_top = None
    if custom_img.width > custom_img.height / 2:
        diff = custom_img.width - custom_img.height / 2
        bed_top = custom_img.resize(size = BED_TOP, box = (diff / 2, 0, custom_img.width - diff / 2, custom_img.height))
    elif custom_img.height > custom_img.width * 2:
        diff = custom_img.height - custom_img.width * 2
        bed_top = custom_img.resize(size = BED_TOP, box = (0, diff / 2, custom_img.width, custom_img.height - diff / 2))
    else:
        bed_top = custom_img.resize(size = BED_TOP)

    bed_top = bed_top.convert('RGBA')
    new_bed.alpha_composite(im = bed_top, dest = LEFT_UPPER)
    return new_bed