// Obtener los elementos del DOM
const inputTarea = document.getElementById("nuevaTarea");
const botonAgregar = document.getElementById("agregarTarea");
const listaTareas = document.getElementById("listaTareas");

// Array para guardar las tareas
let tareas = [];

// Función para renderizar la lista de tareas
function renderizarTareas() {
    listaTareas.innerHTML = "";  // Limpiar la lista actual

    // Usamos un bucle para crear un <li> por cada tarea en el array
    tareas.forEach((tarea, index) => {
        const tareaElemento = document.createElement("li");

        // Crear el texto de la tarea
        tareaElemento.textContent = tarea.texto;

        // Si la tarea está completada, agregar clase "completada"
        if (tarea.completada) {
            tareaElemento.classList.add("completada");
        }

        // Evento para marcar como completada al hacer clic
        tareaElemento.addEventListener("click", () => {
            tarea.completada = !tarea.completada;  // Cambiar el estado de la tarea
            renderizarTareas();  // Volver a renderizar la lista
        });

        // Crear el botón para eliminar la tarea
        const botonEliminar = document.createElement("button");
        botonEliminar.textContent = "Eliminar";
        botonEliminar.addEventListener("click", () => {
            tareas.splice(index, 1);  // Eliminar la tarea del array
            renderizarTareas();  // Volver a renderizar la lista
        });

        // Añadir el botón de eliminar al <li>
        tareaElemento.appendChild(botonEliminar);

        // Añadir el <li> a la lista de tareas
        listaTareas.appendChild(tareaElemento);
    });
}

// Evento para agregar tarea cuando se hace clic en el botón
botonAgregar.addEventListener("click", () => {
    const textoTarea = inputTarea.value.trim();  // Obtener el valor del input

    if (textoTarea) {
        tareas.push({ texto: textoTarea, completada: false });  // Agregar la tarea al array
        inputTarea.value = "";  // Limpiar el input
        renderizarTareas();  // Volver a renderizar la lista
    }
});
