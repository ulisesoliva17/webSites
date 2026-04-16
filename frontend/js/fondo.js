const contenedorFondo = document.getElementById('fondo-grilla');

// Podés cambiar este número para hacer los cuadraditos más grandes o más chicos
const tamañoCuadrado = 50; 

function crearGrilla() {
    // Limpiamos el contenedor por si la pantalla cambió de tamaño
    contenedorFondo.innerHTML = ''; 

    // Calculamos cuántos cuadrados entran a lo ancho y a lo alto
    const columnas = Math.floor(window.innerWidth / tamañoCuadrado) + 1;
    const filas = Math.floor(window.innerHeight / tamañoCuadrado) + 1;
    const totalCuadrados = columnas * filas;

    // Generamos los cuadrados y los metemos en el HTML
    for (let i = 0; i < totalCuadrados; i++) {
        const cuadrado = document.createElement('div');
        cuadrado.classList.add('cuadradito');
        cuadrado.style.width = `${tamañoCuadrado}px`;
        cuadrado.style.height = `${tamañoCuadrado}px`;
        contenedorFondo.appendChild(cuadrado);
    }
}

// Ejecutamos la función al cargar la página
crearGrilla();

// Si el usuario achica o agranda la ventana, recalculamos la grilla
window.addEventListener('resize', crearGrilla);