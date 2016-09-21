from flask import Flask


app = Flask(__name__)
@app.route("/")
@app.route("/missPiggy")
@app.route("/kermit")

def WASSSUP():
    return __name__ + "  WASSSSSSSUPPP"


if __name__ == '__main__':
    app.run()



