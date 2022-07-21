var swiper = new Swiper(".newsSwiper", {
    slidesPerView: 2,
    spaceBetween: 20,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    breakpoints: {
        "@0.00": {
        slidesPerView: 2,
        spaceBetween: 15,
        },
        "576": {
        slidesPerView: 2,
        spaceBetween: 20,
        },
        "768": {
        slidesPerView: 2,
        spaceBetween: 20,
        },
        "992": {
        slidesPerView: 3,
        spaceBetween: 20,
        },
        "1200": {
        slidesPerView: 4,
        spaceBetween: 20,
        },
    }
  });