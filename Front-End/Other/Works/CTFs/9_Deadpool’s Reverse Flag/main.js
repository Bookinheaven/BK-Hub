let _xZq9 = Math.floor(Math.random() * 50) + 10; 

let __a1B = ((_xZq9 * 4) + 12) / 2; 
let _$f9Z = (_xZq9 * 7) + 133; 

// document.getElementById("equation").innerHTML = `( (x * 4) + 12 ) / 2 = ${__a1B}`;
// document.getElementById("flagHint").innerHTML = `Flag Format: <strong>MC_CTF{x * 7 + 133}</strong>`;

document.getElementById("submitBtn").addEventListener("click", function () {
    const _H1lO = document.getElementById("answerInput").value.trim();
    if (parseInt(_H1lO) === _$f9Z) {
        // document.getElementById("flagMessage").innerText = `🎉 Flag: MC_CTF{${"Deadpool" + _$f9Z}} 🎉`;
        document.getElementById("flagMessage").innerText = `${atob("RmxhZzogTUNfQ1RG")}{${"Deadpool_" + "Q2hpbWljaGFuZ2E="}}<br>Still you have to find proper flag from it `;
        document.getElementById("flagMessage").classList.remove("hidden");
    } else {
        alert("❌ Wrong answer! Deadpool says try again.");
    }
});

document.getElementById("download").addEventListener('click', () => {
    document.getElementById("inputContainer").classList.remove("hidden");

    let __XyT = `( (x * 4) + 12 ) / 2 = ${__a1B}\nans = (x * 7) + 133`;
    const _LQ92 = new Blob([__XyT], { type: "text/plain" });
    const _N2mA = document.createElement("a");
    _N2mA.href = URL.createObjectURL(_LQ92);
    _N2mA.download = "deadpool_math.txt";

    document.body.appendChild(_N2mA);
    _N2mA.click();
    document.body.removeChild(_N2mA);
});
