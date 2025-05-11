
document.addEventListener("DOMContentLoaded", function () {
    const offersPerPage = 6;
    const offersGrid = document.querySelector('.offers-grid');
    const sortSelect = document.querySelector('.sort-select');
    const paginationContainer = document.querySelector('.pagination');
    let offerCards = Array.from(document.querySelectorAll('.offer-card'));
    let currentPage = 1;

    function showPage(page) {
        const start = (page - 1) * offersPerPage;
        const end = start + offersPerPage;

        offerCards.forEach((card, index) => {
            card.style.display = index >= start && index < end ? 'block' : 'none';
        });
    }

    function renderPagination() {
        paginationContainer.innerHTML = '';

        const pageCount = Math.ceil(offerCards.length / offersPerPage);
        for (let i = 1; i <= pageCount; i++) {
            const btn = document.createElement('button');
            btn.textContent = i;
            btn.classList.add('page-btn');
            if (i === currentPage) btn.classList.add('active');

            btn.addEventListener('click', () => {
                currentPage = i;
                showPage(currentPage);
                renderPagination();
            });

            paginationContainer.appendChild(btn);
        }
    }

    function sortOffers(criteria) {
    offerCards.sort((a, b) => {
        const priceA = parseFloat(a.dataset.price);
        const priceB = parseFloat(b.dataset.price);
        const durationA = parseInt(a.dataset.duration);
        const durationB = parseInt(b.dataset.duration);

        if (criteria === 'price-low') {
            return priceA - priceB;
        } else if (criteria === 'price-high') {
            return priceB - priceA;
        } else if (criteria === 'duration') {
            return durationA - durationB;
        } else if (criteria === 'destination') {
            const destA = a.querySelector('.offer-meta span').textContent.toLowerCase();
            const destB = b.querySelector('.offer-meta span').textContent.toLowerCase();
            return destA.localeCompare(destB);
        }
    });

    offerCards.forEach(card => offersGrid.appendChild(card));
    currentPage = 1;
    showPage(currentPage);
    renderPagination();
}

    // Event listener for sorting
    sortSelect.addEventListener('change', (e) => {
        const value = e.target.value;
        let sortKey = '';
        if (value.includes('Price') && value.includes('Low')) sortKey = 'price-low';
        else if (value.includes('Price') && value.includes('High')) sortKey = 'price-high';
        else if (value.includes('Duration')) sortKey = 'duration';
        else if (value.includes('Destination')) sortKey = 'destination';

        sortOffers(sortKey);
    });
     sortSelect.addEventListener('change', (e) => {
    sortOffers(e.target.value);
});
    // Initial render
    showPage(currentPage);
    renderPagination();
    
});

