import logging

from instagram import post_image, post_mov

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s %(name)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    post_mov("todo.mov")
    post_image("todo.jpg")
