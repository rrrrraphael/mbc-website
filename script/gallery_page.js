document.addEventListener('DOMContentLoaded', function() {
    var images = document.querySelectorAll('.gallery-image');
    var overlay = document.getElementById('overlay');
    var imageViewer = document.getElementById('imageViewer');
    var imageViewedImg = document.getElementById('imageViewedImg');
    var currentIndex = 0;

    images.forEach(function(image, index) {
        image.addEventListener('click', function() {
            currentIndex = index;
            showSlide(currentIndex);
            overlay.style.display = 'block';
            imageViewer.style.display = 'flex';
        });
    });

    function showSlide(index) {
        if (index >= images.length) {
            currentIndex = 0;
        } else if (index < 0) {
            currentIndex = images.length - 1;
        } else {
            currentIndex = index;
        }
        var src = images[currentIndex].getAttribute('src');
        imageViewedImg.setAttribute('src', src);
    }

    window.plusSlides = function(n) {
        showSlide(currentIndex + n);
    };

    window.closeImageViewer = function() {
        overlay.style.display = 'none';
        imageViewer.style.display = 'none';
    };
});