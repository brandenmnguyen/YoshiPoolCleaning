const http=require("http");
const express=require("express");
const path = require('path');


const app=express();

const server=http.createServer(app);
const port=process.env.PORT || 3000;

app.use(express.static(path.join(__dirname, '..')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '..', 'templates', 'messaging.html'));
});


/*----------------------------------------------------------Socket.io setup---------------------------------------------------------*/

const io=require("socket.io")(server);
var users={};

io.on("connection",(socket)=>{
 socket.on("new-user-joined",(username)=>{
    users[socket.id]=username;
    socket.broadcast.emit('user-connected',username);
    io.emit("users-list", users);
 });

 socket.on("disconnect",()=>{
    socket.broadcast.emit('user-disconnected',user=users[socket.id]);
    delete users[socket.id];
    io.emit("users-list", users);
 })
 socket.on('message', (data)=>{
    socket.broadcast.emit("message", {user: data.user, msg: data.msg});
});
});



/*--------------------------------------------------------Socket.io setup ends-------------------------------------------------------*/
server.listen(port,()=>{
    console.log("Server started at "+port);
});