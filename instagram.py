import os
import requests


def post_image(image_url: str):
    access_token = os.environ["ACCESS_TOKEN"]
    instagram_business_user_id = os.environ["USER_ID"]

    url = f"https://graph.facebook.com/v10.0/{instagram_business_user_id}/media"

    querystring = {
        "access_token": access_token,
        "image_url": image_url,
        "caption": "#imageofday"
    }

    headers = {"Authorization": "Basic Og=="}

    response = requests.request("POST", url, headers=headers, params=querystring)

    container_id = response.json()["id"]

    print(container_id)

    url = f"https://graph.facebook.com/v10.0/{instagram_business_user_id}/media_publish"

    querystring = {
        "access_token": access_token,
        "creation_id": container_id}

    headers = {"Authorization": "Basic Og=="}

    response = requests.request("POST", url, headers=headers, params=querystring)

    print(response.text)


def post_mov(image_url: str):
    access_token = os.environ["ACCESS_TOKEN"]
    instagram_business_user_id = os.environ["USER_ID"]

    url = f"https://graph.facebook.com/v10.0/{instagram_business_user_id}/media"

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

    url = f"https://graph.facebook.com/v10.0/{instagram_business_user_id}/media_publish"

    querystring = {
        "access_token": access_token,
        "creation_id": container_id}

    payload = ""
    headers = {"Authorization": "Basic Og=="}

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)


def exchange_token_to_long_lived_token(short_lived_token: str) -> str:
    """The initial token lives for 1h, the long lived token lives for 60 days"""
    app_secret = os.environ["APP_SECRET"]
    app_id =  os.environ["APP_ID"]

    url = "https://graph.facebook.com/v10.0/oauth/access_token"

    querystring = {"grant_type": "fb_exchange_token",
                   "client_id": app_id,
                   "client_secret": app_secret,
                   "fb_exchange_token": short_lived_token}

    response = requests.request("GET", url, params=querystring)

    return response.json()["access_token"]
