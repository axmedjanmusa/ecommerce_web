// Валидация ввода количества товара
const quantityInput = document.querySelector('.viewcontent__action input');
quantityInput.addEventListener('input', () => {
    if (quantityInput.value < 1) {
        quantityInput.value = 1;
        alert('Количество не может быть меньше 1!');
    }
});