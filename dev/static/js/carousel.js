$(document).ready(function() {
    $('.single-item').slick({
        dots: false,
        infinite: true,
        speed: 1000,
        autoplaySpeed: 3000,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        arrows: false,
        fade: true,
        cssEase: 'linear',
        pauseOnHover: false
    });
});