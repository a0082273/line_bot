#-*- coding:utf-8 -*-
import json
import random
import requests
import urllib.request
import time
import keys



def get_image_urls(search_word):
    CUSTOM_SEARCH_API_KEY = keys.CUSTOM_SEARCH_API_KEY
    CUSTOM_SEARCH_ENGINE_ID = keys.CUSTOM_SEARCH_ENGINE_ID
    query_img = f"https://www.googleapis.com/customsearch/v1?key={CUSTOM_SEARCH_API_KEY}&cx={CUSTOM_SEARCH_ENGINE_ID}&searchType=image&q={search_word}&num=10"

    img_urls = []
    res = urllib.request.urlopen(query_img)
    data = json.loads(res.read().decode('utf-8'))
    for i in range(len(data["items"])):
        img_urls.append(data["items"][i]["link"])
    return img_urls


def line(img):
    line_notify_token = keys.LINE_NOTIFY_TOKEN
    line_notify_api = 'https://notify-api.line.me/api/notify'

    message = '起きる時間です'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    files = {"imageFile": img}
    return requests.post(line_notify_api, headers=headers, params=payload, files=files)


def main():
    search_words = ['かわいい猫', 'かわいい動物', '動物赤ちゃん', '癒やし動物', '癒やし猫']
    for i in range(5):
        search_word = random.choice(search_words)
        search_word = urllib.parse.quote(search_word)
        urls = get_image_urls(search_word)
        url = random.choice(urls)
        img = requests.get(url).content
        line(img)
        time.sleep(5)


def lambda_handler(event, context):
    main()
