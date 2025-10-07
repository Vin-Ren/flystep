
function showModal({ title = '', desc = '', formHtml = '', onSubmit = null, submitText = 'Submit', cancelText = 'Cancel', submitType = 'normal', showBody = true }) {
    const modal = document.getElementById('genericModal');
    const modalContent = document.getElementById('genericModalContent');
    const modalTitle = document.getElementById('modal-title');
    const modalDesc = document.getElementById('modal-desc');
    const modalBody = document.getElementById('modal-body');
    const warningIcon = document.getElementById('modal-warning-icon');
    const submitBtn = document.getElementById('modalSubmitButton');
    const cancelBtn = document.getElementById('modalCancelButton');

    if (!modal) {
        console.error('Modal component not found. Make sure modal.html is included in your template.');
        return;
    }

    // Set modal content
    modalTitle.textContent = title;
    modalDesc.textContent = desc;
    modalBody.innerHTML = formHtml;
    submitBtn.textContent = submitText;
    cancelBtn.textContent = cancelText;

    // Show/hide modal body based on showBody parameter
    if (showBody) {
        modalBody.classList.remove('hidden');
    } else {
        modalBody.classList.add('hidden');
    }

    if (submitType === 'danger') {
        warningIcon.classList.remove('hidden');
    } else {
        warningIcon.classList.add('hidden');
    }

    submitBtn.classList.remove('bg-green-600', 'hover:bg-green-700', 'bg-red-600', 'hover:bg-red-700');
    if (submitType === 'danger') {
        submitBtn.classList.add('bg-red-600', 'hover:bg-red-700');
    } else {
        submitBtn.classList.add('bg-green-600', 'hover:bg-green-700');
    }

    modal.classList.remove('hidden');
    setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
    }, 50);

    // Attach submit handler
    submitBtn.onclick = function (e) {
        e.preventDefault();
        if (onSubmit) {
            onSubmit();
        }
    };
}

function hideModal() {
    const modal = document.getElementById('genericModal');
    const modalContent = document.getElementById('genericModalContent');

    if (!modal || !modalContent) return;

    modalContent.classList.remove('opacity-100', 'scale-100');
    modalContent.classList.add('opacity-0', 'scale-95');

    setTimeout(() => {
        modal.classList.add('hidden');
    }, 150);
}

// Helper for AJAX form submission
function submitAjaxForm(formId, url, successCallback) {
    const form = document.getElementById(formId);

    if (!form) {
        console.error(`Form with id "${formId}" not found.`);
        if (window.showToast) window.showToast('Error', 'Form not found', 'error');
        return;
    }

    fetch(url, {
        method: 'POST',
        body: new FormData(form),
        credentials: 'include'
    })
    .then(response => {
        if (!response.ok) throw new Error('Network response was not ok');
        return response.json();
    })
    .then(data => {
        if (successCallback) successCallback(data);
        hideModal();
        if (window.showToast) window.showToast('Success', 'Operation completed successfully', 'success');
    })
    .catch(error => {
        console.error('Form submission error:', error);
        if (window.showToast) window.showToast('Error', 'Failed to submit form', 'error');
    });
}
