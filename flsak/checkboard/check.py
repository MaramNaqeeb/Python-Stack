from flask import Flask,render_template
app = Flask(__name__)


@app.route ("/")
def index():
    return render_template("check.html")

@app.route("/<int:n1>")
def num(n1):
    return render_template("check2.html",my_boxes=n1)

@app.route("/<int:n1>/<int:n2>")
def num2(n1,n2):
    return render_template("with_x_y.html",x=n1, y= n2)

@app.route("/<int:x>/<int:y>/<my_color1>/<my_color2>")
def row (x,y, my_color1, my_color2):
    return render_template("with_color.html",n1=x,n2=y, color1= my_color1, color2=my_color2)

if __name__ == "__main__":
    app.run(debug=True)
