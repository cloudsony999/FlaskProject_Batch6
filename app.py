from flask import Flask,render_template,request
from calc import  addition
app=Flask(__name__)


@app.route("/")
def index():
    return render_template("input.html")

@app.route("/testing")
def perform():
    n1=int(request.args.get("num1"))
    n2 = int(request.args.get("num2"))
    return addition(n1,n2)


if __name__=='__main__':
    app.run(debug=True)

