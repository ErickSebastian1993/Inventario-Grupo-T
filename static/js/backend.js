(function () {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
  
          form.classList.add('was-validated')
        }, false)
      })
  })()

  function registrar(/*usuario,contraseña,correo,nombre,id*/) {
    var usuario = document.getElementById(txtUsuario);
    var password = document.getElementById(txtPassword);
    var nombre = document.getElementById(txtNombre);
    var correo = document.getElementById(txtCorreo);
    var correo = document.getElementById(txtCorreo);
    

  }

  /*$( "form" ).on( "submit", function( event ) {
    event.preventDefault();
    console.log( $( this ).serialize() );
  });*/