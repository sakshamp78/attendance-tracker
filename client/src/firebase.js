// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
import { getAuth } from "firebase/auth";
// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBP3ltgsk6x50olOu0ddtKpqAoCAyRXfyc",
  authDomain: "attendance-tracker-9a4f1.firebaseapp.com",
  projectId: "attendance-tracker-9a4f1",
  storageBucket: "attendance-tracker-9a4f1.appspot.com",
  messagingSenderId: "777950726702",
  appId: "1:777950726702:web:edb8d78904b2086bae6dbf"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export default app