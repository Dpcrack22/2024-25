window.addEventListener("load", function() {
    var boto = document.getElementById("boto");
    boto.addEventListener("click",afegirArticle);
});

function afegirArticle() {
    var codi = document.getElementById("codi").value;
    var desc = document.getElementById("desc").value;
    var preu = document.getElementById("preu").value;
    var unitats = document.getElementById("unitats").value;
    var descompte = document.getElementById("descompte").value;
    
    var taula = document.getElementById("taula")
    var fila = taula.insertRow();
    
    fila.insertCell().innerHTML = codi;
    fila.insertCell().innerHTML = desc;
    fila.insertCell().innerHTML = preu;
    fila.insertCell().innerHTML = unitats;
    fila.insertCell().innerHTML = descompte;
    fila.insertCell().innerHTML = preuTotal(preu,unitats,descompte);
}

function preuTotal(preu,unitats,descompte)
{
    return ((preu*unitats) - (preu*unitats)*(descompte/100))
}
