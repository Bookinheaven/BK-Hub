document.getElementById("download-btn").addEventListener("click", () => {
    function f(d) {
        let a = document.createElement(atob("YQ=="));
        a.href = d;
        a.download = d;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    }
    f(atob("RFVtcC50YXIuZ3o="));

})