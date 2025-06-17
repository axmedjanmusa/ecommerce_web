// Инициализация табов для переключения изображений продукта
document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('#myffTab .nav-link');
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
        });
    });
});
// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    // === Логика для счетчика символов комментария ===
    const commentTextArea = document.getElementById('id_comment'); // ID вашего поля комментария
    const charCountDisplay = document.getElementById('comment-char-count');
    const submitButton = document.querySelector('.add-review-form button[type="submit"]'); // Кнопка отправки
    const maxChars = 500; // Максимальное количество символов

    if (commentTextArea && charCountDisplay && submitButton) {
        function updateCharCount() {
            const currentLength = commentTextArea.value.length;
            charCountDisplay.textContent = `${currentLength}/${maxChars} символов`;

            if (currentLength > maxChars) {
                charCountDisplay.classList.add('error'); /* Добавляем класс error */
                submitButton.disabled = true; /* Отключаем кнопку, если превышен лимит */
                submitButton.style.opacity = '0.7'; /* Визуально показываем, что кнопка отключена */
                submitButton.style.cursor = 'not-allowed';
            } else {
                charCountDisplay.classList.remove('error'); /* Удаляем класс error */
                submitButton.disabled = false; /* Включаем кнопку */
                submitButton.style.opacity = '1';
                submitButton.style.cursor = 'pointer';
            }
        }

        commentTextArea.addEventListener('input', updateCharCount);
        updateCharCount(); // Инициализация при загрузке страницы
    }