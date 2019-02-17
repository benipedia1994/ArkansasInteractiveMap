from flask import Flask
from flask import render_template, url_for
app = Flask(__name__)

@app.route('/')
def map():
    return render_template("IntMap.html")

if __name__=='__main__':
    app.run(host='0.0.0.0', port = 5000, debug = True)