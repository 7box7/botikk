from datetime import datetime, timedelta
from time import time, sleep
import vk_api
import os
import json
import base64
import requests
from random import randint
from table import sSettt
import IDDD
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from importlib import reload


answers = ['Те че надо, дядь(теть)', 'Может чем-нить полезным займешься?', 'Иди поспи', 'Слова нормальные подбери', 'отправь точку, если че надо']
tok = str(os.environ.get('VK_KEY'))
passw = str(os.environ.get('PASSGIT'))
username = str(os.environ.get('USERR'))
vk = vk_api.VkApi(token=tok)
keyboard = VkKeyboard(one_time=False)
keyboard.add_button('Урок', color=VkKeyboardColor.DEFAULT)
keyboard.add_button('День', color=VkKeyboardColor.DEFAULT)
keyboard.add_button('Завтра', color=VkKeyboardColor.DEFAULT)
count = 0


def write_msg(user_id):
    alll = vk.method('messages.search', {'peer_id': user_id, 'q': '.', 'count': 1})['items'][0]['text']
    return alll


def register(i, bukva, group):
    myfile = requests.get('https://api.github.com/repos/7box7/botikk/contents/IDDD.py', auth=(username, passw))
    f = base64.b64decode(myfile.json()['content'])
    f = f.decode('utf-8')
    f = f[:len(f) - 12] + '\n' + '            %s: [\'%s\', %s],' % (i, bukva, group) + '\n' + '        }'
    g = str(f).encode('utf-8')
    g64 = base64.b64encode(g)
    g64str = g64.decode('utf-8')
    z = requests.get('https://api.github.com/repos/7box7/botikk/contents/IDDD.py',
                     auth=(username, passw))
    f = {
        'message': 'sorry',
        'sha': z.json()['sha']
    }
    z = requests.delete('https://api.github.com/repos/7box7/botikk/contents/IDDD.py',
                        auth=(username, passw),
                        data=json.dumps(f))
    f = {
        'path': '',
        'message': 'Create new file via GitHub API',
        'content': g64str
    }
    requests.put('https://api.github.com/repos/7box7/botikk/contents/IDDD.py',
                 auth=(username, passw),
                 headers={"Content-Type": "application/json"},
                 data=json.dumps(f))


while True:
    T = sSettt()
    I = IDDD.iddd()
    sleep(0.5)
    g = vk.method('messages.getConversations', {'filter': 'unread'})
    if len(g['items']) == 0:
        continue
    z = g
    z = z['items'][0]['conversation']['last_message_id']
    g = g['items'][0]['conversation']['peer']['id']
    n = 0
    if '/reg' in write_msg(g).lower() and len(write_msg(g)) == 4 and g not in I.iD.keys():
        vk.method('messages.send', {'user_id': g, 'message': 'Напиши свой класс и группу в формате: /reg-класс-цифра',
                                    'random_id': int(time())})
        continue
    elif '/reg' in write_msg(g).lower() and len(write_msg(g)) > 4 and g not in I.iD.keys():
            fuf = write_msg(g).split('-')
            if fuf[1] not in ['Z', 'E', 'J']:
                vk.method('messages.send',
                          {'user_id': g, 'message': 'Чел, неправильно написал букву класса или ещё что(/reg-Z-1)',
                           'random_id': int(time())})
            else:
                register(g, fuf[1], fuf[2])
                vk.method('messages.send', {'user_id': g, 'message': 'Готово, подожди 2 минуты', 'random_id': int(time())})
                reload(IDDD)
            continue
    if g not in I.iD.keys():
        vk.method('messages.send',
                  {'user_id': g, 'message': 'Чел, тебя нет в списке, сориии', 'random_id': int(time())})
        vk.method('messages.send', {'user_id': 393598407, 'message': str(g), 'random_id': int(time())})
        continue
    message = write_msg(g)
    if message.lower() == '':
        vk.method('messages.markAsRead', {'peer_id': g, "start_message_id": z, 'random_id': int(time())})
        continue
    if message.lower() == 'валюты':
        vk.method('messages.send', {'user_id': g, 'message': 'Какие? (EUR/USD)', 'random_id': int(time())})
    elif message.lower() in '(eur/usd)':
        slovo = message.upper()
        r = requests.get('https://www.banki.ru/products/currency/cash/moskva/')
        r = r.text.split('\n')
        r = list(filter(lambda x: '<td class="currency-table__large-text color-turquoise">' in x or slovo in x or '<div class="currency-table__large-text">' in x, r))
        for i in range(len(r)):
            if r[i] == '				<td class="currency-table__large-text color-turquoise">':
                if slovo in r[i + 1]:
                    b = r[i + 2]
                    b = b.split('<div class="currency-table__large-text">')
                    b = b[1][:-6]
                    vk.method('messages.send',
                              {'user_id': g, 'message': str(b), 'random_id': int(time())})
    elif message.lower() == 'гуревич':
        vk.method('messages.send', {'user_id': g, 'message': 'Чмо' + '&#128522;', 'random_id': int(time())})
    elif message.lower() == 'солнце' and g in (324831486, 393598407):
        vk.method('messages.send', {'user_id': g, 'message': 'Твое' + '&#10084;', 'random_id': int(time())})
    elif message.lower() == 'урок':
        date = datetime.now() + timedelta(hours=3)
        day = date.strftime('%a')
        hour = int(date.strftime('%H'))
        minu = int(date.strftime('%M'))
        if hour * 60 + minu < 620:
            go = '1'
        elif hour * 60 + minu < 710:
            go = '2'
        elif hour * 60 + minu < 830:
            go = '3'
        elif hour * 60 + minu < 930:
            go = '4'
        else:
            go = '5'
        urok, cab = T.classes[n][I.iD[g][0]][I.iD[g][1]][day][go]
        answer = urok + ': ' + cab
        vk.method('messages.send', {'user_id': g, 'message': answer, 'random_id': int(time())})
    elif message.lower() == 'завтра':
        date = datetime.now() + timedelta(hours=27)
        day = date.strftime('%a')
        hour = int(date.strftime('%H'))
        vk.method('messages.send',
                      {'user_id': g, 'message': ': '.join(T.classes[n][I.iD[g][0]][I.iD[g][1]][day]['1']) + '\n'
                                                + ': '.join(T.classes[n][I.iD[g][0]][I.iD[g][1]][day]['2']) + '\n'
                                                + ': '.join(T.classes[n][I.iD[g][0]][I.iD[g][1]][day]['3']) + '\n'
                                                + ': '.join(T.classes[n][I.iD[g][0]][I.iD[g][1]][day]['4']) + '\n',
                       'random_id': int(time())})
    elif message.lower() == 'день':
        date = datetime.now() + timedelta(hours=3)
        day = date.strftime('%a')
        hour = int(date.strftime('%H'))
        vk.method('messages.send', {'user_id': g, 'message': ': '.join(T.classes[n][I.iD[g][0]][I.iD[g][1]][day]['1']) + '\n'
                                                            + ': '.join(T.classes[n][I.iD[g][0]][I.iD[g][1]][day]['2']) + '\n'
                                                            + ': '.join(T.classes[n][I.iD[g][0]][I.iD[g][1]][day]['3']) + '\n'
                                                            + ': '.join(T.classes[n][I.iD[g][0]][I.iD[g][1]][day]['4']) + '\n', 'random_id': int(time())})
    elif message.lower() == 'илья':
        check = randint(1, 5)
        a = vk.method("photos.getMessagesUploadServer")
        if check == 1:
            b = requests.post(a['upload_url'], files={'photo': open('file1.jpg', 'rb')}).json()
        elif check == 2:
            b = requests.post(a['upload_url'], files={'photo': open('file2.jpg', 'rb')}).json()
        elif check == 3:
            b = requests.post(a['upload_url'], files={'photo': open('file3.jpg', 'rb')}).json()
        elif check == 4:
            b = requests.post(a['upload_url'], files={'photo': open('file4.jpg', 'rb')}).json()
        elif check == 5:
            b = requests.post(a['upload_url'], files={'photo': open('file5.jpg', 'rb')}).json()
        c = vk.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
        att = "photo{}_{}".format(c["owner_id"], c["id"])
        vk.method('messages.send', {'user_id': g, "attachment": att, 'random_id': int(time())})
    elif message.lower() == 'пи18' and count == 4:
        vk.method('messages.send', {'user_id': g, 'message': 'пиздец ты некультурный', 'random_id': int(time())})
        count = 0
    elif message.lower() == 'пи':
        if count == 0:
            vk.method('messages.send', {'user_id': g, 'message': '3.14', 'random_id': int(time())})
            count += 1
        elif count == 1:
            vk.method('messages.send', {'user_id': g, 'message': '3.14...', 'random_id': int(time())})
            count += 1
        elif count == 2:
            vk.method('messages.send', {'user_id': g, 'message': '.....3.14..........', 'random_id': int(time())})
            count += 1
        elif count == 3:
            vk.method('messages.send', {'user_id': g, 'message': 'пи..14', 'random_id': int(time())})
            count += 1
        elif count == 4:
            vk.method('messages.send', {'user_id': g, 'message': 'пи..сец ты некультурный', 'random_id': int(time())})
            count = 0
    elif message.lower() == '.':
        vk.method('messages.send',
                  {'user_id': g, 'message': 'Для всех команд отправь /help', 'keyboard': keyboard.get_keyboard(),
                   'random_id': int(time())})
    elif message.lower() == '/help':
        vk.method('messages.send', {'user_id': g, 'message': 'Команды:' + '\n'
                                                             '------' + 'Гуревич' + '------' + '\n'
                                                             '------' + 'Урок' + '------' + '\n'
                                                             '------' + 'День' + '------' + '\n'
                                                             '------' + 'Завтра' + '------' + '\n'
                                                             '------' + 'Валюты' + '------', 'random_id': int(time())})
    else:
        vk.method('messages.markAsRead', {'peer_id': g, "start_message_id": z, 'random_id': int(time())})
        vk.method('messages.send', {'user_id': g, "message": answers[randint(0, len(answers)) - 1], 'random_id': int(time())})
