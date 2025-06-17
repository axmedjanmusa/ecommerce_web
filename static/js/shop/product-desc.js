// Переключение табов описания
const descTabs = document.querySelectorAll('#myerTab .nav-link');
descTabs.forEach(tab => {
    tab.addEventListener('click', () => {
        descTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
    });
});