from flask import Flask, render_template, session, redirect

app=Flask(__name__)

app.secret_key="Fantasy Bibliophile 4 life"

@app.route('/')
def index():
    if "counter" not in session:
        session["counter"] = 0
    else:
        session["counter"] += 2
    return render_template("index.html")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)