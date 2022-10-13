from flask import *
app = Flask(__name__)
# name=request.values['user']

@app.route("/")
def index():
    # if name !="":
    #     return render_template("index.html", name=request.values['user'])
    # else:
    #     return render_template("index.html")
    return render_template("index.html")

@app.route("/admin/")
def admin():
    return render_template("admin.html")

@app.route("/po_ok", methods=["POST"])
def po_ok():
    title=request.form["title"]
    description=request.form["description"]
    salary=request.form["salary"]
    link=request.form["link"]
    print(title, description, salary, link)
    return ("ok")

if __name__ == '__main__':
    # app.debug = True
    app.run(port=3000)
