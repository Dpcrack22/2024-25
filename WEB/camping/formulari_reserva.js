/*
Validació del correu electrònic:

    Comprova si l'entrada coincideix amb un format de correu electrònic estàndard fent servir RegExp.
    Mostra un missatge d'error si no és vàlid.

Validació del número:

    Assegura que el nombre de campistes és positiu.
    Mostra un missatge d'error si no és vàlid.

Data de validació:

    Assegura que les dues dates són vàlides.
    Assegura que la data d'inici és anterior a la data de finalització.
    Mostra un missatge d'error per a condicions no vàlides.
*/

        document.getElementById('reservationForm').addEventListener('submit', function (event) {
            let isValid = true;

            // Clear previous error messages
            document.getElementById('emailError').textContent = '';
            document.getElementById('campersError').textContent = '';
            document.getElementById('dateError').textContent = '';

            // Get form values
            const email = document.getElementById('email').value;
            const numCampers = document.getElementById('numCampers').value;
            const startDate = new Date(document.getElementById('startDate').value);
            const endDate = new Date(document.getElementById('endDate').value);

            // Email validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                document.getElementById('emailError').textContent = 'Introdueix una adreça de correu vàlida.';
                isValid = false;
            }

            // Number of campers validation
            if (numCampers <= 2 || isNaN(numCampers)) {
                document.getElementById('campersError').textContent = 'Per fer una reserva, el nombre de campistes ha de ser més gran de 1.';
                isValid = false;
            }

            // Date validation
            if (isNaN(startDate.getTime()) || isNaN(endDate.getTime())) {
                document.getElementById('dateError').textContent = 'Introdueix dates vàlides.';
                isValid = false;
            } else if (startDate >= endDate) {
                document.getElementById('dateError').textContent = 'La data d\'inici ha de ser abans de la data de finalització.';
                isValid = false;
            }

            // If not valid, prevent form submission
            if (!isValid) {
                event.preventDefault();
            }
        });