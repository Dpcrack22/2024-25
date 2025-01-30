// Variables (Para almacenar datos)
let nombre = "Juan"; // Variable que puede cambiar
const edadd = 25; // Constante, no cambia
var ciudad = "Madrid"; // No recomendado, usa let


//  Tipos de Datos
let numero = 10; // Número
let texto = "Hola"; // String (Texto)
let esVerdadero = true; // Booleano (true o false)
let arreglo = [1, 2, 3, 4]; // Array
let objeto = { nombre: "Ana", edad: 30 }; // Objeto


//  Operadores Básicos
let suma = 5 + 3; // 8
let resta = 10 - 4; // 6
let multiplicacion = 2 * 3; // 6
let division = 10 / 2; // 5
let resto = 10 % 3; // 1 (módulo)


// Condicionales (if - else)
let edad2 = 18;
if (edad2 >= 18) {
    console.log("Eres mayor de edad");
} else {
    console.log("Eres menor de edad");
}


//Bucles (Loops)
for (let i = 0; i < 5; i++) {
    console.log("Número:", i);
}

let j = 0;
while (j < 3) {
    console.log("Hola");
    j++;
}

// Funciones (Para reutilizar código)
function saludar(nombre) {
    return "Hola, " + nombre;
}
console.log(saludar("Carlos")); // "Hola, Carlos"

//  Eventos en el navegador
document.getElementById("miBoton").addEventListener("click", function() {
    alert("¡Clickeaste el botón!");
});


// Manipulación del DOM (cambiar HTML con JS)
document.getElementById("titulo").innerText = "Nuevo Título";
document.getElementById("caja").style.backgroundColor = "red";



// Pida al usuario que ingrese su edad.
//Si tiene menos de 18 años, obtiene un 10% de descuento.
//Si tiene 65 años o más, obtiene un 20% de descuento.
//En caso contrario, no hay descuento.
//Muestra el resultado en la consola.
// 1. Pedir la edad al usuario con prompt()
let edad = prompt("Ingrese su edad:");

// 2. Convertir la edad a número
edad = Number(edad);

// 3. Definir el descuento
let descuento = 0; // Usamos let porque puede cambiar

// 4. Aplicar condiciones
if (edad < 18) {
    descuento = 10;
} else if (edad >= 65) {
    descuento = 20;
}

// 5. Mostrar el resultado
console.log("Su descuento es del " + descuento + "%");



// Usa console.log() para ver valores y errores
// Si tu código no hace lo que esperas, usa console.log() para ver qué pasa.

function suma(a, b) {
    console.log("Valor de a:", a); // 👀 Verifica el valor de a
    console.log("Valor de b:", b); // 👀 Verifica el valor de b
    return a + b;
}
console.log(suma(5, 3)); // 8


// Usa debugger; para pausar el código
// Si el error es difícil de encontrar, usa debugger; para pausar la ejecución y ver el estado de las variables.
function calcularPrecio(precio, descuento) {
    debugger; // 🔥 Pausa la ejecución aquí
    let precioFinal = precio - (precio * descuento / 100);
    return precioFinal;
}
console.log(calcularPrecio(100, 20)); // Espera 80


// 🔴 Error 
// ReferenceError: x is not defined
// Estás usando una variable que no existe.
// Asegúrate de que x está definida antes de usarla.

// 🔴 Error 
// TypeError: x is not a function
// Estás intentando llamar a algo que no es una función.
// Revisa si x realmente es una función.

// 🔴 Error 
// SyntaxError: Unexpected token
// Hay un error de sintaxis (falta un ;, {}, )).	
// Revisa si hay paréntesis o llaves mal cerradas.

// 🔴 Error 
// Cannot read properties of null (reading 'textContent')
// Intentas acceder a un elemento del DOM que no existe.	
// Usa console.log() para ver si el elemento existe.

// 🔴 Error 
// NaN (Not a Number)
// Estás intentando hacer una operación matemática con algo que no es un número.	
// Asegúrate de que los valores sean números usando Number(valor).
