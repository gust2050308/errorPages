// Data arrays - using hardcoded paths since Django template tags don't work in .js files
const imagenes = [
    "/static/img/1.png",
    "/static/img/2.png",
    "/static/img/3.png",
    "/static/img/4.png",
    "/static/img/5.png",
    "/static/img/6.png",
    "/static/img/7.png",
    "/static/img/8.png",
    "/static/img/9.png",
    "/static/img/10.png",
];

const titulos = [
    "Desarrollo Web", "Inteligencia Artificial", "Base de Datos",
    "Redes Cisco", "Seguridad Informática", "Diseño UX/UI",
    "Cloud Computing", "Internet de las Cosas", "Big Data", "DevOps"
];

const descripciones = [
    "Aprende las últimas tecnologías del mercado.",
    "El futuro de la tecnología está aquí.",
    "Gestiona grandes volúmenes de información.",
    "Conecta el mundo a través de redes seguras.",
    "Protege la integridad de la información.",
    "Mejora la experiencia del usuario final.",
    "Servicios escalables en la nube.",
    "Conectando dispositivos cotidianos a internet.",
    "Análisis de datos para toma de decisiones.",
    "Integración continua y entrega continua."
];

const carrerasContainer = document.getElementById('carreras');
let isLoading = false;
let hasReachedBottom = false;
const Container = document.getElementById('carrerasContainer');

const cargarCarreras = () => {
    if (!carrerasContainer) return;

    for (let i = 0; i < 4; i++) {
        let numberRandom = Math.floor(Math.random() * imagenes.length);

        const carrera = document.createElement('div');
        carrera.classList.add('col-md-4', 'mb-3');
        carrera.innerHTML = `
            <div class="card">
                <img src="${imagenes[numberRandom]}" class="card-img-top" alt="${titulos[numberRandom]}">
                <div class="card-body">
                    <h5 class="card-title">${titulos[numberRandom]}</h5>
                    <p class="card-text">${descripciones[numberRandom]}</p>
                </div>
            </div>
        `;
        carrerasContainer.appendChild(carrera);
    }
};

document.addEventListener('DOMContentLoaded', () => {
    cargarCarreras();
});

window.addEventListener('scroll', () => {
    // Si ya está cargando, no hacer nada
    if (isLoading) return;

    const scrollHeight = document.documentElement.scrollHeight;
    const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    const clientHeight = document.documentElement.clientHeight;

    const scrollPercentage = (scrollTop + clientHeight) / scrollHeight;

    // Cuando llegue al 90% de scroll, comenzar a cargar más
    if (scrollPercentage > 0.90) {
        // Marcar como cargando para evitar múltiples llamadas
        isLoading = true;

        // Mostrar el spinner de carga
        Container.insertAdjacentHTML('beforeend', `
            <div class="col-12 text-center my-4" id="loading-spinner">
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24">
                    <path fill="currentColor" d="M12 2A10 10 0 1 0 22 12A10 10 0 0 0 12 2Zm0 18a8 8 0 1 1 8-8A8 8 0 0 1 12 20Z" opacity="0.5"/>
                    <path fill="currentColor" d="M20 12h2A10 10 0 0 0 12 2V4A8 8 0 0 1 20 12Z">
                        <animateTransform attributeName="transform" dur="1s" from="0 12 12" repeatCount="indefinite" to="360 12 12" type="rotate"/>
                    </path>
                </svg>
                <p class="mt-2">Cargando más carreras...</p>
            </div>
        `);

        // Esperar 700ms y luego agregar más carreras
        setTimeout(() => {
            cargarCarreras(); // Esto agrega (appendChild) las nuevas carreras a las existentes

            // Remover el spinner después de cargar
            const spinner = document.getElementById('loading-spinner');
            if (spinner) {
                spinner.remove();
            }

            // IMPORTANTE: Resetear isLoading después de completar
            // Esto permite cargar más cuando vuelvas a hacer scroll
            isLoading = false;
        }, 700);
    }
});