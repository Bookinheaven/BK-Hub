let enteredPin = "";
const correctPin = "29051970"; 
const pinDisplay = document.getElementById("pin-display");
const message = document.getElementById("message");
const hintBox = document.getElementById("hint-box");

function enterDigit(digit) {
    if (enteredPin.length < 8) {
        enteredPin += digit;
        updateDisplay();
    }
}

function clearPin() {
    enteredPin = "";
    updateDisplay();
}

function updateDisplay() {
    let dots = "🔒 ";
    for (let i = 0; i < 8; i++) {
        dots += i < enteredPin.length ? "● " : "○ ";
    }
    pinDisplay.innerHTML = dots;
}

function checkPin() {
    if (enteredPin === correctPin) {
        message.innerHTML = "Access Granted! <br>Flag: <b>{MC_CTF:Sys01_Log_12_A}</b>";
        message.style.color = "#ffffff";
    } else {
        message.innerHTML = "Access Denied!";
        message.style.color = "red";        
        let container = document.querySelector(".container");
        container.classList.add("shake");
        setTimeout(() => container.classList.remove("shake"), 300);
        setTimeout(() => message.innerHTML = "", 1800);
        
        clearPin();
    }
}

function showHint() {
    hintBox.classList.remove("hidden");
    setTimeout(() => {
        hintBox.classList.add("hidden");
    }, 3000)
}
