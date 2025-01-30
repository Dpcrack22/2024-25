window.onload = function() {

    function createElements(a) {
        if (!Array.isArray(a))
            throw "Error: el paràmetre ha de ser un array!"

        //Recorrem els elements de l'array
        for (var i in a) { //(var i=0;i<a.length;i++) 
            if (typeof(a[i]) != "string") {
                throw "Error: element index " + i + " ha de ser un string";
            }
            else {
                var element = document.createElement(a[i]);
                element.innerHTML = "Lorem ipsum dolor sit.";
                document.body.appendChild(element);
            }
        }

    }

    var prova = ['div', 'h2', 'p', 'a', 'h1'];

    createElements(prova);

}
