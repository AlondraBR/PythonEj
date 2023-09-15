def condiciones():
    # Boletos
    # Horarios
    # Cual Cine
    # Peliculas
    # Dulceria
    # Pr
    print("Condiciones")
    presupuesto = 500
    costoBoletos = 300
    pelicula = "oppenheimer"
    cine = "Cinépolis"
    horario = 13
    costoDulceria = 200

    if presupuesto >= costoBoletos:
        print("Si iremos al cine")
        if cine == "Cinépolis":
            print("entrar a comprar boletos en cinéplis")
            if pelicula == "barbie":
                print("si esta la pelicula de barbie disponible")
            else:
                print("Aunqe tengo dinero, no entrare no entrare al cine porque no esta barbbie")
        else:
            print("No entrare porque no me gusta cinemex")
    else:
        print("No iremos al cine")

condiciones()
script.js
function condiciones() {
  //Boletos - ok
  //Horarios - ok
  //Cual Cine - ok
  //Peliculas - ok
  //Dulceria - ok
  //Presupuesto - ok
  console.log("Condiciones");
  let presupuesto = 500;
  let costoBoletos = 300;
  let pelicula = "barbie";
  let cine = "Cinépolis";
  let horario = 13;
  let costoDulceria = 200;

  if (presupuesto >= costoBoletos) {
    console.log("Si iremos al cine");
    if (cine == "Cinépolis") {
      console.log("Entrar a comprar boletos en Cinépolis");
      if (pelicula == "barbie") {
        console.log("Si esta la pelicula de barbie disponible");
        if (horario == 13) {
          console.log("Comprar boletos y verificare si hay dulces");
          if (presupuesto - costoBoletos >= costoDulceria) {
            console.log("Comprar palomitas y refresco, disfrutar la película");
          } else {
            let dineroRestante = presupuesto - costoBoletos;
            console.log(
              "Meter Hamburguesas de contrabando, porque solo me quedan " +
                dineroRestante
            );
          }
        } else {
          console.log("No hay horario disponible");
        }
      } else {
        console.log(
          "aunque tengo dinero, no entrare al cine porque no esta la película"
        );
      }
    } else {
      console.log("No entrare porque no me gusta cinemex");
    }
  } else {
    console.log("No iremos al cine");
  }
}

condiciones
@AlondraBR
 


    
