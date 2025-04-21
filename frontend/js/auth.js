const backendUrl = "http://localhost:8000/api/users/";

document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("loginForm");
  const registerForm = document.getElementById("registerForm");

  // Handle Login Form Submission
  if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;

      try {
        const response = await fetch(`${backendUrl}login/`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email, password }),
        });

        const data = await response.json();

        if (response.ok) {
          // Store the access token in localStorage
          localStorage.setItem("access_token", data.access);
          alert("Login successful!");
          // Redirect to dashboard or review form
          window.location.href = "dashboard.html";
        } else {
          alert("Login failed! " + data.detail);
        }
      } catch (error) {
        alert("An error occurred during login: " + error.message);
      }
    });
  }

  // Handle Registration Form Submission
  if (registerForm) {
    registerForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const first_name = document.getElementById("first_name").value;
      const last_name = document.getElementById("last_name").value;
      const email = document.getElementById("email").value;
      const mobile = document.getElementById("mobile").value;
      const password = document.getElementById("password").value;
  
      try {
        const response = await fetch(`${backendUrl}signup/`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ first_name, last_name, email, mobile, password }),
        });
  
        if (response.ok) {
          alert("Registration successful! Please login.");
          window.location.href = "login.html";
        } else {
          const data = await response.json();
          alert("Registration failed! " + (data.detail || "Check your form and try again."));
        }
      } catch (error) {
        alert("An error occurred during registration: " + error.message);
      }
    });
  }
  
});
