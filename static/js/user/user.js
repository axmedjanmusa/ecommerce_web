document.addEventListener('DOMContentLoaded', () => {
    // Real-time form validation feedback
    const inputs = document.querySelectorAll('form input');
    inputs.forEach(input => {
        input.addEventListener('input', () => {
            if (input.value.trim() === '') {
                input.style.borderColor = '#b91c1c';
                input.style.boxShadow = '0 0 10px rgba(185, 28, 28, 0.5)';
            } else {
                input.style.borderColor = '#ff6200';
                input.style.boxShadow = '0 0 10px rgba(255, 98, 0, 0.5)';
            }
        });
    });

    // Shadow Clone Jutsu effect on button click
    const buttons = document.querySelectorAll('.btn-primary');
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            button.style.transform = 'scale(0.9)';
            button.style.boxShadow = '0 0 20px rgba(255, 98, 0, 1), 0 0 40px rgba(255, 98, 0, 0.7)';
            setTimeout(() => {
                button.style.transform = 'scale(1)';
                button.style.boxShadow = 'none';
            }, 200);
            // Create a temporary "chakra burst" effect
            const burst = document.createElement('div');
            burst.style.position = 'absolute';
            burst.style.width = '50px';
            burst.style.height = '50px';
            burst.style.background = 'radial-gradient(circle, rgba(255, 98, 0, 0.8), transparent)';
            burst.style.borderRadius = '50%';
            burst.style.left = '50%';
            burst.style.top = '50%';
            burst.style.transform = 'translate(-50%, -50%)';
            burst.style.animation = 'burst 0.5s ease-out forwards';
            button.appendChild(burst);
            setTimeout(() => burst.remove(), 500);
        });
    });

    // Define burst animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes burst {
            0% { transform: translate(-50%, -50%) scale(0); opacity: 1; }
            100% { transform: translate(-50%, -50%) scale(2); opacity: 0; }
        }
    `;
    document.head.appendChild(style);
});