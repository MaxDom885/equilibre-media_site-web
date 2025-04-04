// Initialisation contrôlée pour éviter les conflits
document.addEventListener('DOMContentLoaded', () => {
    // 1. Configuration du carousel Swiper
    const initServicesCarousel = () => {
        new Swiper('.services-carousel', {
            loop: true,
            slidesPerView: 1,
            spaceBetween: 30,
            speed: 800,
            autoplay: {
                delay: 5000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
                dynamicBullets: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            breakpoints: {
                640: { slidesPerView: 2 },
                1024: { 
                    slidesPerView: 3,
                    spaceBetween: 40,
                },
                1440: { 
                    slidesPerView: 4,
                    spaceBetween: 50,
                }
            },
            on: {
                init: function () {
                    this.slides.forEach(slide => {
                        slide.style.transition = 'opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1), transform 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
                    });
                },
            },
        });
    };

    // 2. Animations au défilement
    const animateOnScroll = () => {
        // Animation des éléments généraux
        const elements = document.querySelectorAll('.animate-on-scroll');
        const animationOptions = {
            threshold: 0.2,
            rootMargin: '0px 0px -20% 0px'
        };

        const generalObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                }
            });
        }, animationOptions);

        elements.forEach(element => generalObserver.observe(element));

        // Animation spécifique pour les images
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active-image');
                }
            });
        }, { threshold: 0.2 });

        document.querySelectorAll('.service-detail-page img:not(.service-header img)').forEach(img => {
            imageObserver.observe(img);
        });
    };

    // 3. Initialisation conditionnelle
    if (document.querySelector('.services-carousel')) {
        initServicesCarousel();
        animateOnScroll();
    }

    // 4. Optimisations des performances
    window.addEventListener('scroll', () => {
        requestAnimationFrame(animateOnScroll);
    }, { passive: true });
});

const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animationPlayState = 'running';
        }
    });
}, { threshold: 0.15 });

document.querySelectorAll('.animate-on-scroll').forEach(section => {
    section.style.animationPlayState = 'paused';
    sectionObserver.observe(section);
});