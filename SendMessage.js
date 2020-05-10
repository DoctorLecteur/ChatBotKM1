/**
create date: 09/05/2020
desc: Функция получает текст сообщения, который отпраляется на веб-сервис
**/

function sendMessage()
{
    var sMessageValue = document.getElementById("comment").value;
    var sUserName = document.getElementById("username").value;

    if (sMessageValue)
    {
        doHttpRequest(sMessageValue, sUserName);
        sMessageValue = "";
        sUserName = "";
        document.getElementById("comment").value = "";
        document.getElementById("username").value = "";
    }
    else
        alert("Заполните текст сообщения");
}

/**
create date: 09/05/2020
@param sTextMessage - текст сообщения
@param sUserName - имя пользователя
desc: Функция отправляет сообщение на веб-сервис
**/

function doHttpRequest(sTextMessage, sUserName)
{
    var request = new XMLHttpRequest();
    var url = "http://localhost:8080/send";

    var formData = new FormData();
    formData.append("user", sUserName);
    formData.append("text", sTextMessage);

    request.open("POST", url, true);
    request.send(formData);
}