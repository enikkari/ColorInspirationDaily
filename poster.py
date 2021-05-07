import logging

from instagram import post_image, post_mov
from imageGenerator import make_random_color_block

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s %(name)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    img_url, rgb = make_random_color_block()
    hex = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
    # TODO cmyk HSC HSL
    post_image(img_url,
               color_info_string=f"\n\nrgb({rgb[0]}, {rgb[1]}, {rgb[2]})\nhex {hex}\n\n")

    # post_mov("todo.mov")
