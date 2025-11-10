    document.addEventListener('DOMContentLoaded', function () {
        const searchInput = document.getElementById('search-input');
        const projectCards = document.querySelectorAll('.project-card');

        searchInput.addEventListener('keyup', function () {
            const searchTerm = searchInput.value.toLowerCase();

            projectCards.forEach(card => {
                const title = card.querySelector('.project-title').textContent.toLowerCase();
                const author = card.querySelector('p:nth-of-type(1)').textContent.toLowerCase();
                const tutor = card.querySelector('p:nth-of-type(2)').textContent.toLowerCase();
                const keywords = card.querySelector('p:nth-of-type(4)').textContent.toLowerCase(); // Palabras clave

                if (
                    title.includes(searchTerm) ||
                    author.includes(searchTerm) ||
                    tutor.includes(searchTerm) ||
                    keywords.includes(searchTerm)
                ) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
