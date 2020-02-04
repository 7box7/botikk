import time
import vk_api
import requests
from table import sSettt
from IDDD import iddd

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
vk = vk_api.VkApi(token='7d977d1ac381b8deabb8ef0969ebf9188c8b0be1e16941fc3fdc3496d06f5903c6ad53b3fb87c628b7f8d')


def write_msg(user_id):
    alll = vk.method('messages.search', {'peer_id': user_id, 'q': '.', 'count': 1})['items'][0]['text']
    return alll


while True:
    T = sSettt()
    I = iddd()
    time.sleep(2)
    g = vk.method('messages.getConversations', {'filter': 'unread'})
    if len(g['items']) == 0:
        continue
    g = g['items'][0]['conversation']['peer']['id']
    message = write_msg(g)
    if message.lower() == 'валюты':
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
    elif message.lower() == 'гуревич':
        vk.method('messages.send', {'user_id': g, 'message': 'Чмо' + '&#128522;', 'random_id': int(time.time())})
    elif message.lower() == 'урок':
        if g not in I.iD.keys():
            vk.method('messages.send', {'user_id': g, 'message': 'Чел, тебя нет в списке, сориии', 'random_id': int(time.time())})
            continue
        day = time.strftime('%a', time.localtime())
        hour = int(time.strftime('%H', time.localtime()))
        hour += 2
        if hour >= 24:
            hour = hour - 24
            if day == days[-1]:
                day = 'Mon'
            else:
                day = days[days.index(day) + 1]
        minu = int(time.strftime('%M', time.localtime()))
        if hour * 60 + minu <= 620:
            go = '1'
        elif hour * 60 + minu <= 720:
            go = '2'
        elif hour * 60 + minu <= 840:
            go = '3'
        elif hour * 60 + minu <= 940:
            go = '4'
        elif hour * 60 + minu <= 1440:
            go = '5'
        urok, cab = T.classes[I.iD[g][0]][I.iD[g][1]][day][go]
        vk.method('messages.send', {'user_id': g, 'message': urok, 'random_id': int(time.time())})
        time.sleep(0.5)
        vk.method('messages.send', {'user_id': g, 'message': cab, 'random_id': int(time.time())})
    elif message.lower() == 'день':
        if g not in I.iD.keys():
            vk.method('messages.send', {'user_id': g, 'message': 'Чел, тебя нет в списке, сориии', 'random_id': int(time.time())})
            continue
        day = time.strftime('%a', time.localtime())
        hour = int(time.strftime('%H', time.localtime()))
        hour += 2
        if hour >= 24:
            hour = hour - 24
            if day == days[-1]:
                day = 'Mon'
            else:
                day = days[days.index(day) + 1]
        vk.method('messages.send', {'user_id': g, 'message': ': '.join(T.classes[I.iD[g][0]][I.iD[g][1]][day]['1']) + '\n'
                                                            + ': '.join(T.classes[I.iD[g][0]][I.iD[g][1]][day]['2']) + '\n'
                                                            + ': '.join(T.classes[I.iD[g][0]][I.iD[g][1]][day]['3']) + '\n'
                                                            + ': '.join(T.classes[I.iD[g][0]][I.iD[g][1]][day]['4']) + '\n', 'random_id': int(time.time())})
    elif message.lower() == '/help':
        vk.method('messages.send', {'user_id': g, 'message': 'Команды:' + '\n'
                                                             '------' + 'Гуревич' + '\n'
                                                             '------' + 'Урок' + '\n'
                                                             '------' + 'День' + '\n'
                                                             '------' + 'Валюты', 'random_id': int(time.time())})
