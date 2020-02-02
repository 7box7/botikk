import time
import vk_api
import requests

vk = vk_api.VkApi(token='7d977d1ac381b8deabb8ef0969ebf9188c8b0be1e16941fc3fdc3496d06f5903c6ad53b3fb87c628b7f8d')


def write_msg(user_id):
    alll = vk.method('messages.search', {'peer_id': user_id, 'q': '.', 'count': 1})['items'][0]['text']
    return alll


while True:
    time.sleep(4)
    g = vk.method('messages.getConversations', {'filter': 'unread'})
    if len(g['items']) == 0:
        continue
    g = g['items'][0]['conversation']['peer']['id']
    message = write_msg(g)
    if message == 'Е':
        break
    elif message.lower() == 'валюты':
        vk.method('messages.send', {'user_id': g, 'message': 'Какие? (EUR/USD)', 'random_id': int(time.time())})
    elif message.lower() in '(eur/usd)':
        slovo = message.upper()
        r = requests.get('https://www.banki.ru/products/currency/cash/moskva/')
        r = r.text.split('\n')
        r = list(filter(lambda x: '<td class="currency-table__large-text color-turquoise">' in x or slovo in x or '<div class="currency-table__large-text">' in x,
                        r))
        check = False
        for i in range(len(r)):
            if r[i] == '				<td class="currency-table__large-text color-turquoise">':
                if slovo in r[i + 1]:
                    b = r[i + 2]
                    b = b.split('<div class="currency-table__large-text">')
                    b = b[1][:-6]
                    vk.method('messages.send',
                              {'user_id': g, 'message': str(b), 'random_id': int(time.time())})
