document.addEventListener('DOMContentLoaded', () => {

    // 1. Intersection Observer para animaciones .animate-on-scroll
    const observerOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Dejar de observar luego de la primera vez
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const elementsToAnimate = document.querySelectorAll('.animate-on-scroll');
    elementsToAnimate.forEach(el => observer.observe(el));


    // 2. Parallax Hover disruptivo en el SVG (Nódulo en Hero)
    const nodeContainer = document.getElementById('node-container');
    const heroRight = document.querySelector('.hero-right');

    if (nodeContainer && heroRight) {
        heroRight.addEventListener('mousemove', (e) => {
            const rect = heroRight.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            // Centro
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            // Inversión en hover (20 deg)
            const rotateX = ((y - centerY) / centerY) * -20;
            const rotateY = ((x - centerX) / centerX) * 20;

            nodeContainer.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.08, 1.08, 1.08)`;
        });

        heroRight.addEventListener('mouseleave', () => {
            nodeContainer.style.transform = `perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)`;
            nodeContainer.style.transition = "transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94)";
        });
        
        heroRight.addEventListener('mouseenter', () => {
            nodeContainer.style.transition = "none";
        });
    }


    // 3. Efecto de luz dinámico en las tarjetas de la grilla asimétrica (Grid CSS Custom Properties)
    const gridCards = document.querySelectorAll('.grid-card');
    
    gridCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            // Se actualizan las props de --mouse-x y --mouse-y en el hover de css
            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);
        });
    });


    // 4. Smooth Scrolling de los anchors (polyfill por las dudas)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if(targetId === '#') return;
            const targetElement = document.querySelector(targetId);
            if(targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

});
