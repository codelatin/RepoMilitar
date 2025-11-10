document.addEventListener('DOMContentLoaded', () => {
    // Selecciona el botón del menú hamburguesa y el menú de navegación
    const menuToggle = document.getElementById('menu-toggle');
    const navMenu = document.querySelector('.nav-menu');

    // Añade un evento 'click' al botón del menú
    menuToggle.addEventListener('click', () => {
        // Alterna la clase 'active' en el menú de navegación para mostrarlo/ocultarlo
        navMenu.classList.toggle('active');
        
        // Alterna la clase 'active' en el botón para animarlo a una 'X'
        menuToggle.classList.toggle('active');
    });

    // Opcional: Cierra el menú si se hace clic en un enlace (solo en móvil)
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            // Verifica si el menú está activo (visible)
            if (navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                menuToggle.classList.remove('active');
            }
        });
    });
});