        // logging function
        const logEvent = (elementType, message) => {
            console.log(`[${elementType}] ${message}`);
        };

        // Arrow function to autofill the input field
        const autofillInput = () => {
            const inputField = document.getElementById('inputText');
            inputField.value = "Has passat per sobre el camp d'input!";
        };

        // Arrow function to clear the input field
        const clearInput = () => {
            const inputField = document.getElementById('inputText');
            logEvent(inputField.classList , 'Value before clear:'+inputField.value);
            inputField.value = '';
        };

        // Add event listeners to call the functions
        document.getElementById('inputText').addEventListener('mouseover', autofillInput);
        document.getElementById('clearButton').addEventListener('click', clearInput);