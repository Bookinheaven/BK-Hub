document.addEventListener('DOMContentLoaded', function () {
    setTimeout(() => {
        document.getElementById('hint-section').classList.remove('hidden');
    }, 15000); 
});

function validateLogin() {
    const password = document.getElementById('password').value; //https://www.youtube.com/watch?v=OrKi8idPCSo
    if (password === atob("TGFzdFRpbWVJVHJ1c3RlZFNvbWVvbmVJTG9zdEFuRXll")) {
        document.getElementById('login-screen').classList.add('hidden');
        document.getElementById('terminal-screen').classList.remove('hidden');
        startTerminalLogs();
    } else {
        document.getElementById('error-msg').innerText = "ACCESS DENIED";
    }
}

function startTerminalLogs() {
    const terminal = document.getElementById('terminal-output');
    const logs = [
        "Connecting to SHIELD Intelligence Database...",
        "Verifying encryption protocols...",
        "Decrypting hidden directive...",
        "Retrieving classified document...",
        "Operation complete. Download the directive."
    ];

    let index = 0;
    function showLog() {
        if (index < logs.length) {
            let p = document.createElement("p");
            p.textContent = logs[index];
            terminal.appendChild(p);
            index++;
            setTimeout(showLog, 2000);
        }
    }
    showLog();
}

function downloadFile() {
    const link = document.createElement('a');
    link.href = 'directive.docx';
    link.download = 'directive.docx';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
