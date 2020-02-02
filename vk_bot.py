import time
import vk_api
import requests

Z = {
    'Mon': {
        '1': ['Информатика', '310'],
        '2': ['Физика', '207'],
        '3': ['Литература', '119'],
        '4': ['Биология', '215']},
    'Tue': {
        '1': ['Физра', 'Сами знаете где'],
        '2': ['Инглиш', '211'],
        '3': ['Геометрия', '317'],
        '4': ['ППВ', 'свалишь, получишь']},
    'Wed': {
        '1': ['Информатика', '310'],
        '2': ['География', '215'],
        '3': ['Литература', '119'],
        '4': ['Алгебра', '317']},
    'Thu': {
        '1': ['Физика', '410'],
        '2': ['Химия', '316'],
        '3': ['Информатика', '310'],
        '4': ['История', '108']},
    'Fri': {
        '1': ['Общага', '108'],
        '2': ['Лекция', '208'],
        '3': ['Алгебра', '317'],
        '4': ['Русский', '117']},
    'Sat': {
        '1': ['Информатика', '310'],
        '2': ['Информатика', '310'],
        '3': ['Информатика', '310']},
    'Sun': {
        '1': ['Отдыхай уже', 'Бро'],
        '2': ['Лекция', '208'],
        '3': ['Алгебра', '317'],
        '4': ['Русский', '117']}
}
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
    elif message.lower() == 'расписание':
        day = time.strftime('%a', time.localtime())
        hour = int(time.strftime('%H', time.localtime()))
        minu = int(time.strftime('%M', time.localtime()))
        print(day, hour, minu)
        if hour * 60 + minu <= 620:
            go = '1'
        elif hour * 60 + minu <= 720:
            go = '2'
        elif hour * 60 + minu <= 840:
            go = '3'
        elif hour * 60 + minu <= 940:
            go = '4'
        elif hour * 60 + minu <= 1440:
            go = '1'
        urok, cab = Z[day][go]
        vk.method('messages.send', {'user_id': g, 'message': urok, 'random_id': int(time.time())})
        time.sleep(1)
        vk.method('messages.send', {'user_id': g, 'message': cab, 'random_id': int(time.time())})
