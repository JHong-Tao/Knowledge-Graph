from flask import request
from flask import Flask, render_template

import kgview

app = Flask(__name__)


@app.route('/getword')
def get_keyword():
    keyword = request.args.get("keyword")
    nodes = kgview.kg_view(keyword)
    print(nodes)
    return nodes

@app.route("/test")
def test():
   return render_template("test.html")

@app.route("/")
def index():
   return render_template("index.html")

if __name__ == '__main__':
    app.run()
