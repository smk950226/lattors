
var slideIndex = 1;

function plusIndex(n) {
    showImage(slideIndex += n);
}

function currentSlide(n) {
    showImage(slideIndex = n);
}

function showImage(n){
    var slide = document.getElementsByClassName("slide");
    var dots = document.getElementsByClassName("dots");
    
    if (n > slide.length) {
        slideIndex = 1;
    };
    if (n < 1) {
        slideIndex = slide.length;
    };

    for (var i = 0; i < slide.length ; i++) {
        slide[i].style.display = "none";
    };
    slide[slideIndex-1].style.display = "block";

    for (var i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active","");
    }

    dots[slideIndex-1].className += " active";
};

function autoSlide() {
    var i;
    var slide = document.getElementsByClassName("slide");
    var dots = document.getElementsByClassName("dots");

    if (slideIndex > slide.length) {
        slideIndex = 1;
    };
    if (slideIndex < 1) {
        slideIndex = slide.length;
    };
    for (i = 0; i < slide.length ; i++) {
        slide[i].style.display = "none";
    };
    slide[slideIndex-1].style.display = "block";
    for (var i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active","");
    }

    dots[slideIndex-1].className += " active";
    slideIndex++;
    
    setTimeout(autoSlide,5000);
};

