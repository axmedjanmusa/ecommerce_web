// Function to show a temporary cart notification (keeping this as is)
function showCartNotification() {
    const notification = document.getElementById('cartNotification');
    if (notification) {
        notification.classList.remove('hidden');
        setTimeout(() => {
            notification.classList.add('hidden');
        }, 3000); // Notification disappears after 3 seconds
    }
}

// Global variable to store the timeout ID for hiding the dropdown (keeping this as is)
let profileDropdownHideTimeout;

// Function to initialize the profile dropdown behavior (SIMPLIFIED FOR DEBUGGING)
function initProfileDropdown() {
    const dropdown = document.querySelector('.dropdown');
    const dropdownContent = dropdown ? dropdown.querySelector('.dropdown-content') : null;

    console.log('Initializing profile dropdown...');
    console.log('Dropdown element found:', dropdown);
    console.log('Dropdown content element found:', dropdownContent);

    if (dropdown && dropdownContent) {
        // Ensure initial state is hidden by default
        dropdownContent.style.display = 'none';
        console.log('Dropdown content initially set to display: none');

        // Function to show the dropdown
        function showDropdown() {
            clearTimeout(profileDropdownHideTimeout);
            dropdownContent.style.display = 'block';
            console.log('Dropdown shown');
        }

        // Function to hide the dropdown
        function hideDropdown() {
            dropdownContent.style.display = 'none';
            console.log('Dropdown hidden');
        }

        // Desktop/Tablet: Show menu on mouse enter
        dropdown.addEventListener('mouseenter', function() {
            if (window.innerWidth >= 768) {
                showDropdown();
            }
        });

        // Desktop/Tablet: Hide menu with a delay on mouse leave
        dropdown.addEventListener('mouseleave', function() {
            if (window.innerWidth >= 768) {
                profileDropdownHideTimeout = setTimeout(() => {
                    hideDropdown();
                }, 300); // Small delay before hiding
            }
        });

        // Mobile: Toggle menu on click
        dropdown.addEventListener('click', function(e) {
            // Check if the click target is the dropdown itself or its immediate children
            // This prevents clicks on items *inside* the dropdown content from re-toggling it
            if (!dropdownContent.contains(e.target) || e.target === dropdown) {
                 e.preventDefault(); // Prevent default if clicking the main toggle area
                 e.stopPropagation(); // Prevent propagation to document click listener

                if (dropdownContent.style.display === 'block') {
                    hideDropdown();
                } else {
                    showDropdown();
                }
            } else {
                // Allow clicks on dropdown content items to work normally
                console.log('Clicked inside dropdown content, not toggling.');
            }
        });

        // Close dropdown if clicking outside
        document.addEventListener('click', function(e) {
            if (dropdownContent.style.display === 'block' && !dropdown.contains(e.target)) {
                console.log('Clicked outside dropdown, hiding.');
                hideDropdown();
            }
        });

        // Handle window resize (optional, but good for responsiveness)
        window.addEventListener('resize', () => {
            if (window.innerWidth >= 768 && dropdownContent.style.display === 'block') {
                // If resized to desktop, and it's open, hide it
                hideDropdown();
            } else if (window.innerWidth < 768 && dropdownContent.style.display === 'none' && !dropdown.matches(':hover')) {
                // If resized to mobile, and it's hidden (and not hovered on desktop mode),
                // ensure it's ready for mobile clicks.
                // No action needed here, as click handler will take care of it.
            }
        });

    }
}


// Animation on page load (for elements with .slide-in class) (keeping this as is)
function animateOnLoad() {
    const elements = document.querySelectorAll('.slide-in');
    elements.forEach((el, index) => {
        setTimeout(() => {
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }, index * 200);
    });
    const heroContainer = document.querySelector('section.hero-pattern .container');
    if (heroContainer) {
        const typewriter = document.createElement('div');
        typewriter.className = 'typewriter text-xl text-purple-300 mb-4';
        typewriter.textContent = 'Только для настоящих отаку...';
        heroContainer.prepend(typewriter);
    }
}

// Parallax effect for elements with .parallax class (keeping this as is)
function handleParallaxScroll() {
    const scrollPosition = window.pageYOffset;
    const parallaxElements = document.querySelectorAll('.parallax');
    parallaxElements.forEach(function(element) {
        element.style.backgroundPositionY = (scrollPosition * 0.5) + 'px';
    });
}

// Animation on scroll (for elements with .slide-in class) (keeping this as is)
function animateOnScroll() {
    const elements = document.querySelectorAll('.slide-in');
    const windowHeight = window.innerHeight;
    const windowTop = window.scrollY;
    const windowBottom = windowTop + windowHeight;
    elements.forEach(function(element) {
        const rect = element.getBoundingClientRect();
        const elementTop = rect.top + window.scrollY;
        const elementBottom = rect.bottom + window.scrollY;
        if (elementBottom > windowTop && elementTop < windowBottom - 100) {
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }
    });
}

// Event Listeners for DOMContentLoaded and Scroll (keeping this as is)
document.addEventListener('DOMContentLoaded', () => {
    animateOnLoad();
    initProfileDropdown(); // This will call the simplified function
    animateOnScroll();
});

window.addEventListener('scroll', () => {
    handleParallaxScroll();
    animateOnScroll();
});

// Initial call to set parallax position if already scrolled on page load (keeping this as is)
handleParallaxScroll();