#-*- coding:utf-8 -*-
#https://geeknavi.net/aws/posting-image-of-gohandesuyo-at-noon
#https://qiita.com/Hironsan/items/0eb5578f3321c72637b4
import json
import random
import requests
import urllib.request
import httplib2
import keys



def get_image_urls(search_word):
    CUSTOM_SEARCH_API_KEY = keys.CUSTOM_SEARCH_API_KEY
    CUSTOM_SEARCH_ENGINE_ID = keys.CUSTOM_SEARCH_ENGINE_ID
    query_img = f"https://www.googleapis.com/customsearch/v1?key={CUSTOM_SEARCH_API_KEY}&cx={CUSTOM_SEARCH_ENGINE_ID}&searchType=image&q={search_word}&num=5"

    img_urls = []
    res = urllib.request.urlopen(query_img)
    data = json.loads(res.read().decode('utf-8'))
    for i in range(len(data["items"])):
        img_urls.append(data["items"][i]["link"])
    print(len(img_urls))
    return img_urls



def get_image(img_url):
    opener = urllib.request.build_opener()
    http = httplib2.Http()
    response, content = http.request(img_url)
    return content



def line(img):
    line_notify_token = keys.line_notify_token
    line_notify_api = 'https://notify-api.line.me/api/notify'

    message = '起きる時間です'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    files = {"imageFile": img}
    r = requests.post(line_notify_api, headers=headers, params=payload, files=files)



def main():
    search_word = 'dmm%E6%96%B0%E4%BA%BA'
    urls = get_image_urls(search_word)
    if len(urls) == 0:
        return "no images were found."
    url = random.choice(urls)
    img = get_image(url)
    return line(img)



if __name__ == '__main__':
    main()
