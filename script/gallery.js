function showGallery(folderName) {
    var galleryContainer = document.querySelector('.gallery');
    galleryContainer.innerHTML = ''; // Vorherige Bilder entfernen

    var folderPath = '../gallery/' + folderName + 'hasd/';

    // Ordnerinhalt abrufen
    fetch(folderPath)
        .then(response => response.text())
        .then(data => {
            // Bilder extrahieren
            var imageRegex = /<img[^>]+src="?([^"\s]+)"?\s*\/>/g;
            var matches;
            var imageUrls = [];

            while (matches = imageRegex.exec(data)) {
                imageUrls.push(matches[1]);
            }

            // Bildergalerie erstellen
            imageUrls.forEach(function (url) {
                var image = new Image();
                image.src = folderPath + url;
                galleryContainer.appendChild(image);
            });
        })
        .catch(error => console.error(error));
}
