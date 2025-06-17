// Добавление товара в корзину
const addToCartButton = document.querySelector('.viewcontent__action a');
addToCartButton.addEventListener('click', (e) => {
    e.preventDefault();
    const quantity = document.querySelector('.viewcontent__action input').value;
    alert(`Добавлено ${quantity} товара(ов) в корзину!`);
});