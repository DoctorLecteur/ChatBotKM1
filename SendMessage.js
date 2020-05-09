/**
create date: 09/05/2020
desc: Функция получает текст сообщения, который отпраляется на веб-сервис
**/
function sendMessage()
{
    var sMessageValue = document.getElementById("comment").value;
    if (sMessageValue)
        alert(sMessageValue);
    else
        alert("Заполните текст");
}