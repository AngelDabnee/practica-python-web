# $ .venv\Scripts\activate (en windows)
# $ flask --app hello run
# $ flask --app copyHello run --debug (para no estar reiniciando cada rato todo)
from flask import Flask,render_template,request,jsonify

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
@app.route("/")
def hello_world():
    print(request.method)
    print(request.form)
    try:
        num1 = float(request.form.get('numero1'))
        num2 = float(request.form.get('numero2'))
        suma = num1 + num2
        resta = num1 - num2
        division = num1 / num2
        multiplicacion = num1 * num2 
        print(suma)
        print(resta)
        print(division)
        print(multiplicacion)
    except:
        num1 = "" 
        num2 = ""
        suma = ""
        resta = ""
        division = ""
        multiplicacion = ""
#render_template("copyHello.html")
    return """<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Aplicación para realizar las operaciones matemáticas básicas</h1>
    <div class = "calcular">
        <form action="#" method="post">
            <p>Escribe el 1:</p><input type="number" name = "numero1" value='"""+str(num1)+"""'><br>
            <p>Escribe el 2:</p><input type="number" name = "numero2" value='"""+str(num2)+"""'><br>
            <input type="submit" value = "Calcular" id = "calcular"><br>
            <p id = "resultados"> Resultados<br>
            suma = """+str(num1)+"""+"""+str(num2)+"""="""+str(suma)+"""<br>
            resta = """+str(num1)+"""-"""+str(num2)+"""="""+str(resta)+"""<br>
            division = """+str(num1)+"""/"""+str(num2)+"""="""+str(division)+"""<br>
            multiplicacion = """+str(num1)+"""*"""+str(num2)+"""="""+str(multiplicacion)+"""<br>
            operaciones básicas
            
            
            </p>
        </form>
    </div>
</body>
</html>"""
     