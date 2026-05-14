function login() {

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if(username === "krishnaveni@gmail.com" && password === "08") {

        window.location.href = "index.html";

    } else {

        alert("Invalid username or password");

    }
}