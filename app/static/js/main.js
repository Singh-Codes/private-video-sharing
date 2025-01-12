// Handle file upload progress and validation
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.querySelector('input[type="file"]');
    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                // Check file size (100MB limit)
                const maxSize = 100 * 1024 * 1024; // 100MB in bytes
                if (file.size > maxSize) {
                    alert('File size exceeds 100MB limit');
                    e.target.value = ''; // Clear the file input
                    return;
                }

                // Check file type
                const allowedTypes = ['text/plain', 'application/pdf', 'image/png', 'image/jpeg', 'image/gif', 
                                    'video/mp4', 'video/avi', 'video/quicktime'];
                if (!allowedTypes.includes(file.type)) {
                    alert('File type not allowed');
                    e.target.value = ''; // Clear the file input
                    return;
                }
            }
        });
    }

    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Handle copy button clicks
    const copyButtons = document.querySelectorAll('.copy-btn');
    copyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const originalText = this.textContent;
            this.textContent = 'Copied!';
            setTimeout(() => {
                this.textContent = originalText;
            }, 2000);
        });
    });
});
