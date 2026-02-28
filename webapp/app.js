const tg = window.Telegram.WebApp;

const user = tg.initDataUnsafe.user;

const API="https://aikie.vercel.app";


async function generateImage(){

let prompt=prompt("prompt");

let res=await fetch(API+"/generate-image",{

method:"POST",

headers:{'Content-Type':'application/json'},

body:JSON.stringify({

user_id:user.id,

prompt:prompt

})

});

let data=await res.json();

alert(data.url);

}


async function generateVideo(){

let prompt=prompt("prompt");

let res=await fetch(API+"/generate-video",{

method:"POST",

headers:{'Content-Type':'application/json'},

body:JSON.stringify({

user_id:user.id,

prompt:prompt

})

});

let data=await res.json();

alert(data.url);

}


function openProfile(){

window.location="profile.html"

}


function openHistory(){

window.location="history.html"

}