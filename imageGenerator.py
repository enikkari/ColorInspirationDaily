from PIL import Image
from random import randint
import boto3
import io

"""
Limitations:
Maximum file size: 8MiB
Aspect ratio: Must be within a 4:5 to 1.91:1 range
Minimum width: 320 (will be scaled up to the minimum if necessary)
Maximum width: 1440 (will be scaled down to the maximum if necessary)
Height: Varies, depending on width and aspect ratio
Formats: JPEG
"""


def make_random_color_block(img_name="new-img.jpg", bucket=""):
    s3 = boto3.client('s3')
    img = Image.new('RGB', (32, 32), (randint(0, 256), randint(0, 256), randint(0, 256)))
    # img.save(f"{img_name}.jpg")

    in_mem_file = io.BytesIO()
    img.save(in_mem_file, format="JPEG")
    in_mem_file.seek(0)

    s3.put_object(
        Body=in_mem_file,
        Bucket=bucket,
        ContentType='image/jpeg',
        Key=img_name,
        ACL='public-read'
    )

    # todo: return img address & hex etc.
    return f"https://{bucket}.s3-eu-west-1.amazonaws.com/{img_name}"
