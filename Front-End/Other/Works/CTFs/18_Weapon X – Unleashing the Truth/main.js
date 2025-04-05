document.addEventListener("DOMContentLoaded", function () {
    let description = document.getElementById("description");
    let text = "Access Restricted. Only authorized personnel may proceed.";
    let index = 0;

    function typeWriter() {
        if (index < text.length) {
            description.innerHTML += text.charAt(index);
            index++;
            setTimeout(typeWriter, 50);
        }
    }

    setTimeout(typeWriter, 2000);

    document.getElementById("download-image").addEventListener("click", function () {
        document.getElementById("access-box_id").classList.remove("hidden");

        let link = document.createElement("a");
        link.href = "wolverine.jpg";
        link.download = "wolverine.jpg";
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        document.getElementById("download-image").style.opacity = 0;
    });

    document.getElementById(atob("dmVyaWZ5QnRu")).addEventListener("click", function () {
        let x = document.getElementById(atob("YWNjZXNzQ29kZQ==")).value.trim().replace(/\s+/g, '');

        function f(d) {
            let a = document.createElement(atob("YQ=="));
            a.href = d;
            a.download = d;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        }

        let c1 = atob("U28uLi5UaGlzSXNXaGF0SXRGZWVsc0xpa2Uu");
        let c2 = atob("bG9va2ZsYWdz");
        if (x == c1) {
            f(atob("bG9nYW5fa25vd3NfcGFpbi56aXA="));
            f(atob("YS5vdXQ="));
        } else if (x == c2) {
            f(atob("bGF5ZXIyLnR4dA=="));
        } else {
            console.log(atob("QWNjZXNzIERlbmllZCE="));
        }
    });


});
