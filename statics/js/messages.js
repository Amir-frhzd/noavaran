document.addEventListener('DOMContentLoaded', (event) => {
    const messages = document.querySelectorAll('#messages .message');
    messages.forEach((message) => {
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => {
                message.remove();
            }, 600); // زمان انتقال CSS
        }, 5000);
    });
});