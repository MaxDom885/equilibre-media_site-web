// Animation des compteurs - Version corrigée
function initCounters() {
    const counterElements = document.querySelectorAll('.counter-value'); // Utilisez la bonne classe
    const animationDuration = 2000; // Durée totale en ms
    let animationStarted = false;

    function animateCounter(counter) {
        const target = +counter.getAttribute('data-target');
        const prefix = counter.getAttribute('data-prefix') || '';
        const suffix = counter.getAttribute('data-suffix') || '';
        let startTimestamp = null;

        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / animationDuration, 1);
            const currentValue = Math.floor(progress * target);
            counter.textContent = prefix + currentValue + suffix;
            
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };

        window.requestAnimationFrame(step);
    }

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !animationStarted) {
                animationStarted = true;
                counterElements.forEach(counter => {
                    animateCounter(counter);
                });
                observer.disconnect();
            }
        });
    }, { 
        threshold: 0.5,
        rootMargin: '0px 0px -100px 0px' // Déclenche un peu avant d'arriver à la section
    });

    const statsSection = document.querySelector('.bg-cobalt');
    if (statsSection) {
        observer.observe(statsSection);
    }
}

// Initialisation
document.addEventListener('DOMContentLoaded', function() {
    initCounters();
    
    // Initialisation du slider (si nécessaire)
    if (document.querySelector('.partner-swiper')) {
        new Swiper('.partner-swiper', {
            loop: true,
            autoplay: {
                delay: 2500,
                disableOnInteraction: false,
            },
            breakpoints: {
                640: { slidesPerView: 2 },
                768: { slidesPerView: 3 },
                1024: { slidesPerView: 4 }
            }
        });
    }
});