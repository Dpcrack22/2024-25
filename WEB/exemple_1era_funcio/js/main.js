// Function to autofill the input field
function autofillInput() {
    const inputField = document.getElementById('inputText');
    inputField.value = "Has passat per sobre el camp d'input!";
}

// Function to clear the input field
function clearInput() {
    const inputField = document.getElementById('inputText');
    inputField.value = '';
}

// Add event listeners to call the functions
document.getElementById('inputText').addEventListener('mouseover', autofillInput);
document.getElementById('clearButton').addEventListener('click', clearInput);