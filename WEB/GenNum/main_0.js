document.body.style.fontFamily = 'sans-serif';
let h1 = document.querySelector('h1');
let h2 = document.querySelector('h2');
let h3 = document.querySelector('h3');

h1.className = 'header';
h2.className = 'header';
h3.className = 'header';

// Helper function to check if a number is prime
let isPrime = num => {
  if (num < 2) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
};

// Style headersx
let stdFontWeight = 400;
document.querySelectorAll('.header').forEach(x => {
  x.style.textAlign = 'center';
  x.style.fontWeight = `${stdFontWeight}`;
  x.style.padding = '2px';
  x.style.margin = '0px';
  stdFontWeight -= 30;
});
h2.style.textDecoration = 'underline';
h1.style.color = 'green';

// Create container for the table
let container = document.createElement('div');
let table = document.createElement('table');

function generateNumbers(numCount) {
  table.innerHTML = ''; // Clear previous content
  let row;

  for (let i = 0; i <= numCount; i++) {
    if (i % 6 === 0) {
      row = document.createElement('tr');
      table.appendChild(row);
    }
    
    let cell = document.createElement('td');
    cell.textContent = i;
    cell.style.padding = '10px';
    cell.style.textAlign = 'center';
    cell.style.fontWeight = 'bold';

    // Set colors based on number type
    if (isPrime(i)) {
      cell.style.backgroundColor = 'red';
    } else if (i % 2 === 0) {
      cell.style.backgroundColor = 'green';
    } else {
      cell.style.backgroundColor = 'yellow';
    }
    row.appendChild(cell);
  }
}

// Validation message
let msg = document.querySelector('#message');
let inputArea = document.querySelector('#bar');
inputArea.addEventListener('keypress', key => {
  let val = parseInt(inputArea.value);
  if (val < 0 || val > 100000) {
    msg.textContent = 'Please enter a number between 1-100000!';
  } else {
    msg.textContent = '';
  }
});

let button = document.querySelector('#button_1');
button.addEventListener('click', () => {
  let inputValue = parseInt(inputArea.value);
  if (isNaN(inputValue) || inputValue > 100000 || inputValue < 0) {
    msg.textContent = 'Enter a valid number between 1 and 100000.';
  } else {
    generateNumbers(inputValue);
  }
});

// Style the table
table.style.width = '60%';
table.style.margin = 'auto';
table.style.marginTop = '10px';
table.style.textAlign = 'center';
table.style.borderCollapse = 'collapse';
table.style.fontSize = '18px';
table.style.color = 'white';

// Append table to the container and body
container.appendChild(table);
document.body.appendChild(container);
