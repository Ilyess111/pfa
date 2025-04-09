let currentIndex = 0;
const slides = document.querySelectorAll(".slide");
const indicators = document.querySelectorAll(".indicator");

function showSlide(index) {
    slides.forEach((slide, i) => {
        slide.classList.remove("active");
        indicators[i].classList.remove("active");
        if (i === index) {
            slide.classList.add("active");
            indicators[i].classList.add("active");
        }
    });
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
    showSlide(currentIndex);
}

function prevSlide() {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    showSlide(currentIndex);
}

// Click on dots to navigate
indicators.forEach((dot, i) => {
    dot.addEventListener("click", () => {
        currentIndex = i;
        showSlide(currentIndex);
    });
});

// Auto-slide every 3 seconds
setInterval(nextSlide, 3000);