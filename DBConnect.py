import psycopg2
import datetime
import json
from psycopg2 import sql

conn = psycopg2.connect(dbname='postgres', user='postgres',
                        password='12345', host='localhost')

def doInsertRecord(sSender, sRecipient, sTextMessage, jsonQuery, responseCode, responseJson, nSenderId, nUserId):
    with conn.cursor() as cursor:
        conn.autocommit = True
        values = [
            (datetime.datetime.today(), sSender, sRecipient, sTextMessage, jsonQuery, responseCode, json.dumps(responseJson, ensure_ascii=False), nSenderId, nUserId)
        ]

        insert = sql.SQL('INSERT INTO historylogmessage (datetime, sender, recipient, textmessage, jsonquery, responsecode, responsejson, sender_user_id, recipient_user_id) VALUES {}').format(
            sql.SQL(',').join(map(sql.Literal, values))
        )

        cursor.execute(insert)

    cursor.close()
    conn.close()

