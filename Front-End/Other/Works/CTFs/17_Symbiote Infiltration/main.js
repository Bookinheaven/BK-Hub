document.getElementById("revealBtn").addEventListener("click", function() {
    document.getElementById("downloadSection").classList.remove("hidden");
    this.style.display = "none"; 
});

document.addEventListener("visibilitychange", function () {
    if (!document.hidden) {
        showTauntMessage();
    }
});

let tauntActive = false; 
function showTauntMessage() {
    if (tauntActive) return; 
    tauntActive = true;

    const taunts = [
        "Hey, do you really think I’d give it to you that easily?",
        "Oh wow, base64? That’s cute.",
        "You’re still here? I’m impressed… and disappointed.",
        "Decrypting, huh? Well, let’s see how deep you can go.",
        "Maybe just give up. This isn’t for you.",
        "You must love wasting time.",
        "I bet you thought this would be easy.",
        "Keep going, I love watching people struggle.",
        "The flag is near… or maybe not.",
        "HAHA, you thought that was the last step?",
        "You're almost there… just kidding.",
        "Even Venom would have quit by now.",
        "I wonder if you’ll ever see the light at the end of the tunnel.",
        "You’re decoding this? Wow, what a genius.",
        "Maybe try again tomorrow… or never.",
        "LOL, you really fell for that?",
        "Come on, you can do better than this.",
        "Oh look, another layer. Who could have seen that coming?",
        "You’re about 0.00001% closer to the flag.",
        "Go ahead, decode this one. I dare you.",
        "Your suffering amuses me.",
        "Keep going, I need entertainment.",
        "Maybe there’s a flag… maybe not.",
        "Decrypt, decrypt, decrypt… does it ever end?",
        "This is fun, isn’t it?",
        "You could be outside enjoying life, but no… you’re here.",
        "I’m sure you’re getting tired… or are you just getting started?",
        "You’re closer than before, but still far away.",
        "Oh wow, you actually made it this far?",
        "You must really want this flag.",
        "How many layers? Who knows?",
        "Your persistence is… concerning.",
        "Wow, you’re still here? I admire the stubbornness.",
        "You should have quit three layers ago.",
        "The flag? Oh, I lost it somewhere.",
        "Decrypting this? Good luck, you'll need it.",
        "Only real challengers make it past this point.",
        "Oops, looks like another layer.",
        "Wouldn’t it be funny if this was all a joke?",
        "The flag is waiting… but not for you.",
        "Don’t stop now, I’m having fun.",
        "Imagine if the flag was just ‘try_harder’.",
        "Your sanity must be hanging by a thread.",
        "If you give up now, no one will judge you.",
        "Okay, maybe I’ll give you the flag… after 20 more layers.",
        "How deep does the rabbit hole go?",
        "Base64 again? I expected something harder.",
        "Still decoding? Yikes.",
        "You think you’re close? That’s cute.",
        "Venom is watching. And laughing.",
        "Oh no, not another one… oh wait, yes, another one.",
        "Decrypt, rinse, repeat.",
        "Your patience is being tested.",
        "Just when you thought it was over…",
        "You got past the last one? Let’s see about this one.",
        "Almost there? Not even close.",
        "Imagine if you made a mistake and had to start over.",
        "Go ahead, try it, see what happens.",
        "I hope you have enough coffee for this.",
        "Venom is impressed… or maybe just amused.",
        "You really think I’d make it that simple?",
        "Look at you, wasting your time.",
        "This isn’t over until I say it’s over.",
        "Still decoding? Must be painful.",
        "I can’t believe you’re still going.",
        "You’ve come so far… but it’s not enough.",
        "Do you even know what you’re doing?",
        "One more step? No, fifty more.",
        "I have made it harder, I guess",
        "Base64? Please.",
        "Keep digging, maybe you’ll find a flag.",
        "This challenge isn’t for the weak.",
        "You must be stubborn.",
        "What if the flag isn’t even here?",
        "Decrypting again? Haven’t you learned?",
        "So close, yet so far.",
        "How many more layers can you handle?",
        "I bet you’re regretting this.",
        "Wouldn’t it be funny if I just told you the flag now?",
        "Oh, you thought that was the last one? LOL.",
        "You’ll need a break after this.",
        "Still here? You’re stronger than I thought.",
        "I hope you brought snacks.",
        "I could do this all day.",
        "No, seriously, how are you still going?",
        "Maybe you’re the real symbiote here.",
        "Look at you, decrypting like a pro.",
        "Willpower alone won’t get you through this.",
        "You must really love puzzles.",
        "Hurry up, I’m getting bored.",
        "Okay fine, just five more layers… or ten.",
        "The flag is near. Or is it?",
        "Still not tired? Impressive.",
        "One day, you’ll look back at this and laugh.",
        "Would Venom have solved this faster?",
        "At this point, you deserve a trophy.",
        "Keep pushing, you’re almost suffering enough.",
        "You didn’t come this far just to quit, right?",
        "Okay, this is the last one… just kidding.",
        "Fine. You win. But was it worth it?"
    ];
    const randomTaunt = taunts[Math.floor(Math.random() * taunts.length)];
    const tauntBox = document.getElementById("tauntBox");
    tauntBox.innerText = randomTaunt;
    tauntBox.classList.add("show");
    setTimeout(() => {
        tauntBox.classList.remove("show");
        tauntActive = false;
    }, 5000);
}

function generatePassword(length = 9) {
    const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:',.<>?/`~";
    return Array.from({ length }, () => characters[Math.floor(Math.random() * characters.length)]).join('');
}

function encryptBase64(text, rounds = 3) {
    let encoded = text;
    for (let i = 0; i < rounds; i++) {
        encoded = btoa(encoded);
    }
    return encoded;
}

function generatePasswordsFile() {
    let passwords = Array.from({ length: 99 }, generatePassword);
    passwords.push(atob("Y2hvY29sYXRl")); 
    passwords.sort(() => Math.random() - 0.5);
    const encryptedPasswords = passwords.map(pw => encryptBase64(pw));
    const blob = new Blob([encryptedPasswords.join("\n")], { type: "text/plain" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "passwords.txt";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
document.getElementById("passwordGen").addEventListener("click", generatePasswordsFile);
