const tg = window.Telegram.WebApp;
const user = tg.initDataUnsafe.user;

function generateImage(){
    const prompt = prompt("Enter prompt");
    alert("Image generation requested: " + prompt);
}

function generateVideo(){
    const prompt = prompt("Enter prompt");
    alert("Video generation requested: " + prompt);
}

function openProfile(){
    window.location = "profile.html";
}

function openHistory(){
    window.location = "history.html";
}
