document.addEventListener('DOMContentLoaded', () => {
    // Only handle the hint button functionality
    window.showHint = function() {
        const hintText = document.getElementById('hint-text');
        hintText.classList.toggle('hidden');
    };
}); 