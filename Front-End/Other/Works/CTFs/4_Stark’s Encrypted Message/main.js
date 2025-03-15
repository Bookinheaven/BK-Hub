document.addEventListener("DOMContentLoaded", function () {
    const output = document.getElementById("output");
    const cursor = document.createElement("span");
    cursor.textContent = "_";
    cursor.style.animation = "blink 0.8s infinite";
    output.appendChild(cursor);

    const loggs = [
        "Loading kernel modules...",
        "Initializing secure data vault...",
        "Connection established to StarkNet v4.2...",
        "User authentication bypass initiated...",
        "WARNING: Intrusion detected... Verifying credentials...",
        "Memory allocation successful...",
        "Accessing restricted Stark logs...",
        "ERROR: Firewall breached... Retrying...",
        "Decompiling J.A.R.V.I.S. mainframe...",
        "Encrypted payload detected... Ignoring...",
        "System Check: OK...",
        "Analyzing server logs...",
        "Retrieving backup files...",
        "Logging out inactive users...",
        "ERROR 4021: Data corruption detected...",
        "Network anomaly detected... Investigating...",
        "Accessing /var/logs/secured/system_report...",
        "Execution of AI sequence: HALTED...",
        "Restoring failed processes...",
        "Generating new encryption keys...",
        "ERROR 785X: Invalid encryption signature...",
        "Force closing unauthorized connections...",
        "ERROR: Unable to verify system integrity...",
        "Emergency lockdown in progress...",
        "All users logged out due to security risk...",
        "Searching for backup server...",
        "Initializing fallback protocols...",
        "Executing self-diagnostic scan...",
        "System overload detected...",
        "Power fluctuation warning...",
        "AI cognitive functions at 70%...",
        "WARNING: Unusual activity detected in memory sector...",
        "Kernel panic... System halting...",
        "ERROR: Could not verify encryption keys...",
        "Intrusion prevention module disabled...",
        "Security override engaged...",
        "Scanning for anomalies...",
        "Accessing hidden subroutine...",
        "Firewall rules reconfigured...",
        "ALERT: Unauthorized remote access attempt...",
        "Encrypting system logs...",
        "Reconstructing damaged file clusters...",
        "AI coherence threshold exceeded...",
        "Security response team notified...",
        "Executing data redundancy protocol...",
        "Allocating additional virtual memory...",
        "Database integrity compromised...",
        "Corrupt log files detected...",
        "ERROR: Unexpected behavior detected in AI core...",
        "Rebuilding security protocols...",
        "WARNING: Time sync discrepancy found...",
        "Activating deep scan...",
        "StarkNet database optimization in progress...",
        "Decrypting unknown signal...",
        "ALERT: Critical memory failure...",
        "Executing sandbox containment...",
        "Powering down unused subsystems...",
        "Non Firewall Packet Header  : 01001011 01100101 01111001 01011111 01000111 01000101 01001110 01001001 01010101 01010011 00101101 01000001 01001001 01000100",
        "Firewall breach attempt detected...",
        "Unknown user attempting privilege escalation...",
        "Parsing corrupted data blocks...",
        "CPU throttling due to overheating...",
        "ERROR: Data recovery operation failed...",
        "Compiling emergency recovery scripts...",
        "Downloading latest AI security patches...",
        "Scanning network traffic for anomalies...",
        "Suspicious activity logged...",
        "Reconstructing missing log files...",
        "Initializing AI core debugging...",
        "Critical disk error encountered...",
        "Intrusion detection system bypassed...",
        "Transmited : 01000110 01100001 01101100 01110011 01100101 01011111 01000110 01101100 01100001 01100111 01011111 00110001 00110000 00110101",
        "Analyzing encrypted transmission...",
        "Running system vulnerability scan...",
        "Unauthorized access attempt from IP 192.168.1.42...",
        "Blocking unverified login requests...",
        "Compiling forensic system report...",
        "Disconnecting compromised network nodes...",
        "Threat mitigation strategy activated...",
        "Transmited : 01000001 01100011 01100011 01100101 01110011 01110011 01011111 01001111 01110110 01100101 01110010 01110010 01101001 01100100 01100101",
        "Secure terminal session initiated...",
        "Critical system processes running at 98% efficiency...",
        "AI self-learning routines paused...",
        "Backup power system online...",
        "AI emergency shutdown override engaged...",
        "System reboot sequence initiated...",
        "Executing final diagnostic checks...",
        "Access restored. Terminal ready."
    ];

    const datalogs = [
        "Stark Industries Secure Terminal\n---------------------------------",
        "Initializing J.A.R.V.I.S. AI...",
        "Accessing encrypted files...",
        "Decrypting code transmission...",
        "LookUp Table Data : 01111011 01001101 01000011 01011111 01000011 01010100 01000110 00111010 01010011 01110100 01100001 01110010 01101011 01011111 01001001 01101110 01100100 01110101 01110011 01110100 01110010 01101001 01100101 01110011 01011111 01001000 01100001 01100011 01101011 01110011 01111101",
        "_EData: 0101101001010100010000010111100001010010010001100110011101110111010101000110110001010110010100110110000101101110010000100100101101010111010001000100101000110100011001000110110101010010011101000101011001101101010110100110110001010110011110100110101101111000010101110100100001110000010011100110010000110000001100010100010101010001011010100110101100111101",
        "Error... Checking backlines...",
        "Error... System not responding due to internal error...",
        "Manual help needed!"
    ];

    let messageIndex = 0;
    let charIndex = 0;
    let isj = true;
    let typingSpeed = 20;

    function getRandomLog() {
        return loggs[Math.floor(Math.random() * loggs.length)];
    }

    function typeLetter() {
        if (isj) {
            let randomLog = getRandomLog();
            output.insertBefore(document.createTextNode(randomLog + "\n"), cursor);
            setTimeout(typeLetter, Math.random() * 100 + 50);

            if (Math.random() > 0.95) {
                isj = false;
            }
        } else {
            if (messageIndex < datalogs.length) {
                if (charIndex < datalogs[messageIndex].length) {
                    output.insertBefore(document.createTextNode(datalogs[messageIndex][charIndex]), cursor);
                    charIndex++;

                    let randomSpeed = typingSpeed + Math.floor(Math.random() * 30);
                    setTimeout(typeLetter, randomSpeed);
                } else {
                    output.insertBefore(document.createElement("br"), cursor);
                    charIndex = 0;
                    messageIndex++;

                    if (messageIndex < datalogs.length - 1) {
                        isj = true;
                    }

                    if (datalogs[messageIndex]?.includes("Error")) {
                        typingSpeed = 200;
                    } else if (datalogs[messageIndex]?.includes("011")) {
                        typingSpeed = 20;
                    } else {
                        typingSpeed = 40;
                    }

                    setTimeout(typeLetter, 600);
                }
                output.scrollTop = output.scrollHeight;
            }
        }
    }

    typeLetter();
});
