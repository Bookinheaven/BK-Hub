const normalizeName = (name) => {
    return name.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
};
function sendWarning(message) {
    document.getElementById("warning-message").style.display = "block";
    document.getElementById("warning-message-content").innerText = message;
    setTimeout(() => {
        document.getElementById("warning-message").classList.add("slide-out");
    }, 4000);
}
function sendError(message) {
    document.getElementById("error-message").style.display = "block";
    document.getElementById("error-message-content").innerText = message;
    setTimeout(() => {
        document.getElementById("error-message").classList.add("slide-out");
    }, 4000);
}
export {sendWarning,sendError, normalizeName}