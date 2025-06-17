// shop-main.js - Main script for initializing shop functionality

document.addEventListener('DOMContentLoaded', () => {
    // Initialize view toggle (grid/list)
    const gridViewBtn = document.querySelector('.grid-view');
    const listViewBtn = document.querySelector('.list-view');
    const productsGrid = document.querySelector('.products-grid');

    gridViewBtn.addEventListener('click', () => {
        productsGrid.classList.remove('list-view');
        gridViewBtn.classList.add('active');
        listViewBtn.classList.remove('active');
    });

    listViewBtn.addEventListener('click', () => {
        productsGrid.classList.add('list-view');
        listViewBtn.classList.add('active');
        gridViewBtn.classList.remove('active');
    });

    // Initialize other modules (filters, products, modal)
    initializeFilters();
    initializeProducts();
    initializeModal();
});