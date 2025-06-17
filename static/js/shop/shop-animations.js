// shop-animations.js - JavaScript-driven animations to complement shop-animations.css

function initializeAnimations() {
    // Animate product cards on scroll
    const productCards = document.querySelectorAll('.product-card');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.5s ease forwards';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.2 });

    productCards.forEach(card => observer.observe(card));

    // Smooth filter toggle animation
    const filterItems = document.querySelectorAll('.filter-item');
    filterItems.forEach(item => {
        item.addEventListener('click', () => {
            item.style.transition = 'transform 0.2s ease';
            item.style.transform = 'scale(1.05)';
            setTimeout(() => {
                item.style.transform = 'scale(1)';
            }, 200);
        });
    });

    // Color circle click animation
    const colorCircles = document.querySelectorAll('.color-circle');
    colorCircles.forEach(circle => {
        circle.addEventListener('click', () => {
            circle.style.transition = 'transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
            circle.style.transform = 'scale(1.3)';
            setTimeout(() => {
                circle.style.transform = circle.classList.contains('active') ? 'scale(1.1)' : 'scale(1)';
            }, 200);
        });
    });
}