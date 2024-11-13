from flask import Flask, render_template, request, url_for# Importamos flask y la funcion para renderizar html mediante su nombre.
app = Flask(__name__) #Creamos nuestra instancia de una aplicacion flask con el nombre de __main__

@app.route('/') #Establecemos una ruta sencilla, la cual retorna un mensaje
def index():
    return render_template("index.html")

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == "POST":

        notas = [int(request.form["nota1"]), int(request.form["nota2"]), int(request.form["nota3"])]
        asistencia = int(request.form["asistencia"])
        promedio = round(sum(notas)/3, 1)
        for nota in notas:
            if not(nota >= 0 and nota <= 70):
                error = "La nota debe estar en un rango de 0 a 70"
                break
            else:

                if promedio >= 40 and asistencia >= 75:
                    aprobado = True
                else:
                    aprobado = False
                error = None



        return render_template("ejercicio1.html", aprobado=aprobado, promedio=promedio, error = error)
    return render_template("ejercicio1.html")

@app.route('/ejercicio2', methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        nombres = [request.form["nombre1"], request.form["nombre2"], request.form["nombre3"]]
        for numero, nombre in enumerate(nombres):
        
            if numero == 0:
                mayor = nombre
            if len(mayor) < len(nombre):
                mayor = nombre
        return render_template("ejercicio2.html", mayor = mayor)
        
    else:
        return render_template("ejercicio2.html")


if __name__ == "__main__": #Ejecutamos nuestra app si el script fue ejecutado directamente por su nombre
    app.run(debug=True)