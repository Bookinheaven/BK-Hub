document.addEventListener("DOMContentLoaded", function () {
    console.log("The truth is in the words... or is it?");
    console.log("Maybe you should check the text for hidden characters? 🤔");
    console.log("Sometimes, images hold more than meets the eye. Ever heard of metadata?");

    let isDownloaded = false; 

    document.getElementById("download-btn").addEventListener("click", function () {
        if (isDownloaded) return;
        isDownloaded = true;

        fetch("0291.jpg", { cache: "no-store" })
            .then(response => {
                if (!response.ok) throw new Error("Failed to fetch image");
                return response.blob();
            })
            .then(blob => {
                let link = document.createElement("a");
                let url = URL.createObjectURL(blob);
                link.href = url;
                link.download = "truth.jpg";
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                URL.revokeObjectURL(url);
            })
            .catch(error => console.error("Error downloading the image:", error));
    });
});
