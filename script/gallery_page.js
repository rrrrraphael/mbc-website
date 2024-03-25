document.addEventListener('DOMContentLoaded', function() {
    var images = document.querySelectorAll('.gallery-image');
    var overlay = document.getElementById('overlay');
    var imageViewer = document.getElementById('imageViewer');
    var imageViewedImg = document.getElementById('imageViewedImg');

    images.forEach(function(image) {
        image.addEventListener('click', function() {
            var src = image.getAttribute('src');
            imageViewedImg.setAttribute('src', src);
            overlay.style.display = 'block';
            imageViewer.style.display = 'block';
        });
    });
});

function closeImageViewer() {
    var overlay = document.getElementById('overlay');
    var imageViewer = document.getElementById('imageViewer');
    overlay.style.display = 'none';
    imageViewer.style.display = 'none';
}
