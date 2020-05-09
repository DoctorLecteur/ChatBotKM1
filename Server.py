from bottle import get, post, request, run

@get('/text/<sTextMessage>')
def showText(sTextMessage):
    return sTextMessage


run(host='localhost', port=8080, debug=True)