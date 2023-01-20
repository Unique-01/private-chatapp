const userName = JSON.parse(document.getElementById('username').textContent);
const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/' + userName + '/');
const timeNow = JSON.parse(document.getElementById('time-now').textContent);
var dateOptions = { hour: 'numeric', minute: 'numeric', hour12: true }

chatSocket.onopen = function (e) {
    console.log("Websocket connection has been created successfully")
    var span = document.getElementById('status')
    span.innerHTML = "Connected"
}

chatSocket.onclose = function (e) {
    console.log("Websocket connection has been disconnected")
    var span = document.getElementById('status')
    span.innerHTML = "Disconnected"
}

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    var hello = document.createElement('div')
    var timestamp = new Date(data.timestamp).toLocaleString('en', dateOptions)
    hello.innerHTML = '<p>' + data.message + '<br>' + '<small>' + timestamp.toLowerCase() + '</small>' + '</p>'
    document.getElementById('message-input').value = "";
    document.getElementById('message-div').appendChild(hello)
}

document.getElementById('message-input').focus();
document.getElementById('message-input').onkeyup = function (e) {
    if (e.keyCode == 13) {
        document.getElementById('send-message').click();
    }
}

document.getElementById('send-message').onclick = function (e) {
    var messageInput = document.getElementById('message-input').value;
    chatSocket.send(JSON.stringify({ message: messageInput, timestamp: timeNow }))
}
