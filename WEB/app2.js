// Obtener los elementos del DOM
const inputPrecio = document.getElementById("precioProducto");
const botonAgregar = document.getElementById("agregarProducto");
const listaProductos = document.getElementById("listaProductos");
const inputDescuento = document.getElementById("descuento");
const botonCalcular = document.getElementById("calcularTotal");

const totalSinDescuento = document.getElementById("totalSinDescuento");
const descuentoAplicado = document.getElementById("descuentoAplicado");
const totalFinal = document.getElementById("totalFinal");

let productos = []; // Array para guardar los productos

// Función para renderizar la lista de productos
function renderizarProductos() {
    listaProductos.innerHTML = "";  // Limpiar la lista antes de renderizar

    // Usamos un bucle para recorrer el array de productos
    productos.forEach((producto, index) => {
        const productoElemento = document.createElement("li");
        productoElemento.classList.add("producto");
        productoElemento.textContent = `$${producto.precio}`;
        
        // Crear botón para eliminar producto
        const botonEliminar = document.createElement("button");
        botonEliminar.textContent = "Eliminar";
        botonEliminar.addEventListener("click", () => {
            productos.splice(index, 1);  // Eliminar el producto del array
            renderizarProductos();  // Volver a renderizar la lista
        });

        // Añadir botón de eliminar a cada producto
        productoElemento.appendChild(botonEliminar);

        // Añadir el producto a la lista
        listaProductos.appendChild(productoElemento);
    });
}

// Función para calcular los totales
function calcularTotal() {
    let total = productos.reduce((acc, producto) => acc + producto.precio, 0);  // Sumar todos los precios

    let descuento = parseFloat(inputDescuento.value); // Obtener el descuento
    if (isNaN(descuento)) descuento = 0;  // Si no se ingresa un descuento válido, tomar 0

    let descuentoAplicadoTotal = total * (descuento / 100);  // Calcular el descuento
    let totalConDescuento = total - descuentoAplicadoTotal;  // Calcular el total con descuento

    // Actualizar los totales en la pantalla
    totalSinDescuento.textContent = `Total sin descuento: $${total.toFixed(2)}`;
    descuentoAplicado.textContent = `Descuento aplicado: $${descuentoAplicadoTotal.toFixed(2)}`;
    totalFinal.textContent = `Total final: $${totalConDescuento.toFixed(2)}`;
}

// Evento para agregar producto
botonAgregar.addEventListener("click", () => {
    const precio = parseFloat(inputPrecio.value);  // Obtener el precio del producto
    if (isNaN(precio) || precio <= 0) {
        alert("Por favor, ingresa un precio válido.");
        return;
    }

    productos.push({ precio: precio });  // Agregar el precio al array de productos
    inputPrecio.value = "";  // Limpiar el input
    renderizarProductos();  // Volver a renderizar la lista de productos
});

// Evento para calcular el total
botonCalcular.addEventListener("click", calcularTotal);
