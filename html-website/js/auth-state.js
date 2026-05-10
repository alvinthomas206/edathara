import { auth } from './firebase-config.js';
import { onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-auth.js";

document.addEventListener('DOMContentLoaded', () => {
    onAuthStateChanged(auth, (user) => {
        const desktopBtn = document.getElementById('auth-btn-desktop');
        const mobileBtn = document.getElementById('auth-btn-mobile');
        
        if (user) {
            // User is signed in.
            if (desktopBtn) {
                desktopBtn.href = "members.html";
                desktopBtn.innerHTML = '<i class="fa-solid fa-user-circle mr-1"></i> Members';
                desktopBtn.classList.remove('bg-maroon', 'hover:bg-maroon/90', 'shadow-maroon/30');
                desktopBtn.classList.add('bg-darkgreen', 'hover:bg-green-800', 'shadow-green-900/30');
            }
            if (mobileBtn) {
                mobileBtn.href = "members.html";
                mobileBtn.innerHTML = '<i class="fa-solid fa-user-circle mr-2"></i> Members Area';
                mobileBtn.classList.remove('text-maroon');
                mobileBtn.classList.add('text-darkgreen', 'font-bold');
            }
        } else {
            // No user is signed in.
            if (desktopBtn) {
                desktopBtn.href = "login.html";
                desktopBtn.innerHTML = 'Login';
                desktopBtn.classList.add('bg-maroon', 'hover:bg-maroon/90', 'shadow-maroon/30');
                desktopBtn.classList.remove('bg-darkgreen', 'hover:bg-green-800', 'shadow-green-900/30');
            }
            if (mobileBtn) {
                mobileBtn.href = "login.html";
                mobileBtn.innerHTML = 'Login / Sign Up';
                mobileBtn.classList.add('text-maroon');
                mobileBtn.classList.remove('text-darkgreen', 'font-bold');
            }
        }
    });
});
