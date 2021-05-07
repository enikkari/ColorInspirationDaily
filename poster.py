import logging

from instagram import post_image, post_mov
from imageGenerator import make_random_color_block

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s %(name)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    img_url = make_random_color_block()
    post_image(img_url)

    # post_mov("todo.mov")
