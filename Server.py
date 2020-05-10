# -*- coding: utf-8 -*-
import json
import DBConnect

import requests
from bottle import get, request, run, route

TOKEN = 'access_token'

'''
create date: 10/05/2020
desc: Функция отпрааляет сообщение в чат
'''
@route('/send', method='POST')
def sendMessage():
    sUserName = request.POST.get('user')
    sTextMessage = request.POST.get('text')

    nUserId = getUserForMessage(sUserName)
    dictMessage = {
         "text": str(sTextMessage)
    }

    headers = {'content-type': 'application/json'}
    jsonMessage = json.dumps(dictMessage)
    print(jsonMessage)
    urlSendMessage = 'https://botapi.tamtam.chat/messages?access_token=' + TOKEN + "&user_id=" + str(nUserId)

    bIsSend = False
    while (bIsSend == False):
        response = requests.post(urlSendMessage, headers=headers, data=jsonMessage, verify=False)
        sSender = getInfoBot()
        nSenderId = sSender["user_id"]
        sSenderName = sSender["username"]
        nStatusCode = response.status_code
        responseJson = response.json()
        DBConnect.doInsertRecord(sSenderName, sUserName, str(sTextMessage), json.dumps(dictMessage, ensure_ascii=False), nStatusCode, responseJson, nSenderId, nUserId)

        if (nStatusCode == 200):
            bIsSend = True

'''
create date: 09/05/2020
desc: Функция возвращает информацию о боте
'''
@get('/InfoBot')
def getInfoBot():
    res = requests.get('https://botapi.tamtam.chat/me?access_token=' + TOKEN)
    return res.json()

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

'''
create date: 09/05/2020
desc: Функция возращает user_id указано контакта
'''

@get('/UserForMessage/<sUserName>')
def getUserForMessage(sUserName):
    aChats = json.loads(getChatsInfo())
    aUsersActive = getActiveChatsUsers(aChats)

    for i in range(0, len(aUsersActive), 1):
        if (aUsersActive[i]["name"] == sUserName):
            return aUsersActive[i]["user_id"]


run(host='localhost', port=8080, debug=True)