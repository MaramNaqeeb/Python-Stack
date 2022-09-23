from flask import Flask,render_template,request
app = Flask(__name__)
@app.route ("/")
def registration():
    return render_template ("registration.html")


@app.route('/result', methods=['POST'])
def show():
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comment = request.form['comment']
    

    return render_template("show.html", name_on_template=name_from_form, location_on_template=location_from_form,language_on_template=language_from_form,comment_on_template=comment)

if __name__ == "__main__":
    app.run(debug=True)