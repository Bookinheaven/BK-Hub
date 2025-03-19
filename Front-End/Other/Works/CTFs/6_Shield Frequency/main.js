console.log("⚠️ S.H.I.E.L.D. Secure Frequency Activated.");
console.log("🔍 Intercepted Transmission Detected...");

let transmissionData = "- .-. .. ... -.- . .-.. .. --- -. ..-. .- .-.. .-.. ..--- ----- .---- ....-";
let fasd = "7B4D435F4354463A4B4545505F4D4F5253455F434F44455F484552457D"; //hex 
let d113 = "{MC_CTF:Access_Denied_403}";
let gs1 = "{MC_CTF:SHIELD_Protocol}"; 

function typeWriterEffect(elementId, text, speed) {
    let i = 0;
    function type() {
        if (i < text.length) {
            document.getElementById(elementId).innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    type();
}

document.addEventListener("DOMContentLoaded", function () {
    typeWriterEffect("encryptedMessage", "\n- .-. .. ... -.- . .-.. .. --- -. ..-. .- .-.. .-.. ..--- ----- .---- ....-", 50);
});

console.log(d113);
console.log(gs1);
console.log("🔒 This transmission is classified...");
console.log("🔓 Decryption Protocol Initiated...");
