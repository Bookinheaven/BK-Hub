document.addEventListener("DOMContentLoaded", function() {
    let hiddenButton = document.getElementById("hidden-btn");

    document.body.addEventListener("mousemove", function(event) {
        if (event.clientY > window.innerHeight - 90 && event.clientX > window.innerWidth - 90) {
            hiddenButton.style.opacity = "1";
        }
        else {
            hiddenButton.style.opacity = "0";   
        }
    });
});

function revealFlag() {
    let flag = document.getElementById("flag");
    flag.style.display = "block";

    setTimeout(function() {
        flag.style.display = "none";
    }, 10000);
}
