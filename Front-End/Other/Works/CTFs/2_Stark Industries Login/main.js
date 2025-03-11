document.addEventListener("DOMContentLoaded", function() {
    const sdfhasdfljasdf = "V2FyTWFjaGluZTY4";
    const asjdfasdfasdf = "V0FSTUFDSElORVJPWA==";
    
    function sendErrorMessage() {
        let errm = document.getElementById("error-message")
        errm.style.display = "block";  
        setTimeout(function () {
            errm.style.display = "none";  
        }, 4000)
    }
    function attemptLogin() {
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        if (btoa(username) === sdfhasdfljasdf &&
        btoa(password) === asjdfasdfasdf) {
            document.getElementById("firewall").style.display = "none";  
            document.getElementById("flag").style.display = "block";   
            document.getElementsByClassName("sys-message")[0].style.display = "none";  
            document.getElementById("ffaaf").innerText = "ZTAxRFgwTlVSanBKY205dVgweGxaMkZqZVY5TllYSnJYMWhNU1VsOQ==";
        } else {
            sendErrorMessage()
        }
    }
    document.getElementById("password").addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            attemptLogin();
        }
    });

    window.attemptLogin = attemptLogin;
});

document.getElementById("togglePassword").addEventListener("click", function() {
    let passwordField = document.getElementById("password");
    if (passwordField.type === "password") {
        passwordField.type = "text";
        this.textContent = "🔒";
    } else {
        passwordField.type = "password";
        this.textContent = "👁️";
    }
});

// base64