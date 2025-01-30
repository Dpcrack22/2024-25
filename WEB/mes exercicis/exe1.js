function crear() {

  //CONTAINER
  var container = document.createElement('div');
  container.setAttribute('id', 'container');

  //HEAD
  var head = document.createElement('div');
  head.setAttribute('id', 'head');
  var h1Head = document.createElement('h1');
  h1Head.innerHTML = "Hello";
  head.appendChild(h1Head);

  //CONTAINERBODY
  var containerBody = document.createElement('div');
  containerBody.setAttribute('id', 'containerBody');

  var contBodyP1 = document.createElement('p');
  contBodyP1.innerHTML = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus est fuga incidunt cumque doloremque ex voluptatum natus sit dolor porro qui nostrum illo expedita labore rerum eos vel. Fugit est.';
  var contBodyP2 = document.createElement('p');
  contBodyP2.innerHTML = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolore nesciunt autem ducimus explicabo necessitatibus molestias.';
  containerBody.appendChild(contBodyP1);
  containerBody.appendChild(contBodyP2);
  container.appendChild(containerBody);

  //FOOTER
  var footer = document.createElement('div');
  footer.setAttribute('id', 'footer');
  var footerP = document.createElement('p');
  footerP.innerHTML = "&copy;";
  footer.appendChild(footerP);

  //AFEGIM ELS ELEMENTS A LA PÀGINA
  container.appendChild(head);
  container.appendChild(containerBody);
  container.appendChild(footer);
  document.body.appendChild(container);
}

crear();