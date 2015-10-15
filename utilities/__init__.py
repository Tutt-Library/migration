from remove_mods_namespace import remove_mods_namespace
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', 
            debug=True)

