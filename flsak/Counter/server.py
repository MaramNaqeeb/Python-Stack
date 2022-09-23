from flask import Flask, render_template,redirect, session 
app = Flask(__name__)
app.secret_key = "count"

@app.route("/")
def counter ():

    if 'counter' not in session:
        session['counter']=0
    else:
        session['counter']+=1

    return render_template ("counter.html",times=session['counter']) 


@app.route("/delete")
def clear():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)