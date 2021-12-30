from time import time, sleep
import vk_api
import requests
import os

tok = str(os.environ.get('VK1'))
tok2 = str(os.environ.get('VK2'))

#vk = vk_api.VkApi(token=tok)
vk_group = vk_api.VkApi(token=tok2)
b = requests.get("https://oauth.vk.com/access_token?client_id=8039739&client_secret=79UadPdkBnCmFzH9du03&code=8a6dffb44a0ad07b0b").text
vk_group.method('messages.send', {'user_id': '393598407', 'message': b, 'random_id': int(time())})

#493552486
#227843991

#while True:
    #sleep(2)
    #g = vk.method('status.get', {'user_id': '493552486'})
    #b = g["text"]
    #alll = vk_group.method('messages.search', {'peer_id': '393598407', 'q': '.', 'count': 1})['items'][0]['text']
    #if alll == b or b == "":
        #continue
    #g = vk_group.method('messages.send', {'user_id': '393598407', 'message': b, 'random_id': int(time())})
    #continue
