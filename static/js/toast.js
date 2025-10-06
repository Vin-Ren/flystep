// Global Toast Helper
(function(window) {
    function showToast(title, message, type = 'normal', duration = 3000) {
        let toastComponent = document.getElementById('toast-component');
        let toastTitle = document.getElementById('toast-title');
        let toastMessage = document.getElementById('toast-message');
        let toastIcon = document.getElementById('toast-icon');

        if (!toastComponent) {
            console.error('Toast component not found. Make sure toast.html is included in your template.');
            return;
        }

        // Remove all type classes first
        toastComponent.classList.remove('toast-success', 'toast-error', 'toast-normal');

        // Set type styles and icon
        if (type === 'success') {
            toastComponent.classList.add('toast-success');
            toastIcon.innerHTML = '&#10004;'; // Checkmark
        } else if (type === 'error') {
            toastComponent.classList.add('toast-error');
            toastIcon.innerHTML = '&#10008;'; // X mark
        } else if (type === 'info') {
            toastComponent.classList.add('toast-info');
            toastIcon.innerHTML = '&#9432;'; // Info icon
        } else {
            toastComponent.classList.add('toast-normal');
            toastIcon.innerHTML = '&#9432;'; // Info icon
        }

        toastTitle.textContent = title;
        toastMessage.textContent = message;

        // Show toast
        toastComponent.classList.remove('opacity-0', 'translate-y-20');
        toastComponent.classList.add('opacity-100', 'translate-y-0');

        // Auto-hide after duration
        clearTimeout(window.__toastTimeout);
        window.__toastTimeout = setTimeout(() => {
            toastComponent.classList.remove('opacity-100', 'translate-y-0');
            toastComponent.classList.add('opacity-0', 'translate-y-20');
        }, duration);
    }

    // Expose globally
    window.showToast = showToast;
})(window);
