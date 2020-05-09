/**
create date: 09/05/2020
desc: Функция получает текст сообщения, который отпраляется на веб-сервис
**/

function sendMessage()
{
    var sMessageValue = document.getElementById("comment").value;
    if (sMessageValue)
    {
        alert(sMessageValue);
        doHttpRequest(sMessageValue);
        sMessageValue = "";
        document.getElementById("comment").value = "";
    }
    else
        alert("Заполните текст сообщения");
}

/**
create date: 09/05/2020
@param sTextMessage - текст сообщения
desc: Функция отправляет сообщение на веб-сервис
**/

function doHttpRequest(sTextMessage)
{
    var xhr = new XMLHttpRequest();
    var sBody = sTextMessage;
    xhr.open("GET", "http://localhost:8080/text/" + sBody);
    xhr.send();
}