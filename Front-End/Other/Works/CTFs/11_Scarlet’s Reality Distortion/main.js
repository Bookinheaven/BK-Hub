function downloadImage() {
    const link = document.createElement('a');
    link.href = 'wanda_reality_hidden.png';
    link.download = 'wanda_reality_hidden.png';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
