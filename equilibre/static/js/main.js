// Animation des compteurs - Version améliorée
function initCounters() {
    const counterElements = document.querySelectorAll('[data-target]');
    let animationStarted = false;

    function animateCounter(counter) {
        const target = +counter.dataset.target;
        const prefix = counter.dataset.prefix || '';
        const suffix = counter.dataset.suffix || '';
        const duration = 2000; // 2 secondes
        const startValue = 0;
        const startTime = Date.now();

        const updateCounter = () => {
            const currentTime = Date.now();
            const elapsedTime = currentTime - startTime;
            const progress = Math.min(elapsedTime / duration, 1);
            
            const currentValue = Math.floor(progress * (target - startValue) + startValue);
            counter.textContent = prefix + currentValue + suffix;
            
            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            }
        };

        requestAnimationFrame(updateCounter);
    }

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !animationStarted) {
                animationStarted = true;
                counterElements.forEach(counter => {
                    animateCounter(counter);
                });
            }
        });
    }, {
        threshold: 0.5,
        rootMargin: '0px 0px -50px 0px'
    });

    if (counterElements.length > 0) {
        counterElements.forEach(counter => {
            observer.observe(counter);
        });
    }
}

// Initialisation du carousel des partenaires
function initPartnersCarousel() {
    const partnersCarousel = document.getElementById('partnersCarousel');
    if (partnersCarousel) {
        new bootstrap.Carousel(partnersCarousel, {
            interval: 3000,
            wrap: true
        });
    }
}

// Initialisation globale
document.addEventListener('DOMContentLoaded', function() {
    initCounters();
    initPartnersCarousel();
    
    // Initialisation des carousels Bootstrap
    const carousels = document.querySelectorAll('.carousel');
    carousels.forEach(carousel => {
        new bootstrap.Carousel(carousel);
    });
});

// Partenaires Carousel - Auto Play
document.addEventListener('DOMContentLoaded', function() {
    const partnersCarousel = new bootstrap.Carousel('#partnersCarousel', {
        interval: 3000,  // Rotation toutes les 3 secondes
        wrap: true,
        pause: false
    });
});