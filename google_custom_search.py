#-*- coding:utf-8 -*-
#https://geeknavi.net/aws/posting-image-of-gohandesuyo-at-noon
#https://qiita.com/Hironsan/items/0eb5578f3321c72637b4
#https://qiita.com/tadaken3/items/0998c18df11d4a1c7427
import json
import random
import requests
import urllib.request
import urllib.parse
import keys



def get_image_urls(search_word):
    CUSTOM_SEARCH_API_KEY = keys.CUSTOM_SEARCH_API_KEY
    CUSTOM_SEARCH_ENGINE_ID = keys.CUSTOM_SEARCH_ENGINE_ID
    custom_search_url = f"https://www.googleapis.com/customsearch/v1?key={CUSTOM_SEARCH_API_KEY}&cx={CUSTOM_SEARCH_ENGINE_ID}&searchType=image&q={search_word}&num=10"

    img_urls = []
    res = urllib.request.urlopen(custom_search_url)
    data = json.loads(res.read().decode('utf-8'))
    for i in range(len(data["items"])):
        img_urls.append(data["items"][i]["link"])
    return img_urls



def line(img):
    LINE_NOTIFY_TOKEN = keys.LINE_NOTIFY_TOKEN
    line_notify_url = 'https://notify-api.line.me/api/notify'

    message = '起きる時間です'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + LINE_NOTIFY_TOKEN}
    files = {"imageFile": img}
    r = requests.post(line_notify_url, headers=headers, params=payload, files=files)



def main():
    search_words = ['千代丸', '遠藤関', '高見盛', '朝青龍', '寺尾力士', 'わんぱく相撲']
    search_word = random.choice(search_words)
    search_word = urllib.parse.quote(search_word)

    img_urls = get_image_urls(search_word)
    img_url = random.choice(img_urls)
    img = requests.get(img_url).content
    return line(img)



if __name__ == '__main__':
    main()
