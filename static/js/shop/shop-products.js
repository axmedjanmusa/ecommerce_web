// shop-products.js - Manages product grid, sorting, and pagination

// Sample product data (in a real app, this would come from an API)
const products = [
    { id: 1, title: 'Наруто Сага Расенгана', price: 3990, originalPrice: 4990, stock: 'В наличии', rating: 4.5, reviews: 24, category: 'trending shoes', tags: ['аниме', 'кроссовки', 'наруто'], color: 'red', badges: ['new'] },
    { id: 2, title: 'Атака Титанов - Эрен', price: 2990, originalPrice: 4290, stock: 'В наличии', rating: 3.5, reviews: 18, category: 'new in', tags: ['аниме', 'кроссовки', 'атака титанов'], color: 'black', badges: ['sale'] },
    { id: 3, title: 'Токийский Гуль - Канеки', price: 3590, stock: 'В наличии', rating: 4, reviews: 12, category: 'popular', tags: ['аниме', 'кроссовки', 'токийский гуль'], color: 'white' },
    { id: 4, title: 'Ван Пис - Мугивара', price: 4290, originalPrice: 5590, stock: 'Мало в наличии', rating: 5, reviews: 35, category: 'trending shoes', tags: ['аниме', 'кроссовки', 'ван пис'], color: 'blue', badges: ['hot'] },
    { id: 5, title: 'Клинок, рассекающий демонов', price: 3890, stock: 'В наличии', rating: 4.5, reviews: 19, category: 'new in', tags: ['аниме', 'кроссовки', 'демон слеер'], color: 'green' },
    { id: 6, title: 'Моя геройская академия', price: 3490, stock: 'Нет в наличии', rating: 3.5, reviews: 9, category: 'sale & promo', tags: ['аниме', 'кроссовки'], color: 'red', badges: ['out'] }
];

function initializeProducts() {
    // Initial render
    updateProducts({});

    // Sorting
    const sortSelect = document.querySelector('.sort-select select');
    sortSelect.addEventListener('change', () => {
        const sortBy = sortSelect.value;
        updateProducts({ sortBy });
    });

    // Pagination
    const pageLinks = document.querySelectorAll('.page-link');
    pageLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            pageLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
            const page = link.textContent === '→' ? parseInt(document.querySelector('.page-link.active').textContent) + 1 : parseInt(link.textContent);
            updateProducts({ page });
        });
    });
}

function updateProducts(filters = {}) {
    let filteredProducts = [...products];

    // Apply filters
    if (filters.category) {
        filteredProducts = filteredProducts.filter(p => p.category.toLowerCase() === filters.category);
    }
    if (filters.minPrice !== undefined && filters.maxPrice !== undefined) {
        filteredProducts = filteredProducts.filter(p => p.price >= filters.minPrice && p.price <= filters.maxPrice);
    }
    if (filters.color) {
        filteredProducts = filteredProducts.filter(p => p.color === filters.color);
    }
    if (filters.tags && filters.tags.length > 0) {
        filteredProducts = filteredProducts.filter(p => filters.tags.every(tag => p.tags.includes(tag)));
    }

    // Apply sorting
    if (filters.sortBy) {
        switch (filters.sortBy) {
            case 'По популярности':
                filteredProducts.sort((a, b) => b.reviews - a.reviews);
                break;
            case 'По возрастанию цены':
                filteredProducts.sort((a, b) => a.price - b.price);
                break;
            case 'По убыванию цены':
                filteredProducts.sort((a, b) => b.price - a.price);
                break;
            case 'Сначала новые':
                filteredProducts.sort((a, b) => (b.badges?.includes('new') ? 1 : -1));
                break;
        }
    }

    // Apply pagination
    const page = filters.page || 1;
    const pageSize = 12;
    const start = (page - 1) * pageSize;
    const paginatedProducts = filteredProducts.slice(start, start + pageSize);

    // Render products
    const productsGrid = document.querySelector('.products-grid');
    productsGrid.innerHTML = paginatedProducts.map(product => `
        <article class="product-card">
            <div class="product-image">
                <img src="${product.title.toLowerCase().replace(/ /g, '-')}.jpg" alt="${product.title} кроссовки">
                <div class="product-overlay">
                    <div class="product-actions">
                        <button class="action-btn" aria-label="Добавить в корзину"><i class="fas fa-shopping-cart"></i></button>
                        <button class="action-btn" aria-label="Добавить в избранное"><i class="fas fa-heart"></i></button>
                        <button class="action-btn quick-view" aria-label="Быстрый просмотр" data-id="${product.id}"><i class="fas fa-eye"></i></button>
                    </div>
                </div>
                ${product.badges ? `<div class="product-badges">${product.badges.map(b => `<span class="badge ${b}">${b.toUpperCase()}</span>`).join('')}</div>` : ''}
            </div>
            <div class="product-info">
                <h2 class="product-title">${product.title}</h2>
                <div class="product-price">₽${product.price}${product.originalPrice ? ` <span>₽${product.originalPrice}</span>` : ''}</div>
                <div class="product-stock">${product.stock}</div>
                <div class="product-rating">
                    ${Array(Math.floor(product.rating)).fill('<i class="fas fa-star"></i>').join('')}
                    ${product.rating % 1 !== 0 ? '<i class="fas fa-star-half-alt"></i>' : ''}
                    ${Array(5 - Math.ceil(product.rating)).fill('<i class="far fa-star"></i>').join('')}
                    <span>(${product.reviews})</span>
                </div>
                <div class="product-characteristics">
                    ${product.tags.slice(0, 2).map(tag => `<span class="characteristic">${tag}</span>`).join('')}
                </div>
            </div>
        </article>
    `).join('');

    // Update product count
    document.querySelector('.products-control p').textContent = `Showing ${paginatedProducts.length} of ${filteredProducts.length} results`;
}