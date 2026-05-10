import { db } from './firebase-config.js';
import { collection, addDoc, serverTimestamp } from 'https://www.gstatic.com/firebasejs/10.8.1/firebase-firestore.js';

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contact-form');
    const status = document.getElementById('contact-status');
    const submitButton = document.getElementById('contact-submit');

    if (!form || !status || !submitButton) {
        console.warn('Contact form script loaded but form elements are missing.');
        return;
    }

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const name = document.getElementById('contact-name').value.trim();
        const branch = document.getElementById('contact-branch').value.trim();
        const contactDetail = document.getElementById('contact-contact').value.trim();
        const message = document.getElementById('contact-message').value.trim();

        status.textContent = '';
        status.classList.remove('text-red-500', 'text-green-600');

        if (!name || !contactDetail || !message) {
            status.textContent = 'Please fill in all required fields.';
            status.classList.add('text-red-500');
            return;
        }

        submitButton.disabled = true;
        submitButton.textContent = 'Sending...';
        status.textContent = '';

        try {
            await addDoc(collection(db, 'contactMessages'), {
                name,
                branch,
                contactDetail,
                message,
                read: false,
                createdAt: serverTimestamp()
            });

            form.reset();
            status.textContent = 'Thank you! Your message has been sent successfully.';
            status.classList.remove('text-red-500');
            status.classList.add('text-green-600');
        } catch (error) {
            console.error('Contact form submit error:', error);
            status.textContent = `Unable to send your message right now. ${error?.message ?? 'Please check the console.'}`;
            status.classList.remove('text-green-600');
            status.classList.add('text-red-500');
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = 'Send Message';
        }
    });
});
