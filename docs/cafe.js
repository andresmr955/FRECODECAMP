const boton = document.getElementById('miBoton');

function miFuncion() {
  alert('¡Hiciste clic!');
}

// Aquí estás *escuchando* el evento y lo conectas con tu función
boton.addEventListener('click', miFuncion);