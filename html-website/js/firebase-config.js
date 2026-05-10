import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-analytics.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-firestore.js";
import { getStorage } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-storage.js";

const firebaseConfig = {
    apiKey: "AIzaSyAZNCPmlff0BXHouCDT3i42Vv0RJ_goPLw",
    authDomain: "cypher-projects-6cce3.firebaseapp.com",
    databaseURL: "https://cypher-projects-6cce3-default-rtdb.firebaseio.com",
    projectId: "cypher-projects-6cce3",
    storageBucket: "cypher-projects-6cce3.firebasestorage.app",
    messagingSenderId: "454711938195",
    appId: "1:454711938195:web:876fb3046d091061251166",
    measurementId: "G-WJF8L0C0YX"
};

export const app = initializeApp(firebaseConfig);
let analyticsInstance = null;
try {
    analyticsInstance = getAnalytics(app);
} catch (e) {
    console.error("Analytics failed to load:", e);
}
export const analytics = analyticsInstance;
export const auth = getAuth(app);
export const db = getFirestore(app);
export const storage = getStorage(app);
