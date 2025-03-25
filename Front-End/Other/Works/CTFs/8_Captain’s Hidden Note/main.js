
document.getElementById("downloadBtn").addEventListener("click", function () {
    document.getElementById("downloadBtn").style.display = "none";
    document.getElementById("inputContainer").classList.remove("hidden");
    const link = document.createElement("a");
    link.href = "captains_note.txt"; 
    link.download = "captains_note.txt";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
});

document.getElementById("submitBtn").addEventListener("click", function () {
    const gdsfg = document.getElementById("finalWord").value.trim();
    const dsfg46hw = "SSB3aWxsIGFsd2F5cyBiZSB3aXRoIHlvdSwgUGVnZ3ku";

    if (btoa(gdsfg) === dsfg46hw) {
        document.getElementById("aads-Fd").classList.remove("hidden");
        document.getElementById("aads-Fd").innerText = atob("e01DX0NURjpBdmVuZ2Vyc0Fzc2VtYmxlfQ==")
    } else {
        alert("Wrong answer! Try again.");
    }
});
