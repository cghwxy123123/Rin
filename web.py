from flask import web,render_template,request
app = web(__name__)
@app.route("/")
def index():
    return render_template("index.html")
