from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
@app.route("/")
def hello_world():
    try:
        num1 = float(request.form.get('numero1'))
        num2 = float(request.form.get('numero2'))
        suma = num1 + num2
        resta = num1 - num2
        division = num1 / num2
        multiplicacion = num1 * num2 
    except:
        num1 = ''
        num2 = ''
        suma = ''
        resta = ''
        division = ''
        multiplicacion = ''
    return render_template("copyHello.html", n1 = num1 , n2 = num2, suma = suma , resta = resta , 
                           division = division, multiplicacion = multiplicacion )