# coding: utf8;
from bottle import get, post, request, run
import requests
import json


TOKEN = 'access_token'

@get('/text/<sTextMessage>')
def showText(sTextMessage):
    return sTextMessage


@post('/send')
def sendMessage():
    print(request)

'''
create date: 09/05/2020
desc: Функция возвращает информацию о боте
'''
@get('/InfoBot')
def getInfoBot():
    res = requests.get('https://botapi.tamtam.chat/me?access_token=' + TOKEN)
    return res

'''
create date: 09/05/2020
desc: Функция возращает чаты в которых участвует бот
'''
@get('/ChatsInfo')
def getChatsInfo():
    res = requests.get('https://botapi.tamtam.chat/chats?access_token=' + TOKEN)
    response = res.json()
    chats = response["chats"]

    return json.dumps(chats)

'''
create date: 09/05/2020
desc: Функция возращает активные чаты в которых участвует бот
'''

def getActiveChatsUsers(aChats):

    aChatsActive = []
    for i in range(0, len(aChats), 1):
        if (aChats[i]["status"] == 'active'):
            aChatsActive.append(aChats[i]["dialog_with_user"])
    return aChatsActive

@get('/UserForMessage/<sUserName>')
def getUserForMessgae(sUserName):
    aChats = json.loads(getChatsInfo())
    aUsersActive = getActiveChatsUsers(aChats)

    for i in range(0, len(aUsersActive), 1):
        if (aUsersActive[i]["name"] == sUserName):
            return str(aUsersActive[i]["user_id"])


run(host='localhost', port=8080, debug=True)