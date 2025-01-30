document.body.style.fontFamily = 'san-serif';
let h1 = document.querySelector('h1');
let h2 = document.querySelector('h2');
let h3 = document.querySelector('h3');

h1.className = 'header';
h2.className = 'header';
h3.className = 'header';

// helper function 
let isPrime = num => {
  if (num == 1 || num == 0) return false;
  if (num == 2 || num == 3)
    return true;

  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i == 0) return false;
  }
  return true;
}

// headers styling      
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

let container = document.createElement('div');
let table = document.createElement('table');

function generateNumbers(numCount) {
  let nums = 0;  // Start from 1
  let row = document.createElement('tr'); // Create the first row

  while (nums <= numCount) {
    let cell = document.createElement('td');
    cell.textContent = nums; // Set the number in the cell

    // Apply color based on number type
    if (isPrime(nums)) {
      cell.style.backgroundColor = 'red'; // Prime numbers are red
    } else if (nums % 2 === 0) {
      cell.style.backgroundColor = 'green'; // Even numbers are green
    } else {
      cell.style.backgroundColor = 'yellow'; // Odd numbers are yellow
    }

    row.appendChild(cell); // Add the cell to the row

    // Check if the row has 6 cells
    if (row.children.length === 6) {
      table.appendChild(row); // Add the current row to the table
      row = document.createElement('tr'); // Create a new row for the next set of cells
    }

    nums++; // Increment the number
  }

  // Add any remaining cells to the table (if the last row has less than 6 cells)
  if (row.children.length > 0) {
    table.appendChild(row);
  }
}

// logic
let msg = document.querySelector('#message');
let inputArea = document.querySelector('input');
inputArea.addEventListener('keypress', key => {
  let val = parseInt(inputArea.value);
  if (val < 0 || val > 1000) {
    msg.textContent = 'Please enter a number between 1-1000!';
  } else {
    msg.textContent = ' ';
  }
});

let button = document.querySelector('#button_1');
button.addEventListener('click', () => {
  table.innerHTML = ''; // Clear table before generating numbers
  let inputValue = parseInt(inputArea.value);

  if (inputValue > 1000 || inputValue < 0) {
    msg.textContent = 'Enter a valid number between 1 and 1000.';
  } else {
    generateNumbers(inputValue);
  }
});

// table styling
table.style.width = '60%';
table.style.marginRight = '20%';
table.style.marginLeft = '20%';
table.style.marginTop = '1pc';
table.style.textAlign = 'center';
table.style.fontFamily = 'ariel';
table.style.fontSize = '15px';
table.style.fontWeight = 'bold';
table.style.color = 'white';

container.appendChild(table);
document.body.appendChild(container);

/* 

document.body.style.fontFamily = 'san-serif';:
  Establece la fuente global de la página a "sans-serif", es decir, todos los textos de la página tendrán esa tipografía, a menos que se sobrescriba en algún otro lugar.
let h1 = document.querySelector('h1');:
  querySelector selecciona el primer elemento h1 en la página.
  h1.className = 'header';:
    Aquí le asignamos a h1, h2, y h3 la clase header para que podamos aplicar estilos comunes a todos estos elementos.

    

isPrime es una función que verifica si un número es primo.
  Un número es primo si es mayor que 1 y no tiene divisores aparte de 1 y el mismo número.

if (num == 1 || num == 0):
  Si el número es 1 o 0, devuelve false porque no son números primos.

if (num == 2 || num == 3):
  Los números 2 y 3 son primos por definición, así que si el número es 2 o 3, se devuelve true.

for (let i = 2; i <= Math.sqrt(num); i++):
  Esta es la parte clave del algoritmo para verificar si un número es primo.
  Se verifica desde 2 hasta la raíz cuadrada de num porque los factores de un número n están dentro de este rango. Si no encontramos ningún divisor, es un número primo.

if (num % i == 0):  
  Aquí comprobamos si num es divisible por i. Si lo es, entonces el número no es primo y la función devuelve false.

return true;:
  Si no se encuentra ningún divisor, el número es primo y la función devuelve true.


stdFontWeight = 400;:
  Creamos una variable que controla el peso de la fuente.

document.querySelectorAll('.header').forEach(x => { ... }):
  Seleccionamos todos los elementos con la clase header (que son h1, h2, h3), y les aplicamos ciertos estilos:
    textAlign = 'center': Alinea el texto de cada encabezado al centro.
    fontWeight = ${stdFontWeight};: Cambia el peso de la fuente de cada encabezado, empezando con 400. Luego, decrece el peso en 30 para h2 y h3.
    padding = '2px' y margin = '0px': Aplica un pequeño margen y padding para espaciar un poco los elementos.

h2.style.textDecoration = 'underline';:
  Subraya el texto de h2.

h1.style.color = 'green';:
  Cambia el color del texto de h1 a verde.


document.createElement('div') y document.createElement('table'):
  Creamos un contenedor (div) y una tabla (table) para añadir más adelante los números generados.


let nums = 1;:
  Iniciamos los números desde 1 y los vamos incrementando uno a uno.

let row = document.createElement('tr');:
  Creamos una fila (<tr>) para empezar a agregar las celdas (<td>).

while (nums <= numCount):
  Creamos un ciclo que se ejecuta hasta que lleguemos al número que el usuario ha ingresado.

let cell = document.createElement('td');:
  Creamos una celda (<td>) en cada iteración.

cell.textContent = nums;:
  Asignamos el valor del número actual a la celda.

Condiciones de color:
  isPrime(nums): Si el número es primo, se le asigna el color rojo.
  nums % 2 === 0: Si el número es par, se le asigna el color verde.
  Si el número no es ni primo ni par, será impar, por lo que se le asigna el color amarillo.

Añadir la celda a la fila:
  row.appendChild(cell);: Añadimos la celda con el número y el color a la fila.

Verificación de columnas:
  Si la fila tiene 6 celdas, añadimos la fila a la tabla y creamos una nueva fila para los siguientes números.

Añadir las filas restantes:
  Si la última fila tiene menos de 6 celdas, se añade al final.


inputArea.addEventListener('keypress', ...):
  Cuando el usuario presiona una tecla en el input, se valida si el valor es un número entre 0 y 1000.
  Si el número no es válido, muestra un mensaje de error. Si es válido, limpia el mensaje.
*/