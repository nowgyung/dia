from crypt import methods
from flask import Flask, render_template, request
import dia

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def index():
    # if request.method=='POST':
    esti = dia.getModel()
    # 당뇨여부 = esti.predict([[6.0, 148,72,35,0,33.6,0.6,50]])
    당뇨여부 = esti.predict([[1.0, 89,66,23,94,28.1,0.2,21]])

    return render_template("index.html", 당뇨여부=당뇨여부)

app.run(debug=True) 