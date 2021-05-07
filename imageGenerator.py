from PIL import Image
from random import randint

"""
Limitations:
Maximum file size: 8MiB
Aspect ratio: Must be within a 4:5 to 1.91:1 range
Minimum width: 320 (will be scaled up to the minimum if necessary)
Maximum width: 1440 (will be scaled down to the maximum if necessary)
Height: Varies, depending on width and aspect ratio
Formats: JPEG
"""


def make_random_color_block():
    img = Image.new('RGB', (320, 320), (randint(0, 256), randint(0, 256), randint(0, 256)))
    img.save("new.jpg") # TODO save to s3
