import os
import requests


def post_image(image_url):
    access_token = os.environ["ACCESS_TOKEN"]
    user_id = os.environ["USER_ID"]

    url = f"https://graph.facebook.com/v10.0/{user_id}/media"

    querystring = {
        "access_token": access_token,
        "image_url": image_url,
        "caption": "#imageofday"
    }

    headers = {"Authorization": "Basic Og=="}

    response = requests.request("POST", url, headers=headers, params=querystring)

    container_id = response.json()["id"]

    print(container_id)

    url = f"https://graph.facebook.com/v10.0/{user_id}/media_publish"

    querystring = {
        "access_token": access_token,
        "creation_id": container_id}

    headers = {"Authorization": "Basic Og=="}

    response = requests.request("POST", url, headers=headers, params=querystring)

    print(response.text)


def post_mov(image_url):
    access_token = os.environ["ACCESS_TOKEN"]
    user_id = os.environ["USER_ID"]

    url = f"https://graph.facebook.com/v10.0/{user_id}/media"

    querystring = {
        "media_type": "VIDEO",
        "access_token": access_token,
        "video_url": image_url,
        "caption": "#imageofday"
    }

    headers = {"Authorization": "Basic Og=="}

    response = requests.request("POST", url, headers=headers, params=querystring)

    container_id = response.json()["id"]

    print(container_id)
    # TODO: wait until media is ready

    url = f"https://graph.facebook.com/v10.0/{user_id}/media_publish"

    querystring = {
        "access_token": access_token,
        "creation_id": container_id}

    payload = ""
    headers = {"Authorization": "Basic Og=="}

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)
