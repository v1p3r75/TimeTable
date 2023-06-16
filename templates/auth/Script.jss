function validateForm() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm-password").value;
    
    if (password.trim() === "") {
        alert("Veuillez entrer un mot de passe.");
        return false;
    }
    
    if (password !== confirmPassword) {
        alert("Les mots de passe ne correspondent pas.");
        return false;
    }
    
    return true;
}
