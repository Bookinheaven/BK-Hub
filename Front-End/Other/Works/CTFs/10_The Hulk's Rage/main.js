let qZ9 = Math.floor(Math.random() * 10) + 201;
let pX3 = Math.floor(Math.random() * 50);
let mL7 = [];

for (let i = 0; i < 1000; i++) {
    mL7.push(Math.floor(Math.random() * 40) + 80);
}

mL7[pX3] = qZ9;

let tR2 = qZ9 - 200;
let kL4 = (tR2 * 5) + 42;

document.getElementById("download").addEventListener('click', () => {
    document.getElementById("inputContainer").classList.remove("hidden");
    document.getElementById("download").classList.add("hidden");

    let fileContent = mL7.join(" ") + `\n\nBruce: "One mistake could push me over the edge... \nFind it, then the difference of it with 200 should be multiplied with 5 and then add 42."`;

    const blob = new Blob([fileContent], { type: "text/plain" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "hulk_pulse.txt";

    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
});

document.getElementById("submitBtn").addEventListener("click", function () {
    const uI = document.getElementById("answerInput").value.trim();
    if (uI == Number(kL4) ){
        const aB5 = "WlRBeFJGZ3dUbFZTYW5CSlpGZDRjbGd3WkdoaVZ6Rm9XREZLYUZwSGJHaGtSMngyWW00d1BRPT0="; 
        document.getElementById("flagMessage").innerText = `Flag: ${atob(aB5)}`;
        document.getElementById("flagMessage").classList.remove("hidden");
    } else {
        alert("❌ Wrong answer! Bruce is still transforming! Try again.");
    }
});