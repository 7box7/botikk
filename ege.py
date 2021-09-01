from time import time, sleep
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import requests
import os
import json

#tok = str(os.environ.get('VK1'))
tok2 = str(os.environ.get('VK2'))
#tok2 = str("7d977d1ac381b8deabb8ef0969ebf9188c8b0be1e16941fc3fdc3496d06f5903c6ad53b3fb87c628b7f8d")

#vk = vk_api.VkApi(token=tok)
vk_group = vk_api.VkApi(token=tok2)

"""
while True:
    sleep(2)
    g = vk.method('status.get', {'user_id': '393598407'})
    b = g["text"]
    alll = vk_group.method('messages.search', {'peer_id': '393598407', 'q': '.', 'count': 1})['items'][0]['text']
    if alll == b or b == "":
        continue
    g = vk_group.method('messages.send', {'user_id': '393598407', 'message': b, 'random_id': int(time())})
    continue
"""

"""
data = vk_group.method('groups.getLongPollServer', {'group_id': '172955888'})
print(data)
while True:
    response = requests.get(
        '{server}?act=a_check&key={key}&ts={ts}&wait=25'.format(server=data['server'],
                                                                key=data['key'],
                                                                ts=data['ts'])).json()
    print(response)
    updates = response['updates']
    if updates:
        for element in updates:
            print(element)
    data['ts'] = response['ts']
"""
#395952683
#233764475
while True:
    longpoll = VkBotLongPoll(vk_group, 172955888)
    try:
        for event in longpoll.listen():
            if event.object.message["from_id"] == 393598407:
                query_json = json.dumps(
                    {"peer_id": event.object.message["peer_id"], "conversation_message_ids": event.object.message["conversation_message_id"], "is_reply": True})
                a = vk_group.method("photos.getMessagesUploadServer")
                b = requests.post(a['upload_url'], files={'photo': open('file.jpg', 'rb')}).json()
                c = vk_group.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
                att = "photo{}_{}".format(c["owner_id"], c["id"])
                vk_group.method('messages.send', {'peer_id': event.object.message["peer_id"], "attachment": att, 'random_id': int(time()), "forward": [query_json]})
    except requests.exceptions.ReadTimeout as timeout:
        continue
