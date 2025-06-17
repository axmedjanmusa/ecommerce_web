// shop-filters.js - Обрабатывает функциональность фильтров (категории, цена, цвета, размеры)

// Вспомогательная функция для обновления параметров URL и перезагрузки страницы
function updateFilters(newFilters) {
    const url = new URL(window.location.href);
    const params = url.searchParams;

    // Применить новые фильтры
    for (const key in newFilters) {
        if (newFilters[key] !== null && newFilters[key] !== undefined && newFilters[key] !== '') {
            params.set(key, newFilters[key]);
        } else {
            params.delete(key); // Удалить параметр, если значение пустое/null
        }
    }

    // Перенаправить на новый URL
    window.location.href = url.toString();
}

document.addEventListener('DOMContentLoaded', function() {
    // Фильтры категорий - Нажатие на тег <a> естественно перезагрузит страницу
    // Здесь не требуется специальный JS, кроме установки активного состояния, что делается Django
    // в shop.html на основе контекста 'selected_category'.

    // Слайдеры ценового диапазона
    const minPriceSlider = document.getElementById('minPrice');
    const maxPriceSlider = document.getElementById('maxPrice');
    const minPriceDisplay = document.querySelector('.min-price');
    const maxPriceDisplay = document.querySelector('.max-price');
    const priceFilterBtn = document.getElementById('priceFilterBtn');

    // Инициализация отображаемых значений из текущего URL или значений по умолчанию
    minPriceDisplay.textContent = `₽${minPriceSlider.value}`;
    maxPriceDisplay.textContent = `₽${maxPriceSlider.value}`;

    // Обновление отображения при изменении слайдеров
    minPriceSlider.addEventListener('input', function() {
        let minValue = parseInt(this.value);
        let maxValue = parseInt(maxPriceSlider.value);
        if (minValue > maxValue - 100) { // Сохранять минимальный диапазон в 100
            minValue = maxValue - 100;
            this.value = minValue;
        }
        minPriceDisplay.textContent = `₽${minValue}`;
    });

    maxPriceSlider.addEventListener('input', function() {
        let maxValue = parseInt(this.value);
        let minValue = parseInt(minPriceSlider.value);
        if (maxValue < minValue + 100) { // Сохранять минимальный диапазон в 100
            maxValue = minValue + 100;
            this.value = maxValue;
        }
        maxPriceDisplay.textContent = `₽${maxValue}`;
    });

    // Обработчик нажатия кнопки фильтра цены
    if (priceFilterBtn) {
        priceFilterBtn.addEventListener('click', function() {
            updateFilters({
                min_price: minPriceSlider.value,
                max_price: maxPriceSlider.value
            });
        });
    }


    // Фильтры цветов
    const colorCircles = document.querySelectorAll('.color-circle');
    colorCircles.forEach(circle => {
        circle.addEventListener('click', function(e) {
            e.preventDefault(); // Предотвратить стандартное поведение ссылки
            const color = this.getAttribute('data-color');
            const currentUrl = new URL(window.location.href);

            // Переключение цветового фильтра: если уже выбран, удалить его; в противном случае, установить.
            if (currentUrl.searchParams.get('color') === color) {
                updateFilters({ color: '' }); // Передать пустую строку для удаления параметра
            } else {
                updateFilters({ color: color });
            }
        });
    });

    // Фильтр размера (используя элемент select)
    const sizeFilter = document.getElementById('sizeFilter');
    if (sizeFilter) {
        sizeFilter.addEventListener('change', function() {
            updateFilters({ size: this.value });
        });
    }

    // Функция сортировки (уже обрабатывается во встроенном скрипте shop.html)
    // window.updateSort уже глобально доступен благодаря его объявлению в shop.html
    // так что здесь не требуется никаких изменений.

    // Переключатель вида (уже обрабатывается во встроенном скрипте shop.html)
    // Это чисто клиентский рендеринг и не влияет на серверную фильтрацию.
    // Здесь не требуется никаких изменений.

    // Фильтры тегов (Они не были напрямую обработаны в вашем views.py,
    // поэтому я закомментировал исходную логику. Если вы реализуете фильтрацию по тегам
    // на бэкенде, вам нужно будет повторно включить и настроить этот раздел.)
    /*
    const tags = document.querySelectorAll('.tag');
    tags.forEach(tag => {
        tag.addEventListener('click', () => {
            tag.classList.toggle('active');
            // Это потребует более сложной логики фильтрации, например, тегов, разделенных запятыми
            // и вызова AJAX или манипуляций с параметрами URL для отправки в Django.
            // В соответствии с вашим текущим views.py, фильтрация по тегам не реализована.
            // Если вы хотите ее реализовать, вам нужно будет добавить логику в views.py
            // для фильтрации по списку тегов.
        });
    });
    */
});