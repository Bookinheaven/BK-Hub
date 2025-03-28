function downloadImage() {
    const link = document.createElement('a');
    link.href = 'trickshot_l3.png';
    link.download = 'trickshot_l3.png';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

document.addEventListener('DOMContentLoaded', () => {
    const terminal = document.getElementById("terminal");

    fetch("hawkeye_log.txt")
        .then(response => response.text())
        .then(data => {
            terminal.innerHTML = ""; 
            const lines = data.split("\n"); 

            lines.forEach(line => {
                const logLine = document.createElement("p");
                logLine.classList.add("log");
                logLine.textContent = line;
                terminal.appendChild(logLine);
            });
        })
        .catch(error => {
            terminal.innerText = "Error loading log file.";
            console.error("Error:", error);
        });
});