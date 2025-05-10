// static/javascript/home.js

document.addEventListener('DOMContentLoaded', function() {
    // Slider functionality
    const slides = document.querySelectorAll('.slide');
    const dots = document.querySelectorAll('.dot');
    let currentSlide = 0;
    const slideInterval = 3000; // 5 seconds
    
    function showSlide(index) {
        slides.forEach(slide => slide.classList.remove('active'));
        dots.forEach(dot => dot.classList.remove('active'));
        
        slides[index].classList.add('active');
        dots[index].classList.add('active');
        currentSlide = index;
    }
    
    function nextSlide() {
        let nextIndex = (currentSlide + 1) % slides.length;
        showSlide(nextIndex);
    }
    
    // Set up automatic sliding
    let slideTimer = setInterval(nextSlide, slideInterval);
    
    // Pause on hover
    const slider = document.querySelector('.slider');
    slider.addEventListener('mouseenter', () => clearInterval(slideTimer));
    slider.addEventListener('mouseleave', () => {
        slideTimer = setInterval(nextSlide, slideInterval);
    });
    
    // Dot navigation
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            clearInterval(slideTimer);
            showSlide(index);
            slideTimer = setInterval(nextSlide, slideInterval);
        });
    });
    
    // Header scroll effect
    const header = document.querySelector('header');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            header.classList.add('header-scrolled');
        } else {
            header.classList.remove('header-scrolled');
        }
    });
    
    // Initialize first slide
    showSlide(0);
});