// shop-modal.js - Manages quick-view modal functionality

function initializeModal() {
    const modal = document.querySelector('.quick-view-modal');
    const closeBtn = document.querySelector('.close-modal');
    const quantityMinus = document.querySelector('.quantity-btn[aria-label="Уменьшить количество"]');
    const quantityPlus = document.querySelector('.quantity-btn[aria-label="Увеличить количество"]');
    const quantityInput = document.querySelector('.quantity-selector input');

    // Open modal on quick-view click
    document.addEventListener('click', (e) => {
        if (e.target.closest('.quick-view')) {
            const productId = e.target.closest('.quick-view').dataset.id;
            const product = products.find(p => p.id == productId); // From shop-products.js
            if (product) {
                updateModalContent(product);
                modal.classList.add('active');
                modal.setAttribute('aria-hidden', 'false');
            }
        }
    });

    // Close modal
    closeBtn.addEventListener('click', () => {
        modal.classList.remove('active');
        modal.setAttribute('aria-hidden', 'true');
    });

    // Close modal on outside click
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.remove('active');
            modal.setAttribute('aria-hidden', 'true');
        }
    });

    // Quantity controls
    quantityMinus.addEventListener('click', () => {
        let value = parseInt(quantityInput.value);
        if (value > 1) {
            quantityInput.value = value - 1;
        }
    });

    quantityPlus.addEventListener('click', () => {
        let value = parseInt(quantityInput.value);
        quantityInput.value = value + 1;
    });

    // Add to cart (placeholder)
    document.querySelector('.add-to-cart-btn').addEventListener('click', () => {
        alert(`Добавлено ${quantityInput.value} товара в корзину!`);
    });
}

function updateModalContent(product) {
    const modal = document.querySelector('.modal-product');
    modal.innerHTML = `
        <div class="modal-product-image">
            <img src="${product.title.toLowerCase().replace(/ /g, '-')}.jpg" alt="${product.title} кроссовки">
        </div>
        <div class="modal-product-info">
            <h2 class="modal-product-title">${product.title}</h2>
            <div class="modal-product-rating">
                ${Array(Math.floor(product.rating)).fill('<i class="fas fa-star"></i>').join('')}
                ${product.rating % 1 !== 0 ? '<i class="fas fa-star-half-alt"></i>' : ''}
                ${Array(5 - Math.ceil(product.rating)).fill('<i class="far fa-star"></i>').join('')}
                <span>(${product.reviews} отзыва)</span>
            </div>
            <div class="modal-product-price">₽${product.price}${product.originalPrice ? ` <span>₽${product.originalPrice}</span>` : ''}</div>
            <div class="modal-product-stock">${product.stock}</div>
            <p class="modal-product-description">
                Эксклюзивные кроссовки с персонажами ваших любимых аниме. Ограниченный выпуск с уникальным дизайном.
                Высококачественные материалы и стильный дизайн для настоящих отаку.
            </p>
            <div class="modal-product-characteristics">
                <h3>Характеристики:</h3>
                <ul>
                    <li>Материал: Высококачественный текстиль, искусственная кожа</li>
                    <li>Подошва: Резина, EVA</li>
                    <li>Особенности: Эксклюзивный дизайн, лимитированная коллекция</li>
                    <li>Персонаж: ${product.title.split(' - ')[0]}</li>
                </ul>
            </div>
            <div class="modal-product-actions">
                <div class="quantity-selector">
                    <button class="quantity-btn" aria-label="Уменьшить количество">-</button>
                    <input type="number" value="1" min="1" aria-label="Количество">
                    <button class="quantity-btn" aria-label="Увеличить количество">+</button>
                </div>
                <button class="add-to-cart-btn">ДОБАВИТЬ В КОРЗИНУ</button>
            </div>
            <div class="modal-product-categories">
                Категории: ${product.tags.map(tag => `<a href="#">${tag}</a>`).join(', ')}
            </div>
        </div>
    `;
}