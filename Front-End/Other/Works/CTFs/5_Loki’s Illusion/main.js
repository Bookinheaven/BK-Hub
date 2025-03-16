console.log("Loki: 'You really thought I’d make it that easy?'");
console.log("One of these flags is the key... but which one?");
console.log("Hint: Look beyond what you see!");

let flags = [
    "01001000 01100101 01101000 01100101 00100000 01100110 01101111 01101111 01101100", //binary
    "486120466F6F6C656420416761696E3F3F", // Hex encoded
    "{MC_CTF:Illusions_Never_End}",
    "e01DX0NURjpJbGx1c2lvbl9QZXJzaXN0c18yMDE4fQ==", // Base64 encoded
    "{MC_CTF:Mischief_Managed}"
];

console.log("Possible flags:");
flags.forEach((flag, index) => {
    console.log(`${flag}`);
});

console.log("Loki: 'If you're reading this, you're close... but the truth is hidden in the illusion.'");
console.log("Hint: Some things need to be transformed to be understood... I Don't care anymore");
