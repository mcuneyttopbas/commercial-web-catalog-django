var swiper = new Swiper(".variantSlider", {
    slidesPerView: 3,
    spaceBetween: 10,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        "@0.00": {
            slidesPerView: 4,
            spaceBetween: 15,
        },
        "576": {
            slidesPerView: 4,
            spaceBetween: 20,
        },
        "768": {
            slidesPerView: 4,
            spaceBetween: 20,
        },
        "992": {
            slidesPerView: 4,
            spaceBetween: 20,
        },
        "1200": {
            slidesPerView: 4,
            spaceBetween: 20,
        },
        "1400": {
            slidesPerView: 5,
            spaceBetween: 20,
        },
    },
});