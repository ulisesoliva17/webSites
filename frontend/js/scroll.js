// Usamos Intersection Observer para detectar cuándo los elementos entran en pantalla
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        // Si el elemento entra en la pantalla, le agregamos la clase 'visible'
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
});

// Seleccionamos todos los elementos que queremos animar al hacer scroll
const hiddenElements = document.querySelectorAll('.animate-on-scroll');

// Le decimos al observer que vigile cada uno de esos elementos
hiddenElements.forEach((el) => observer.observe(el));