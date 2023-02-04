const userName = JSON.parse(document.getElementById('username').textContent);
const requestUser = JSON.parse(document.getElementById('request-username').textContent);
const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/' + userName + '/');
const timeNow = JSON.parse(document.getElementById('time-now').textContent);
var dateOptions = { hour: 'numeric', minute: 'numeric', hour12: true }

window.onload = function (e) {
    // scroll(0, 3000)
    scrollBy(0, 3000)
}
chatSocket.onopen = function (e) {
    console.log("Websocket connection has been created successfully")
    var span = document.getElementById('status')
    span.classList.add('text-success')
    span.innerHTML = "Connected"
}

chatSocket.onclose = function (e) {
    console.log("Websocket connection has been disconnected")
    var span = document.getElementById('status')
    span.classList.add('text-danger')
    span.innerHTML = "Disconnected"
}

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    // 
    // create div to display incoming data
    var senderMessage = document.createElement('div')
    var receiverMessage = document.createElement('div')
    // 
    // add css attributes to the created div 
    senderMessage.classList.add('d-flex', 'justify-content-end')
    receiverMessage.classList.add('d-flex', 'justify-content-start')
    // 
    // Convert django datetime to js date
    var timestamp = new Date(data.timestamp).toLocaleString('en', dateOptions);
    // 
    // clear the input box
    document.getElementById('message-input').value = "";
    // 
    // validate the dic to be display
    if (requestUser == data.username) {
        senderMessage.innerHTML = '<p class="bg-success px-2 py-1 cust-rounded">' + '<span>' + data.message + '</span>' + '<br/>' + '<small class="d-flex justify-content-end">' + timestamp.toLowerCase() + '.' + '</small>' + '</p>';
        document.getElementById('message-div').appendChild(senderMessage)
    } else {
        receiverMessage.innerHTML = '<p class="bg cust-rounded px-2 py-1">' + '<span>' + data.message + '</span>' + '<br/>' + '<small>' + timestamp.toLowerCase() + '.' + '</small>' + '</p>';
        document.getElementById('message-div').appendChild(receiverMessage)
    }
    // window.scroll(0, 3000000000000)
    window.scrollBy(0, 3000)

}

document.getElementById('message-input').focus();
document.getElementById('message-input').onkeyup = function (e) {
    if (e.keyCode == 13) {
        document.getElementById('send-message').click();
    }
}

document.getElementById('send-message').onclick = function (e) {
    var messageInput = document.getElementById('message-input').value;
    chatSocket.send(JSON.stringify({ username: requestUser, message: messageInput, timestamp: timeNow }))
}
