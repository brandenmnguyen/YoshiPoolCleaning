const socket=io();

var username;

var chats=document.querySelector(".chats");

var users_List=document.querySelector(".users-list");

var users_count=document.querySelector(".users-count");
var user_send = document.querySelector("#user-send"); // For the send button
var user_msg = document.querySelector("#user-msg"); // For the message input


do{
    username=prompt("Enter your name");
}
while(!username);
/*-----it will be called when user has joined-----*/
socket.emit("new-user-joined", username);

/*-----notifying that the user has joined-------*/
socket.on('user-connected', (socket_name)=>{
    userJoinLeft(socket_name, 'joined');
});

/*----function to create join left status div-----*/
function userJoinLeft(name, status){
    let div=document.createElement("div");
    div.classList.add('user-join');
    let content=`<p><b>${name}</b> ${status} the chat</p>`;
    div.innerHTML=content;
    chats.appendChild(div);
    chats.scrollTop=chats.scrollHeight;
}

/*------notifying that the user has left-------*/
socket.on('user-disconnected', (user)=>{
    userJoinLeft(user,'left');
});

/*------for updating user list and user counts------*/
socket.on('users-list', (users)=>{
 users_List.innerHTML="";
 users_arr=Object.values(users);
 for(i=0; i<users_arr.length; i++)
 {
    let p=document.createElement('p');
    p.innerText=users_arr[i];
    users_List.appendChild(p);
 }

 users_count.innerHTML=users_arr.length;
});

/*-----for sending message--------*/
user_send.addEventListener('click', ()=>{
    console.log("Send button clicked"); // Test to see if this logs when the button is clicked
    let data = {
        user: username,
        msg: user_msg.value
    };
    if(user_msg.value!=''){
        appendMessage(data, 'outgoing');
        socket.emit('message', data);
        user_msg.value='';
    }
});


function appendMessage(data, status) {
    let div = document.createElement('div');
    div.classList.add('message', status);
    let content = `
    <h5> ${data.user}</h5>
    <p> ${data.msg}</p>
    `;
    div.innerHTML = content;
    chats.appendChild(div);
    chats.scrollTop = chats.scrollHeight;
}


socket.on('message',(data)=>{
    appendMessage(data, 'incoming');
});