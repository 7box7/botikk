from time import time, sleep
import vk_api
import os

tok = str(os.environ.get('VK_KEY2'))
tok2 = str(os.environ.get('VK_KEY'))

vk = vk_api.VkApi(token=tok)
vk_group = vk_api.VkApi(token=tok2)


while True:
    sleep(2)
    g = vk.method('status.get', {'user_id': '493552486'})
    b = g["text"]
    alll = vk_group.method('messages.search', {'peer_id': '393598407', 'q': '.', 'count': 1})['items'][0]['text']
    if alll == b or b == "":
        continue
    g = vk_group.method('messages.send', {'user_id': '393598407', 'message': b, 'random_id': int(time())})
    continue
