document.addEventListener("DOMContentLoaded", function() {
    const messageElement = document.getElementById("wakandanMessage");
    const text = messageElement.innerText;
    messageElement.innerText = "";
    let index = 0;

    function typeEffect() {
        if (index < text.length) {
            messageElement.innerHTML += text[index];
            index++;
            setTimeout(typeEffect, Math.random() * 20 + 10);
        }
    }

    typeEffect();
});
